#!/bin/bash
echo "Generating markdown docs..."
pydoc-markdown
echo "Generating requirements.txt..."
python -m pip freeze > requirements.txt

echo "Running ruff format..."
ruff format .

echo "Running ruff check with autofix..."
ruff check . --fix

if [ $? -ne 0 ]; then
    echo "Ruff found errors that cannot be fixed automatically."
    exit 1
fi

echo "Ruff check passed."

echo "Enter commit message:"
read commit_message

if [ -z "$commit_message" ]; then
    echo "Commit message cannot be empty."
    exit 1
fi

echo "Git add..."
git add .

echo "Git commit..."
git commit -m "$commit_message"

echo "Git push..."
git push

echo "Code pushed successfully."