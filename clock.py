import datetime
import colorama
from colorama import Back, Fore, Style
colorama.init()

now = datetime.datetime.now()
print(Fore.GREEN + "Krishna Singh Rajput Clock :")
print(Fore.BLUE + now.strftime("%y-%m-%d %H:%M:%S"))