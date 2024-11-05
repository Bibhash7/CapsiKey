import re
import logging
from constantClassApp.constants import ErrorMessage

logger = logging.getLogger()


def check_alpha_string(string):
    """
    Checks if a string is completely alphanumeric.
    :param string:
    :return bool:
    """
    if string.replace("_", "").isalpha():
        return True
    return False


def create_constant_class(textstring):
    """
    Create key value pair of strings.
    :param textstring:
    :return string:
    """
    try:
        multiline_str = ""
        textstring = textstring.replace(" ", "")
        text_arr = re.split(r'[,\n]+', textstring)
        text_arr = [text.strip('\r') for text in text_arr if text.strip('\r')]
        for text in text_arr:
            if check_alpha_string(text):
                multiline_str += f'{text.upper()} = "{text}"\n'
            else:
                raise ValueError(ErrorMessage.NOT_A_ALPHA_STRING)
        return multiline_str

    except Exception as error:
        logger.error(error)
