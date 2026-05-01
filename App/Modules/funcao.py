#Libs Internas
import Config as cfg

#Libs externas
import telebot
import os
import json
from datetime import datetime

class Funcao():
    def __init__(self):
        self.bot              = telebot.TeleBot(cfg.Credenciais.token)
        self.id_canal         = cfg.Credenciais.id_canal
        self.caminho_enviar   = './App/Docs/Enviar'
        self.caminho_enviados = './App/Docs/Enviado'
        self._criar_caminhos()
    
    def enviar_mensagem(self):

        #verifica quantos arquivos existem na pasta
        arquivos = os.listdir(self.caminho_enviar)
        cfg.log.info(f"Quantidade de arquivos na pasta: {len(arquivos)}")

        if len(arquivos) == 0:
            cfg.log.info("Nenhum arquivo encontrado para enviar.")
            self._enviar_texto(self, '*Sem arquivos* para enviar!')
            return
        
        for arquivo in arquivos:
            #verifica a extensão do arquivo
            if arquivo.endswith('.txt'):
                with open(os.path.join(self.caminho_enviar, arquivo), 'r') as f:
                    texto = f.read()
                    if self._enviar_texto(texto):
                        excluir = True
                    cfg.log.info(f"Arquivo {arquivo} enviado para o canal.")
            else:
                cfg.log.info(f"Arquivo {arquivo} ignorado, extensão não suportada.")
                continue

            if excluir: os.remove(os.path.join(self.caminho_enviar, arquivo))
            excluir = False

    def _enviar_texto(self, texto):
        mensagem = self.bot.send_message(chat_id=self.id_canal, text=texto, parse_mode="Markdown")
        self._salvar_id_mensagem(mensagem)
        return True
    
    def _salvar_id_mensagem(self, mensagem):
        id_mensagem = mensagem.message_id
        horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not os.path.exists(f'{self.caminho_enviados}/ids_mensagens.json'):
            with open(f'{self.caminho_enviados}/ids_mensagens.json', 'w', encoding='utf-8') as f:
                json.dump({id_mensagem: horario}, f)

        else:
            with open(f'{self.caminho_enviados}/ids_mensagens.json', 'r', encoding='utf-8') as f:
                ids_mensagens = json.load(f)
            
            ids_mensagens[id_mensagem] = horario
            with open(f'{self.caminho_enviados}/ids_mensagens.json', 'w', encoding='utf-8') as f:
                json.dump(ids_mensagens, f)
                

    def _excluir_ultima_msgem(self, id_mensagem):
        with open(f'{self.caminho_enviados}/ids_mensagens.json', 'r', encoding='utf-8') as f:
            ids_mensagens = json.load(f)

        id_excluir = max(ids_mensagens, key=ids_mensagens.get)
        self.bot.delete_message(chat_id=self.id_canal, message_id=id_excluir)

    def _criar_caminhos(self):
        if not os.path.exists(self.caminho_enviar):
            os.makedirs(self.caminho_enviar)
        
        if not os.path.exists(self.caminho_enviados):
            os.makedirs(self.caminho_enviados)