import re
import logging
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


def check_and_create_constant_class(textstring):
    """
    Create key value pair of strings.
    :param textstring:
    :return string:
    """
    try:
        multiline_str = ""
        text_arr = re.split(r'[,\n\s]+', textstring)
        text_arr = [text.strip('\r') for text in text_arr if text.strip('\r')]
        for text in text_arr:
            if check_alpha_string(text):
                multiline_str += f'{text.upper()} = "{text}"\n'
            else:
                return None
        return multiline_str

    except Exception as error:
        logger.error(error)
