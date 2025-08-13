# Organizador de Notas Fiscais

![GitHub license](https://img.shields.io/github/license/thucosta/organizador-nf)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-produção-green)

Um aplicativo desktop com interface gráfica para organizar arquivos de notas fiscais (XML, PDF, P7S) em pastas com o formato "NFs prontas para envio - dia [data atual]".

![Screenshot do Aplicativo](docs/images/screenshot.png)

## 📋 Funcionalidades

- ✅ Interface gráfica amigável para seleção de pastas e visualização de arquivos
- ✅ Permite ao usuário selecionar a pasta de origem dos arquivos
- ✅ Permite ao usuário selecionar a pasta base de destino
- ✅ Cria automaticamente uma pasta de destino com o formato "NFs prontas para envio - dia [data atual]"
- ✅ Move arquivos de notas fiscais da pasta de origem para a pasta de destino
- ✅ Suporta arquivos XML, PDF e P7S
- ✅ Exibe uma lista dos arquivos encontrados
- ✅ Mostra o progresso da operação
- ✅ Registra todas as operações em um arquivo de log

## 📁 Estrutura do projeto

```
organizador-nf/
├── executar.bat                # Script para executar o programa
├── README.md                   # Documentação do projeto
├── LICENSE                     # Licença do projeto
├── .gitignore                  # Configuração do Git
├── docs/                       # Documentação adicional
│   └── images/                 # Imagens para documentação
├── release/                    # Pasta com o executável compilado
│   ├── OrganizadorNF.exe       # Executável compilado
│   └── README.md               # Documentação do programa
└── src/                        # Pasta com o código-fonte
    ├── organizar_nfs_gui.py    # Script principal com interface gráfica
    ├── requirements.txt        # Dependências do projeto
    ├── TH.ico                  # Ícone do executável
    ├── compilar_gui.bat        # Script para compilar o executável
    └── executar_gui.bat        # Script para executar o programa a partir do código-fonte
