#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Organizador de Notas Fiscais (Versão com Interface Gráfica)
Este script organiza arquivos de notas fiscais em pastas com o formato "NFs prontas para envio - dia [data atual]".
"""

import os
import shutil
import sys
import logging
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from typing import List
import subprocess

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("organizador_nf.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def criar_pasta_destino(pasta_base: str) -> str:
    """
    Cria uma pasta de destino com o formato "NFs prontas para envio - [data atual]".
    
    Args:
        pasta_base (str): Pasta base onde a pasta de destino será criada
        
    Returns:
        str: Caminho da pasta criada
    """
    # Obter a data atual no formato DD-MM-YYYY
    data_atual = datetime.now().strftime("%d-%m-%Y")
    
    # Criar o nome da pasta
    nome_pasta = f"NFs prontas para envio - dia {data_atual}"
    caminho_pasta = os.path.join(pasta_base, nome_pasta)
    
    # Criar a pasta se não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        logging.info(f"Pasta {caminho_pasta} criada com sucesso.")
    
    return caminho_pasta

def encontrar_arquivos_nf(diretorio: str) -> List[str]:
    """
    Encontra arquivos de notas fiscais no diretório especificado.
    
    Args:
        diretorio (str): Diretório onde procurar os arquivos
        
    Returns:
        List[str]: Lista de caminhos dos arquivos encontrados
    """
    extensoes = ['.xml', '.pdf', '.p7s']
    arquivos_nf = []
    
    for arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(arquivo)
            if extensao.lower() in extensoes:
                arquivos_nf.append(caminho_completo)
    
    return arquivos_nf

def mover_arquivos(arquivos: List[str], pasta_destino: str) -> int:
    """
    Move os arquivos para a pasta de destino.
    
    Args:
        arquivos (List[str]): Lista de caminhos dos arquivos a serem movidos
        pasta_destino (str): Caminho da pasta de destino
        
    Returns:
        int: Número de arquivos movidos com sucesso
    """
    contador = 0
    for arquivo in arquivos:
        try:
            nome_arquivo = os.path.basename(arquivo)
            destino = os.path.join(pasta_destino, nome_arquivo)
            shutil.move(arquivo, destino)
            logging.info(f"Arquivo {nome_arquivo} movido para {pasta_destino}")
            contador += 1
        except Exception as e:
            logging.error(f"Erro ao mover arquivo {arquivo}: {str(e)}")
    
    return contador

def abrir_pasta(caminho: str) -> None:
    """
    Abre a pasta no explorador de arquivos.
    
    Args:
        caminho (str): Caminho da pasta a ser aberta
    """
    try:
        if sys.platform == 'win32':
            os.startfile(caminho)
        elif sys.platform == 'darwin':  # macOS
            subprocess.Popen(['open', caminho])
        else:  # Linux
            subprocess.Popen(['xdg-open', caminho])
        logging.info(f"Pasta aberta: {caminho}")
    except Exception as e:
        logging.error(f"Erro ao abrir pasta {caminho}: {str(e)}")

class OrganizadorNFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Notas Fiscais")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Configurar o estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("TLabel", padding=6, font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 12, "bold"))
        
        # Criar o frame principal
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Organizador de Notas Fiscais", 
            style="Header.TLabel"
        )
        self.title_label.pack(pady=(0, 20))
        
        # Frame para pasta de origem
        self.origem_frame = ttk.Frame(self.main_frame)
        self.origem_frame.pack(fill=tk.X, pady=5)
        
        self.origem_label = ttk.Label(
            self.origem_frame, 
            text="Pasta de Origem:", 
            width=15
        )
        self.origem_label.pack(side=tk.LEFT)
        
        self.origem_entry = ttk.Entry(self.origem_frame)
        self.origem_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.origem_button = ttk.Button(
            self.origem_frame, 
            text="Selecionar", 
            command=self.selecionar_origem
        )
        self.origem_button.pack(side=tk.LEFT)
        
        # Frame para pasta de destino
        self.destino_frame = ttk.Frame(self.main_frame)
        self.destino_frame.pack(fill=tk.X, pady=5)
        
        self.destino_label = ttk.Label(
            self.destino_frame, 
            text="Pasta de Destino:", 
            width=15
        )
        self.destino_label.pack(side=tk.LEFT)
        
        self.destino_entry = ttk.Entry(self.destino_frame)
        self.destino_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.destino_button = ttk.Button(
            self.destino_frame, 
            text="Selecionar", 
            command=self.selecionar_destino
        )
        self.destino_button.pack(side=tk.LEFT)
        
        # Frame para informações
        self.info_frame = ttk.Frame(self.main_frame)
        self.info_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.info_label = ttk.Label(
            self.info_frame, 
            text="Status: Aguardando...", 
            anchor=tk.W
        )
        self.info_label.pack(fill=tk.X, pady=5)
        
        # Barra de progresso
        self.progress = ttk.Progressbar(
            self.info_frame, 
            orient=tk.HORIZONTAL, 
            length=100, 
            mode='determinate'
        )
        self.progress.pack(fill=tk.X, pady=5)
        
        # Lista de arquivos
        self.list_frame = ttk.LabelFrame(self.info_frame, text="Arquivos encontrados")
        self.list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.scrollbar = ttk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            self.list_frame, 
            yscrollcommand=self.scrollbar.set,
            selectmode=tk.EXTENDED
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar.config(command=self.listbox.yview)
        
        # Frame para botões
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        # Botão para sair
        self.sair_button = ttk.Button(
            self.button_frame, 
            text="Sair", 
            command=self.root.destroy
        )
        self.sair_button.pack(side=tk.LEFT, padx=5)
        
        # Botão para mover arquivos
        self.processar_button = ttk.Button(
            self.button_frame, 
            text="Mover Arquivos", 
            command=self.processar_arquivos
        )
        self.processar_button.pack(side=tk.RIGHT, padx=5)
        
        # Variáveis
        self.pasta_origem = ""
        self.pasta_destino = ""
        self.pasta_destino_final = ""
        self.arquivos_nf = []
        
    def selecionar_origem(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta de origem dos arquivos")
        if pasta:
            self.pasta_origem = pasta
            self.origem_entry.delete(0, tk.END)
            self.origem_entry.insert(0, pasta)
            self.info_label.config(text=f"Status: Pasta de origem selecionada: {pasta}")
            logging.info(f"Pasta de origem selecionada: {pasta}")
            
            # Verificar arquivos automaticamente quando a pasta de origem é selecionada
            self.verificar_arquivos()
    
    def selecionar_destino(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta base de destino")
        if pasta:
            self.pasta_destino = pasta
            self.destino_entry.delete(0, tk.END)
            self.destino_entry.insert(0, pasta)
            self.info_label.config(text=f"Status: Pasta de destino selecionada: {pasta}")
            logging.info(f"Pasta de destino selecionada: {pasta}")
    
    def verificar_arquivos(self):
        if not self.pasta_origem:
            return
        
        self.info_label.config(text="Status: Procurando arquivos de notas fiscais...")
        self.root.update()
        
        try:
            self.arquivos_nf = encontrar_arquivos_nf(self.pasta_origem)
            
            # Limpar a listbox
            self.listbox.delete(0, tk.END)
            
            if not self.arquivos_nf:
                self.info_label.config(text=f"Status: Nenhum arquivo de nota fiscal encontrado em {self.pasta_origem}.")
                logging.info(f"Nenhum arquivo de nota fiscal encontrado em {self.pasta_origem}.")
                return
            
            # Adicionar arquivos à listbox
            for arquivo in self.arquivos_nf:
                self.listbox.insert(tk.END, os.path.basename(arquivo))
            
            self.info_label.config(text=f"Status: Encontrados {len(self.arquivos_nf)} arquivos de notas fiscais.")
            logging.info(f"Encontrados {len(self.arquivos_nf)} arquivos de notas fiscais.")
            
        except Exception as e:
            erro = f"Erro ao verificar arquivos: {str(e)}"
            self.info_label.config(text=f"Status: {erro}")
            logging.error(erro)
            messagebox.showerror("Erro", erro)
    
    def processar_arquivos(self):
        if not self.pasta_origem:
            messagebox.showwarning("Aviso", "Selecione a pasta de origem primeiro.")
            return
        
        if not self.pasta_destino:
            messagebox.showwarning("Aviso", "Selecione a pasta de destino primeiro.")
            return
        
        # Verificar arquivos novamente para garantir que a lista está atualizada
        if not self.arquivos_nf:
            self.verificar_arquivos()
            if not self.arquivos_nf:
                messagebox.showinfo("Informação", f"Nenhum arquivo de nota fiscal encontrado na pasta selecionada.")
                return
        
        # Confirmar a operação de mover
        resposta = messagebox.askyesno(
            "Confirmar", 
            "Esta operação irá MOVER os arquivos da pasta de origem para a pasta de destino.\n\n"
            "Os arquivos serão removidos da pasta de origem.\n\n"
            "Deseja continuar?"
        )
        
        if not resposta:
            return
        
        try:
            self.info_label.config(text="Status: Criando pasta de destino...")
            self.root.update()
            
            # Criar a pasta de destino
            self.pasta_destino_final = criar_pasta_destino(self.pasta_destino)
            
            self.info_label.config(text=f"Status: Movendo arquivos para {self.pasta_destino_final}...")
            self.root.update()
            
            # Configurar a barra de progresso
            self.progress["maximum"] = len(self.arquivos_nf)
            self.progress["value"] = 0
            
            # Mover os arquivos
            contador = 0
            for i, arquivo in enumerate(self.arquivos_nf):
                try:
                    nome_arquivo = os.path.basename(arquivo)
                    destino = os.path.join(self.pasta_destino_final, nome_arquivo)
                    shutil.move(arquivo, destino)
                    logging.info(f"Arquivo {nome_arquivo} movido para {self.pasta_destino_final}")
                    contador += 1
                    
                    # Atualizar a barra de progresso
                    self.progress["value"] = i + 1
                    self.root.update()
                    
                except Exception as e:
                    logging.error(f"Erro ao mover arquivo {arquivo}: {str(e)}")
            
            # Mostrar mensagem de conclusão
            if contador > 0:
                mensagem = f"Operação concluída com sucesso!\n\n{contador} arquivos foram movidos para:\n{self.pasta_destino_final}"
                self.info_label.config(text=f"Status: {mensagem}")
                logging.info(f"Organização concluída. {contador} arquivos movidos.")
                messagebox.showinfo("Sucesso", mensagem)
                
                # Atualizar a lista de arquivos após mover
                self.arquivos_nf = []
                self.listbox.delete(0, tk.END)
            else:
                mensagem = "Nenhum arquivo foi movido."
                self.info_label.config(text=f"Status: {mensagem}")
                logging.info("Organização concluída. Nenhum arquivo movido.")
                messagebox.showinfo("Informação", mensagem)
            
        except Exception as e:
            erro = f"Erro durante a execução: {str(e)}"
            self.info_label.config(text=f"Status: {erro}")
            logging.error(erro)
            messagebox.showerror("Erro", erro)

def main():
    root = tk.Tk()
    app = OrganizadorNFApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 