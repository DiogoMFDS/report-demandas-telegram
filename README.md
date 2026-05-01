# Report Demandas Telegram Bot

Bot Telegram responsável por enviar mensagens a partir de arquivos colocados em uma pasta específica.

No momento envia arquivos: .txt
## O que o projeto faz

- Lê arquivos `.txt` em `App/Docs/Enviar`
- Envia o conteúdo de cada arquivo para um canal Telegram usando `telebot`
- Registra o `message_id` de cada envio em `App/Docs/Enviado/ids_mensagens.json`
- Gera logs de execução em `logs/`

## Pré-requisitos

- Python 3.8 ou superior
- Internet ativa para acesso à API do Telegram

## Instalação

1. No diretório do projeto, crie e ative o ambiente virtual:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

## Configuração

O bot usa `iniUts` para carregar credenciais de `App/config/init/prod.ini`.

- `App/Config/config_app.py` aponta para o arquivo `prod.ini` e usa a chave de criptografia `encryption_code`
- Ajuste o caminho ou a chave se necessário
- Configure o token do bot e o ID do canal dentro do `.ini`

> Observação: se quiser um ambiente de desenvolvimento separado, crie um arquivo semelhante a `dev.ini` e altere o caminho em `App/Config/config_app.py`.

## Uso

### Executar pela linha de comando
```powershell
python App\__main__.py
```

### Executar pelo arquivo batch
```powershell
executar.bat
```

O `executar.bat` também cria/ativa o ambiente virtual e instala as dependências se necessário.

## Como funciona

- `App/__main__.py` inicializa o logger e executa `Funcao.enviar_mensagem()`
- `App/Modules/funcao.py`:
  - cria as pastas `App/Docs/Enviar` e `App/Docs/Enviado` quando faltam
  - lista os arquivos em `App/Docs/Enviar`
  - envia cada `.txt` como mensagem Markdown para o canal Telegram
  - salva o `message_id` e data/hora em `App/Docs/Enviado/ids_mensagens.json`
  - remove o arquivo `.txt` enviado com sucesso

## Estrutura do projeto

- `App/__main__.py` — ponto de entrada da aplicação
- `App/Config/config_app.py` — carregamento de credenciais com `iniUts`
- `App/Config/config_log.py` — configuração de logs
- `App/Docs/Enviar/` — pasta de origem dos arquivos de texto a enviar
- `App/Docs/Enviado/` — pasta onde fica o histórico de IDs de mensagens enviadas
- `App/Modules/funcao.py` — lógica de envio e persistência
- `requirements.txt` — dependências do projeto
- `executar.bat` — atalho para rodar o bot no Windows

## Dependências

- `telebot` — cliente Telegram
- `iniUts` — leitura de arquivos `.ini`
- `cryptography`, `cffi`, `pycparser` — dependências da biblioteca de configuração

## Logs

Os logs são gravados em `logs/` por padrão. A configuração de log define:
- saída em arquivo
- saída no console
- formatação com data/hora, linha, módulo e nível

## Observações

- Apenas arquivos `.txt` são processados.
- O bot salva IDs de mensagens enviadas para possível controle posterior.
- Se não houver arquivos para enviar, o bot apenas registra e termina.


