@echo off
echo Executando o Organizador de Notas Fiscais (Versao GUI)...

REM Verificar se o Python está instalado
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Erro: Python nao encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

REM Executar o script
python organizar_nfs_gui.py

pause 