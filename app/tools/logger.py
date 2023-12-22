import logging

from rich.console import Console
from rich.logging import RichHandler


CONSOLE = Console(color_system="256", width=150, style="blue")
LOG_FORMAT_FN  = "[%(funcName)s: %(lineno)d] - %(message)s"
HIGHLIGHT = ["KEYWORD_1", "KEYWORD_2"]
    

def get_logger(module_name):
    logger = logging.getLogger(module_name)
    logger.propagate = False

    log_path = True
    log_format = LOG_FORMAT_FN

    handler = RichHandler(
        rich_tracebacks=False,
        console=CONSOLE,
        show_path=log_path,
        keywords=HIGHLIGHT
        )

    handler.setFormatter(logging.Formatter(log_format))
    
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger
