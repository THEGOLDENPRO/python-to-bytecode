from io import StringIO
from dis import dis

from devgoldyutils import Colours
from . import pytob_logger
from .info import DISPLAY_NAME, COPYRIGHT

class Api():

    def get_display_name(self):
        return DISPLAY_NAME

    def to_bytecode(self, code:str) -> str:
        """Converts python code and returns the bytecode."""
        string_io = StringIO()
        dis(code, file=string_io)
        string_io.seek(0)

        pytob_logger.info(f"""{Colours.ORANGE.apply_to_string('Python')} -> {Colours.PINK_GREY.apply_to_string('Bytecode')}

{code}

{string_io.read()}
        """)

        string_io.seek(0)
        return string_io.readlines()