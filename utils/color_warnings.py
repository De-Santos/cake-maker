import warnings

from colorama import Fore, Style


def custom_formatwarning(message, category, filename, lineno, line):
    return f"{Fore.YELLOW}Warning: '{category.__name__}': {message}{Style.RESET_ALL}\n"


warnings.formatwarning = custom_formatwarning
