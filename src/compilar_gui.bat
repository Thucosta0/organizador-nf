@echo off
echo Compilando o Organizador de Notas Fiscais (Versao GUI)...

REM Verificar se o Python está instalado
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Erro: Python nao encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

REM Compilar o executável
echo Compilando o executavel...
python -m PyInstaller --onefile --windowed --icon=TH.ico --name=OrganizadorNF --hidden-import=tkinter --hidden-import=tkinter.filedialog --hidden-import=tkinter.messagebox --hidden-import=tkinter.ttk organizar_nfs_gui.py

if %ERRORLEVEL% neq 0 (
    echo Erro durante a compilacao. Verifique se o PyInstaller esta instalado.
    pause
    exit /b 1
)

REM Copiar o executável para a pasta release
if not exist "..\release" mkdir "..\release"
copy /Y "dist\OrganizadorNF.exe" "..\release\"

echo Build concluido com sucesso! O executavel esta na pasta 'release'.

pause 