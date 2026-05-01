import Config as cfg
from Libs     import *
from Models   import *
from Modules  import *

def __main__():

    cfg.log.info("Iniciando aplicação...")
    envio_demanda = Funcao()
    envio_demanda.enviar_mensagem()

if __name__ == "__main__":
    __main__()