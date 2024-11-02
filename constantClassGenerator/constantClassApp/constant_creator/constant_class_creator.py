import logging
from constantClassApp.constants import ErrorMessage

logger = logging.getLogger()


def check_alpha_string(string):
    if string.replace("_", "").isalpha():
        return True
    return False


def create_constant_class(textstring):
    try:
        multiline_str = """"""
        textstring = textstring.replace(" ", "")
        text_arr = textstring.split(",")
        for text in text_arr:
            if check_alpha_string(text):
                multiline_str += text.upper() + " = " + f'"{text}"' + "\n"
            else:
                raise ValueError(ErrorMessage.NOT_A_ALPHA_STRING)
        return multiline_str

    except Exception as error:
        logger.error(error)
