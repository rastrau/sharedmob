git filter-repo --path-glob '*.zip' --invert-paths --force

git gc --aggressive --prune=now

git push --force --all

git push --force --tags
