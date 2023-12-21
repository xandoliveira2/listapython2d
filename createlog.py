import logging
log = logging.getLogger(__name__)
log.propagate = False # por padrao é True, precisamos botar em False para que quando importemos ele não de logger
log.info('Olá')