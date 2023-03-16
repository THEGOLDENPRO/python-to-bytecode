import webview
from devgoldyutils.logging import LoggerAdapter, Colours, log, add_custom_handler

LOGGER_NAME = f"{Colours.ORANGE.value}Python {Colours.RESET_COLOUR.value}To {Colours.GREY.value}Bytecode{Colours.RESET_COLOUR.value}"
pytob_logger = add_custom_handler(log.getLogger(LOGGER_NAME)); pytob_logger.setLevel(log.DEBUG)

from .js_api import Api

class PythonToBytecode():
    def __init__(self) -> None:
        """The main class of the application"""

        self.logger = LoggerAdapter(
            pytob_logger, 
            prefix = "PythonToBytecode"
        )
    
    def start(self):
        webview.create_window(
            "Python To Bytecode", 
            "./web/index.html", 
            js_api = Api(), 
            min_size = (1050, 634)
        )

        webview.start()