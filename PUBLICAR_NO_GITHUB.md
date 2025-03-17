# Instruções para publicar no GitHub

## Pré-requisitos

1. Ter uma conta no GitHub
2. Ter o Git instalado no seu computador
   - Você pode baixar o Git em: https://git-scm.com/downloads
3. Configurar o Git com seu nome e email:
   ```
   git config --global user.name "Seu Nome"
   git config --global user.email "seu-email@exemplo.com"
   ```

## Método 1: Usando o script automatizado

1. Edite o arquivo `publicar_no_github.bat` e substitua `seu-usuario` pelo seu nome de usuário do GitHub
2. Execute o arquivo `publicar_no_github.bat`
3. Quando solicitado, insira suas credenciais do GitHub

## Método 2: Passo a passo manual

1. Crie um novo repositório no GitHub:
   - Acesse https://github.com/new
   - Dê um nome ao repositório, como "organizador-nf"
   - Adicione uma descrição
   - Deixe o repositório como público
   - Não inicialize o repositório com README, .gitignore ou licença
   - Clique em "Create repository"

2. Abra um terminal (Prompt de Comando ou PowerShell) na pasta do projeto

3. Inicialize o repositório Git:
   ```
   git init
   ```

4. Adicione todos os arquivos ao repositório:
   ```
   git add .
   ```

5. Faça o primeiro commit:
   ```
   git commit -m "Versão inicial do Organizador de Notas Fiscais"
   ```

6. Adicione o repositório remoto (substitua `seu-usuario` pelo seu nome de usuário do GitHub):
   ```
   git remote add origin https://github.com/thucosta/organizador-nf.git
   ```

7. Envie para o GitHub:
   ```
   git push -u origin master
   ```

8. Quando solicitado, insira suas credenciais do GitHub

## Verificação

Após a publicação, acesse seu repositório no GitHub para verificar se todos os arquivos foram enviados corretamente:
```
https://github.com/thucosta/organizador-nf
```

## Configurando o GitHub Pages (opcional)

Para criar uma página web para o seu projeto:

1. Acesse as configurações do repositório no GitHub
2. Role até a seção "GitHub Pages"
3. Selecione a branch "master" como fonte
4. Clique em "Save"

Após alguns minutos, seu projeto estará disponível em:
```
https://thucosta.github.io/organizador-nf/
``` 