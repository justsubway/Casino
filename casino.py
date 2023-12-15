import sys as s
import numpy as np
import termcolor
from termcolor import colored
from colorama import Fore, Back, Style


text = colored(" _____   ___   _____ _____ _   _ _____   _ ", "magenta", attrs=['blink'],)
text2 = colored("/  __ \ / _ \ /  ___|_   _| \ | |  _  | | |", "magenta", attrs=['blink'])
text3 = colored("| /  \// /_\ \/ `--.  | | |  \| | | | | | |", "magenta", attrs=['blink'])
text4 = colored("| |    |  _  | `--. \ | | | . ` | | | | | |", "magenta", attrs=['blink'])
text5 = colored("| \__/\| | | |/\__/ /_| |_| |\  \ \_/ / |_|", "magenta", attrs=['blink'])
text6 = colored(" \____/\_| |_/\____/ \___/\_| \_/\___/  (_)", "magenta", attrs=['blink'])
text7 = colored("                                           ", "magenta", attrs=['blink'])
text8 = colored("Enter how much you wish to bet", "green")

print("                                                                       ")
print(text)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)


name = str(input("Enter your name: "))
age = float(input("Enter your age: "))

bet = (np.random.randint(-10,10))
if age>=18:
    print("Welcome to the Casino!")
    print("")
    stake = float(input("Enter how much you wish to bet: "))
    result = bet*stake
    finalresult = abs(result)
    if result>bet:
     print(Fore.GREEN + name, "you won! You get back:", finalresult, "$")
    elif result<bet:
     print(Fore.RED + name, "you lost! Amount you owe the casino:", finalresult, "$",)
    else: 
     print(name, "you didn't win or lose anything. Try again later.")
else:
    print("You're not old enough to get into the casino!")
print(Fore.WHITE + "Thank you for playing!")


