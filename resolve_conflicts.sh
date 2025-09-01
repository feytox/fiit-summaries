#!/bin/bash

# Script to resolve merge conflicts between main and site branches
# This script preserves site-specific content while merging main updates

echo "Resolving merge conflicts..."

# Handle content/index.md specifically 
if [ -f content/index.md ] && git status --porcelain | grep -q "^UU.*content/index.md"; then
    echo "Resolving content/index.md conflict..."
    
    # Create a merged version that preserves site intro but uses main content
    cat > content/index.md << 'EOF'
#### О сайте
Данный сайт это web-версия конспектов из [репозитория](https://github.com/feytox/fiit-summaries). На сайте возможны баги, поэтому советую пользоваться Obsidian. Подробная информация о конспектах описана в [репозитории](https://github.com/feytox/fiit-summaries)

Отличия от Obsidian:
- Конспекты здесь синхронизируются автоматически в течение нескольких минут после push в main.
- Некоторый текст, возможно, отображается по-другому

EOF
    
    # Append content from main branch (skip any existing "О сайте" section)
    git show origin/main:content/index.md | sed '/^#### О сайте/,/^$/d; /^#### Отличия от Obsidian:/,/^$/d' >> content/index.md
    
    git add content/index.md
    echo "Resolved content/index.md"
fi

# For any other conflicts, prefer main branch version
for file in $(git status --porcelain | grep "^UU" | cut -c4-); do
    if [ "$file" != "content/index.md" ]; then
        echo "Resolving $file by using main branch version..."
        git checkout --theirs "$file"
        git add "$file"
    fi
done

echo "All conflicts resolved"