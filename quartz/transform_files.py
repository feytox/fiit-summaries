# -*- coding: utf-8 -*-
import os

def main():
    count = 0
    for root, _, files in os.walk("content"):
        for file in files:
            transform_file(os.path.join(root, file))
            count += 1
    print(f"{count} files has been transoformed to quartz format")

def transform_file(path: str):
    if not path.endswith(".md"):
        return

    new_lines = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
        has_spoiler = False
        
        for line in lines:
            if "```spoiler" in line:
                has_spoiler = True
                continue
            if has_spoiler and "```" in line:
                has_spoiler = False
                continue
            # "компилятор" думает, что <\epsilon - тэг, поэтому крашится
            if has_spoiler:
                line = line.replace(" < ", "<").replace("<", " < ")
            new_lines.append(line)
    with open(path, 'w', encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    main()