import os
from os.path import isdir
import subprocess
def startup_text():
    print("\nWelcome to (prooted) Alpine Linux!\nThis linux distribution is based on the Alpine filesystem.\n\nTo install packages, type apk add <package>\nPackage names should be mostly the same as on ubuntu/debian distro's.\nIf you can't find a package, use /sbin/apk search, or simply google <package name> alpine.\n\nBy default ssh, python, pip and bash (your new default shell) are already installed.\n\nIf you need help, The Alpine Wiki contains a large amount of how-to guides and general\ninformation about administrating Alpine systems.\nSee <https://wiki.alpinelinux.org/>.\n")

startup_text()

os.system("mkdir /home")
os.system("export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")
os.system("export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin | /bin/bash")
os.system("touch /dev/null")

bin_directories = ["/bin", "/usr/bin", "/usr/sbin", "/sbin"]

directory = "/home"
def change_directory(user_input):
    global directory
    if user_input.startswith("cd .."):
        directory = os.path.dirname(directory) # move up 1

    elif user_input.startswith("cd /"):
        new_user_input = user_input[3:]
        if os.path.isdir(new_user_input):
            directory = os.path.normpath(new_user_input)
            print(new_user_input)
        else:
            print("[ERROR] not a valid directory!")
    
    elif user_input.startswith("cd "):
        new_dir = f"{user_input[3:]}"
        new_dir = os.path.normpath(f"/{new_dir}") # sanitize directory path, clearing double //
        print(new_dir)
        newnew_dir = directory + new_dir
        if os.path.isdir(newnew_dir):
            directory = newnew_dir
        else:
            print("[ERROR] That directory does not exist.")
    
    elif user_input.startswith("cd") or user_input.startswith("cd ~"):
        directory = "/home"
    
    directory = directory.replace("//", "/")

    if not os.path.isdir(directory):
        print("[ERROR] An unknown error occurred setting the directory. Defaulting to /")
        directory = "/"
    return directory

def apt_frontend(user_input):
    user_input = user_input.replace("apt", "apk")
    user_input = user_input.replace("install", "add")
    user_input = user_input.replace("remove", "del")
    user_input = user_input.replace("uninstall", "del")
    execute_cmd(user_input)

def execute_cmd(user_input):
    custom_env = {
    'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    'HOME': '/home'
    }
    if user_input == "":
        user_input = ":"
    subprocess.run(['/bin/bash', '-c', f"cd {directory} && {user_input}"], env=custom_env)


while True:
    print("[root@iwanttobreakfree] " + directory)
    user_input = input("")
    if user_input.startswith("cd"):
        directory = change_directory(user_input)
    elif user_input == "exit" or user_input == "/quit" or user_input == "stop" or user_input == "quit":
        exit(0)
    elif user_input.startswith("apt") or user_input.startswith("sudo apt"):
        apt_frontend(user_input)
    elif user_input.startswith("systemctl") or user_input.startswith("systemd"):
        print("[ERROR] nuh-uh. Please use <openrc> and <rc-update>, not systemd")
    else:
        execute_cmd(user_input)


#    match user_input:
#        case str if str.startswith("apt"):
#            user_input.replace("apt", "apk")
#        
#        case "bash":
#            print("Bash is available, but using anything other than the default shell may be broken.\nIf you #want to continue, type /bin/bash instead.")
#        case _:
#            is_bin = False
#            # check
#            try:
#                first_word_user_input = user_input.split()[0]
#                for directory in bin_directories:
#                    if os.path.exists(f"{directory}/{first_word_user_input}"):
#                        os.system(f"{directory}/{user_input}")
#                        is_bin = True
#            except:
#                pass
#            
#            if not is_bin: