@echo off
echo Publicando o projeto no GitHub...

REM Substitua "seu-usuario" pelo seu nome de usuário do GitHub
set GITHUB_USER=thucosta
set REPO_NAME=organizador-nf

REM Inicializar o repositório Git
git init

REM Adicionar todos os arquivos ao repositório
git add .

REM Fazer o primeiro commit
git commit -m "Versão inicial do Organizador de Notas Fiscais"

REM Adicionar o repositório remoto
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git

REM Enviar para o GitHub
git push -u origin master

echo.
echo Projeto publicado com sucesso no GitHub!
echo Acesse: https://github.com/%GITHUB_USER%/%REPO_NAME%
echo.

pause 