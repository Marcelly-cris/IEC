import structlog
import logging

# Configuração do logger
logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
log = structlog.get_logger()

# Exemplo de log estruturado
log.info("Iniciando aplicação", user="João", action="Login")
log.error("Erro ao acessar recurso", user="João", error_code=404)
