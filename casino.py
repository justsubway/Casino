import sys as s
import numpy as np
import termcolor
from termcolor import colored
from colorama import Fore, Back, Style
import time


text = colored(" _____   ___   _____ _____ _   _ _____   _ ", "magenta", attrs=['blink'],)
text2 = colored("/  __ \ / _ \ /  ___|_   _| \ | |  _  | | |", "magenta", attrs=['blink'])
text3 = colored("| /  \// /_\ \/ `--.  | | |  \| | | | | | |", "magenta", attrs=['blink'])
text4 = colored("| |    |  _  | `--. \ | | | . ` | | | | | |", "magenta", attrs=['blink'])
text5 = colored("| \__/\| | | |/\__/ /_| |_| |\  \ \_/ / |_|", "magenta", attrs=['blink'])
text6 = colored(" \____/\_| |_/\____/ \___/\_| \_/\___/  (_)", "magenta", attrs=['blink'])
text7 = colored("                                           ", "magenta", attrs=['blink'])
text8 = colored("Enter how much you wish to bet", "green")
incorrect = colored("Please select an option!", "red")
gamechoice = colored("\nWhich game do you wish to play?\n", "yellow")
choice1 = colored("[1] Random Bet\n", "green")
choice2 = colored("[2] Guess the number:\n", "light_blue")

print("                                                                       ")
print(text)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)


name = str(input(colored("Enter your name: ", "light_magenta")))
age = float(input(colored("Enter your age: ", "light_magenta")))


reply = "incorrect"
def start() :
    global reply
    if age>=18:
        choice = (input(gamechoice + choice1 + choice2 + ":"))
        if "1" in choice:
                reply = "correct"
                print (colored("\n Welcome to Betting!\n", "cyan"))
                bet = (np.random.randint(-10,10))
                stake = float(input("Enter how much you wish to bet: "))
                result = bet*stake
                finalresult = abs(result)
                if result>bet:
                    print(Fore.GREEN + name, "you won! You get back:", finalresult, "$")
                    print(Fore.WHITE + "Thank you for playing!")
                elif result<bet:
                    print(Fore.RED + name, "you lost! Amount you owe the casino:", finalresult, "$",)
                    print(Fore.WHITE + "Thank you for playing!")
                else: 
                    print(name, "you didn't win or lose anything. Try again later.")
                    print(Fore.WHITE + "Thank you for playing!")        
        elif "2" in choice:
                print("Welcome to guess the number!\n")
                reply = "correct" 
                number = (np.random.randint(1,20))
                playersnumber = float(input("Enter your guess (1-20): "))
                bet = float(input("Enter the amount of betting: "))
                if number == playersnumber:
                    print("You won! Your earnings doubled, so you got:", bet*2)
                else:
                    print(colored("You lost... Better luck next time!", "red"))
        else:
            print(incorrect)
    else:
                print(colored("You're not old enough to get into the casino!", "red"))
                reply = "correct"      
while reply == "incorrect":
    time.sleep(2)
    start()

