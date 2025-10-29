echo "# overview" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ProgramaFuturoCientista/overview.git
git push -u origin main

Para futuras atualizações:
Quando a branch master estiver à frente da main, execute:

git checkout main
git merge master
git push origin main
git checkout master