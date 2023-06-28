import os


if __name__ == '__main__':
    print("Welcome to KARROB. A RoboSpeaker created by KARAN")
    while True:
        x= input("Enter your command : ")
        if x == 'q':
            os.system("say 'Bye Bye friend'")
            break
        command = f"say {x}"
        os.system(command)

