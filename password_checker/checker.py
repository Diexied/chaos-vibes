from colorama import Fore, Style, init

init()

def password_checker(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("make it FAT and juciy bruhh😮‍💨")
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("put those letters in upper case bruh! let them see some world!")
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("some needs to be put down too!")
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("throw in some digits tooo, why are you being such a stingy?😒")
    if any(char in "!@#$%^&*()><?}{|" for char in password):
        strength += 1
    else:
        feedback.append("add some cute details bruh!!")
    if strength == 5:
        return Fore.GREEN + "password is strong as hell bruhhh😏👌🔥" + Style.RESET_ALL 
    elif strength == 3:
        return Fore.YELLOW + "password is mid ngl👀\nMissing:\n- " + "\n- ".join(feedback) + Style.RESET_ALL
    else:
        return Fore.RED + "dude just what is this bruh?? go change it✏️😭🙏🏼\nMissing:\n- " + "\n- ".join(feedback) + Style.RESET_ALL

#real one!
user_input = input("Enter your pasword, lets see😏 : ")
result = password_checker(user_input)
print(result)      
