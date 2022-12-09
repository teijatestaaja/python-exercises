def congratulate():
    name = input("Hello! What's your name? ")
    message = "Congratulations, " + name + "! You are the best!"
    print(message)
    return message

if __name__ == '__main__':
    congratulate()