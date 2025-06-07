import markdown
from pathlib import Path
import re
from bs4 import BeautifulSoup

SCRIPT_DIR = Path(__file__).resolve().parent

class StructureNode:
    def __init__(self, path=Path(), parent=None):
        self.title : str = path.stem
        self.dirs : dict[str, StructureNode] = dict()
        self.markdown_files : dict[str, StructureNode] = dict()
        self.path : Path = path
        self.parent : StructureNode = parent


class Structure:
    def __init__(self, content_path, result_path):
        self.folder_content = content_path
        self.folder_result = result_path

        self.tree = StructureNode()
        for path in self.folder_content.rglob("*"):
            if path.is_file():
                if path.suffix == ".md":
                    self._add_file(self.get_relative_path_content(path))
            if path.is_dir():
                self._add_dir(self.get_relative_path_content(path))

    def get_relative_path_content(self, path):
        return path.relative_to(self.folder_content)

    def get_absolute_path_result(self, relative_path):
        return self.folder_result / relative_path

    def get_absolute_path_content(self, relative_path):
        return self.folder_content / relative_path

    def _add_file(self, path: Path):
        node = self._add_dir(path.parent)
        file = StructureNode(path, node)
        node.markdown_files[path.name] = file
        return file

    def _add_dir(self, path):
        if path == Path('.'):
            return self.tree
        node = self._add_dir(path.parent)
        if path.name in node.dirs:
            return node.dirs[path.name]
        child = StructureNode(path, node)
        node.dirs[path.name] = child
        return child

    def __iter__(self):
        for el in self._get_dir_subtree(self.tree):
            yield el

    def _get_dir_subtree(self, node: StructureNode):
        yield node
        for dirs in node.dirs.values():
            for el in self._get_dir_subtree(dirs):
                yield el

    def find_node_relative_path(self, root_node: StructureNode, link: str):
        separated_link = link.split("/", 2)
        if len(separated_link) > 1:
            return root_node.dirs[separated_link[0]].path.name / self.find_node_relative_path(
                root_node.dirs[separated_link[0]],
                separated_link[1]
            )

        for file in root_node.markdown_files.values():
            if file.title == link:
                return file.path.relative_to(root_node.path)
        for directory in root_node.dirs.values():
            path = self.find_node_relative_path(directory, link)
            if path is not None:
                return directory.path.name / path
        return None

class App:
    def __init__(self):
        # Use absolute paths based on the script's location
        self.folder_content = SCRIPT_DIR / "content"
        self.folder_result = SCRIPT_DIR / "docs"
        self.folder_result.mkdir(exist_ok=True)
        self.structure = Structure(self.folder_content, self.folder_result)

    def convert(self):
        for node in self.structure:
            for dirs in node.dirs.values():
                self.create_dir(dirs)
            for file in node.markdown_files.values():
                self.create_html_file(file)

    def create_dir(self, node: StructureNode):
        path = self.structure.get_absolute_path_result(node.path)
        path.mkdir(exist_ok=True)

    def link_changer(self, node: StructureNode, obsidian_link: str):
        """obsidian_links format: [[ссылка|название]], [[название=ссылка]]"""
        namelink = obsidian_link.strip().strip("[").strip("]").strip().split("|")
        name = namelink[0]
        link = namelink[0]
        if len(namelink) == 2:
            name = namelink[1]

        relative_path = self.structure.find_node_relative_path(node, link)

        if relative_path is not None:
            relative_path = relative_path.with_suffix(".html")
            return f'<a href="{relative_path}">{name}</a>'
        return f"<span>{name}</span>"


    def replace_manual(self, text, pattern, node):
        result_parts = []
        last_end = 0
        for match in re.finditer(pattern, text):
            result_parts.append(text[last_end:match.start()])
            result_parts.append(self.link_changer(node.parent, text[match.start():match.end()]))
            last_end = match.end()
        result_parts.append(text[last_end:])
        return "".join(result_parts)

    def create_html_file(self, node: StructureNode):
        source_path = self.structure.get_absolute_path_content(node.path)
        result_path = self.structure.get_absolute_path_result(node.path)
        html_path = result_path.with_suffix(".html")

        template_file_path = SCRIPT_DIR / "code_assets/mdtemplate.html"
        with open(template_file_path, encoding="utf-8") as f:
            template_html = f.read()
        with open(source_path, encoding="utf-8") as f:
            md_text = f.read()

        markdown_html = markdown.markdown(md_text, extensions=['nl2br'])
        markdown_html = (markdown_html
                         .replace("<em>", "")
                         .replace("</em>", "")
                         )
        markdown_html = re.sub(
            r'<code>spoiler-markdown(.*?)</code>',
            r'<div class="spoiler-markdown"><p>\1</p></div>',
            markdown_html, flags=re.DOTALL
        )
        markdown_html = re.sub(
            r'```spoiler-markdown(.*?)```',
            r'<div class="spoiler-markdown"><p>\1</p></div>',
            markdown_html, flags=re.DOTALL
        )

        markdown_html = self.replace_manual(
            markdown_html,
            r'\[\[(.*?)\|(.*?)\]\]|\[\[(.*?)\]\]',
            node
        )
        soup = BeautifulSoup(template_html, features="html.parser")
        context_html = f"<h1>{source_path.stem}</h1>"
        soup.find("title").string = source_path.stem
        if source_path.stem == "index":
            context_html = ""
            soup.find("title").string = "Главная страница"

        if context_html:
            soup.body.div.append(BeautifulSoup(context_html, features="html.parser"))
        
        if markdown_html:
            soup.body.div.append(BeautifulSoup(markdown_html, features="html.parser"))

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(str(soup))

if __name__ == "__main__":
    app = App()
    app.convert()
