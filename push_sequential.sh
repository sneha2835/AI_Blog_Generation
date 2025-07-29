declare -a files=(
    "BlogGen/settings.py"
    "BlogGen/urls.py"
    "BlogGen/views.py"
    "api/views.py"
    "requirements.txt"
    "../frontend/requirements.txt"
    "api/exceptions.py"
    "api/utils/"
    "../frontend/app.py"
)

for file in "${files[@]}"
do
    if [ -e "$file" ] || [ -d "$file" ]; then
        git add "$file"
        git commit -m "Update $file"
        git push origin main
        echo "✅ Pushed $file"
    else
        echo "⚠️  Skipped $file (not found)"
    fi
done

# 4. Pop stashed changes back
git stash pop