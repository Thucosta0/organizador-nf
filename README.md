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

## 🔧 Requisitos

- Python 3.8 ou superior
- Tkinter (incluído na instalação padrão do Python)
- PyInstaller 6.10.0 ou superior (apenas para compilar o executável)

## 📦 Instalação

### Método 1: Usando o executável pré-compilado

1. Baixe a última versão do executável na [página de releases](https://github.com/thucosta/organizador-nf/releases)
2. Extraia o arquivo ZIP
3. Execute o arquivo `executar.bat` ou diretamente o `OrganizadorNF.exe` na pasta `release`

### Método 2: Usando o código-fonte

1. Clone o repositório:
   ```
   git clone https://github.com/thucosta/organizador-nf.git
   cd organizador-nf
   ```

2. Navegue até a pasta `src`
3. Instale as dependências:
   ```
   python -m pip install -r requirements.txt
   ```

4. Execute o script:
   ```
   python organizar_nfs_gui.py
   ```

   Ou use o arquivo batch fornecido:
   ```
   executar_gui.bat
   ```

## 🚀 Como usar

1. Execute o arquivo `executar.bat` na raiz do projeto
   - Ou execute diretamente o arquivo `OrganizadorNF.exe` na pasta `release`
2. Clique no botão "Selecionar" ao lado de "Pasta de Origem" para escolher a pasta de origem dos arquivos
   - Os arquivos serão verificados automaticamente e exibidos na lista
3. Clique no botão "Selecionar" ao lado de "Pasta de Destino" para escolher a pasta base de destino
4. Clique no botão "Mover Arquivos" para mover os arquivos para a pasta de destino
5. Confirme a operação quando solicitado
6. Os arquivos serão movidos para a pasta de destino com o formato "NFs prontas para envio - dia [data atual]"
7. Clique no botão "Sair" para fechar o programa quando terminar

## 🛠️ Compilando o executável

1. Navegue até a pasta `src`
2. Execute o script de build fornecido:
   ```
   compilar_gui.bat
   ```

O executável será gerado na pasta `release` com o nome `OrganizadorNF.exe`.

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
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

1. Faça um fork do projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Seu Nome - [seu-email@exemplo.com](mailto:seu-email@exemplo.com)

Link do projeto: [https://github.com/thucosta/organizador-nf](https://github.com/thucosta/organizador-nf) 