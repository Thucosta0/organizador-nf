@echo off
echo Executando o Organizador de Notas Fiscais...

REM Verificar se o executável existe
if exist "release\OrganizadorNF.exe" (
    start "" "release\OrganizadorNF.exe"
) else (
    echo Executavel nao encontrado. Compilando o programa...
    cd src
    call compilar_gui.bat
    cd ..
    if exist "release\OrganizadorNF.exe" (
        start "" "release\OrganizadorNF.exe"
    ) else (
        echo Erro: Nao foi possivel compilar o programa.
        pause
        exit /b 1
    )
) 