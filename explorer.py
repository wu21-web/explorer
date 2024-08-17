import os
import webbrowser
import time
import tqdm
import platform

history = list()

def delete(path):   #DONE
    try:
        os.remove(path)
    except IsADirectoryError:
        print("It is a directory.")
    else:
        print("Cannot perform operations to file.")

def rmdir(path):   #DONE
    os.system("rm -ri " + path)

def opendir(dir):   #DONE
    os.system("cd " + path)

def lis(dir):    #DONE
    os.system("ls")

def makedir(dirname):    #DONE
    os.system("mkdir " + dirname)

def read(path):   #DONE
    try:
        with open(path, mode="r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file.")

def wrt(path, contents): #DONE
    try:
        with open(path, mode="w") as file:
            file.write(contents)
            print("New file content: \n" + file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file.")

def afc(path, appendents):    #DONE
    with open(path, mode="w") as file:
        #Edit here
        contents = file.read()
        choice = input("Add a new line: (Y/n)")
        if choice.lower().strip() == "y":
            newline = True
        elif choice.lower().strip() == "n":
            newline = False
        else:
            raise ConnectionRefusedError
        if newline:
            new_content = contents + "\n" + appendents
        elif not newline:
            new_content = contents, appendents
        else:
            pass
        #SEPERATOR
        file.write(new_content)
        print(("New file content:\n" + file.read()))

def csmcmd(cmd):    #DONE
    os.system(cmd)
    history.append(cmd)

def rb(path): #DONE
    try:
        with open(path, mode="rb") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file!")

def wb(path, content):  #DONE
    with open(path, mode="wb") as file:
        if input("Are you sure you want to write binary? This mode is only for devolopers! (Yes) You should provide strings, not bytes.") == "Yes":
            try:
                with open(path, mode="wb") as file:
                    file.write(content.encode(encoding='utf-8)'))
            except FileNotFoundError:
                print("File not found.")
            else:
                print("Cannot access file!")

def rename(target, name):   #DONE
    if name and target:
        os.system(f"mv {target} {name}")

def move_file(path, target_path):     #DONE
    if path and target_path:
        os.system(f"mv {path} {target_path}/")

def sigfile(path):      #DONE
    if input("This command only works for Macintosh and Linux users, are you sure you want to continue? (Yes)").lower().strip() == "yes":
        os.system("chmod +x " + path)

def winlog():    #DONE
    os.system("dir")

def exi():   #DONE
    exit("Program exited with a value of 0.", 0)

def scan(path):    #DONE
    if os.path.exists(path):
        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
    else:
        print("Path doesn't exists!")

def find_file_core(filename, search_path):   #DONE
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def find_file_entry(name, path):    #DONE
    search_path = path
    filename = name

    file_path = find_file_core(filename, search_path)
    if file_path:
        print(f"File found at: {file_path}")
    else:
        print("File not found.")
    
def find_directory_core(dirname, search_path):     #DONE
    for root, dirs, files in os.walk(search_path):
        if dirname in dirs:
            return os.path.join(root, dirname)
    return None

def find_directory_entry(path, dir):     #DONE
    search_path = path
    dirname = dir

    dir_path = find_directory_core(dirname, search_path)
    if dir_path:
        print(f"Directory found at: {dir_path}")
    else:
        print("Directory not found.")

def websurf(link, browser=None):    #DONE
    if browser == None:
        webbrowser.open(link)
        print("Make sure that you at least have a default broswer installed, and added to PATH.")
    else:
        webbrowser.get(browser).open(link)   
        print("Make sure that you at least have a default broswer installed, and added to PATH.")

def clear_console():    #DONE
    os.system("cls")

def clear_bash():   #DONE
    os.system("clear")

def msg():   #CACHED
    print("This function is not avaliable for NONE UNIX users.")
    
def warning():     #CACHED
    if platform.system() == 'Windows':
        return False
    else:
        return True
#APTS
def update_pkg_lists():   #DONE
    if warning():
        print("Asking for sudo access, which may requires your password.")
        os.system("sudo apt update")
    else:
        msg()

def i_installer(pkg):    
    if warning():
        print("Asking for sudo access, which may requires your password.")
        os.system("sudo apt install " + pkg.strip())
    else:
        msg()

def i_uninstaller(pkg):
    if warning():
        print("Asking for sudo access, which may requires your password.")
        os.system("sudo apt remove " + pkg.strip())
    else:
        msg()

def upgrade_pkgs():
    if warning():
        print("Asking for sudo access, which may requires your password.")
        os.system("sudo apt upgrade")
    else:
        msg()

def search_pkg(pkg):
    if warning():
        os.system("apt search " + pkg.strip())
    else:
        msg()

def show_details(pkg):
    if warning():
        os.system("apt show " + pkg.strip())
    else:
        msg()

def cleanup():
    if warning():
        print("Asking for sudo access, which may requires your password.")
        print("Cleaning up packages. This might take a few minutes", end="")
        for i in "......":
            print(i)
            time.sleep(0.5)
        os.system("clear")
        os.system("sudo apt clean")
        os.system("clear")
        print("Waiting to be finished...")
        time.sleep(1)
        for i in tqdm(range(100)):
            time.sleep(0.1)
    else:
        msg()
#APTS

def brew_installer():
    if warning():
        print("Installing Homebrew. The missing package installer.")
        os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'")
        os.system("clear")
        print("Exporting to PATH.")
        time.sleep(1)
        os.system("export PATH='/home/linuxbrew/.linuxbrew/bin:$PATH'")
        print("Reloading Bash 80*24")
        time.sleep(1.5)
        os.system("source ~/.bashrc")
        print("Successfully installed homebrew: " + os.system("brew --version"))
    else:
        msg()
#Compiler
def cmake():
    if platform.system() == "Windows":
        webbrowser.open("https://cmake.org/download/")
    elif platform.system() == "Darwin":
        if input("A better option to install this is using wget. Are you sure you installed Homebrew? (Yes) ").strip().lower() == "yes":
             os.system("brew install wget")
             os.system("wget https://github.com/Kitware/CMake/releases/download/v3.30.2/cmake-3.30.2-macos-universal.dmg")
        else:
            webbrowser.open("https://cmake.org/download")
    elif platform.system() == "Linux":
        i_installer("wget")
        os.system("wget --version")
        os.system("wget https://github.com/Kitware/CMake/releases/download/v3.30.2/cmake-3.30.2-linux-x86_64.sh")
        print("Assuming you are using x86-x64.")
    else:
        print("You are not on a supported platform, program aborted.")
        
def tscnt(url, max):
    if warning():
        if platform.system() == "Darwin":
            os.system(f"curl -I --max-time {max} {url}")
        elif platform.system() == "Linux":
            i_installer("curl")
            os.system(f"curl -I --max-time {max} {url}")
        else:
            print("Platform not supported. Program aborted.")
    else:
        print("Platform not avaliable.")

def default():
    print("Command doesn't exist.")

def check_empty(string):
    if string == "":
        return True
    else:
        return False

def record():
    print(history)

while True:
    bash_prompt = input(">")
    history.append(bash_prompt)
    if bash_prompt.lower().strip() == "delete":
        history.append("Delete")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            delete(path=path)
    #SEP
    elif bash_prompt.lower().strip() == "remove directory":
        history.append("Remove Directory")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            rmdir(path=path)
    #SEP
    elif bash_prompt.lower().strip() == "set location":
        history.append("Set Location")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            opendir(dir=path)
    #SEP
    elif bash_prompt.lower().strip() == "list content unix":
        history.append("List Content (Unix)")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            lis(dir=path)
    #SEP
    elif bash_prompt.lower().strip() == "create directory":
        history.append("Create Directory")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            makedir(dirname=path)
    #SEP
    elif bash_prompt.lower().strip() == "read docs":
        history.append("Read Docs")
        history.append(input("Argument: "))
        path = history[len(history)-1]
        if not check_empty(string=path):
            read(path=path)
    #SEP
    elif bash_prompt.lower().strip() == "write files":
        history.append("Write Files")
        history.append(input("File path: "))
        file = history[len(history)-1]
        history.append(input("New content: "))
        newcontent = history[len(history)-1]
        wrt(path=file, contents=newcontent)
    #SEP
    elif bash_prompt.lower().strip() == "append information to file":
        history.append("Append Information to File")
        history.append(input("File path: "))
        file = history[len(history)-1]
        history.append(input("Appendents: "))
        appendent = history[len(history)-1]
        afc(path=file, appendents=appendent)
    #SEP
    elif bash_prompt.lower().strip() == "custom command":
        history.append("Custom Command")
        csmcmd(cmd=input("Argument: "))
    #SEP
    elif bash_prompt.lower().strip() == "read binary":
        history.append("Read Binary")
        path = input("Argument: ")
        history.append(path)
        rb(path=path)
    #SEP
    elif bash_prompt.lower().strip() == "write binary":
        history.append("Write Binary")
        history.append(input("File path: "))
        file = history[len(history)-1]
        history.append(input("New content: "))
        newcontent = history[len(history)-1]
        wb(path=file, content=newcontent)
    #SEP
    elif bash_prompt.lower().strip() == "rename":
        history.append("Renaming")
        path = input("File path: ")
        history.append(path)
        new_name = input("New name: ")
        history.append(new_name)
        rename(target=path, name=new_name)
    #SEP
    elif bash_prompt.lower().strip() == "move items":
        history.append("Move Files or Directories")
        path = input("File path: ")
        history.append(path)
        directory = input("Directory: ")
        history.append(dir)
        move_file(path=path, target_path=directory)
    #SEP
    elif bash_prompt.lower().strip() == "sign files":
        history.append("Sign Files")
        history.append(input("Agument: "))
        path = history[len(history)-1]
        sigfile(path=path)
    #SEP
    elif bash_prompt.lower().strip() == "list windows":
        history.append("List Windows Directory")
        winlog()
    #SEP
    elif bash_prompt.lower().strip() == "exit":
        history.append("Key Exiting")
        exi()
    #SEP
    elif bash_prompt.lower().strip() == "scan directory":
        history.append("Scan Directory")
        history.append(input("Argument: "))
        directory = history[len(history)-1]
        scan(path=directory)
    #SEP
    elif bash_prompt.lower().strip() == "find_file":
        directory = input("Directory you are searching for: ")
        filename = input("File Name: ")
        history.append("Find File")
        a = (directory, filename)
        for i in a:
            history.append(i)
        find_file_entry(name=filename, path=directory)
    #SEP
    elif bash_prompt.lower().strip() == "find directory":
        history.append("Find Directory")
        directory = input("Directory you are searching for: ")
        dirname = input("Directory name: ")
        a = (directory, dirname)
        for i in a:
            history.append(i)
        find_directory_entry(path=directory, dir=dirname)
    #SEP
    elif bash_prompt.lower().strip() == "surf web":
        history.append("Web Surf")
        url = input("Url: ")
        browser = input("Browser (Optional): ")
        for i in (url, browser):
            history.append(i)
        if browser == "":
            websurf(link=url)
        else:
            websurf(link=url, browser=browser)
    #SEP
    elif bash_prompt.lower().strip() == "clear windows terminal":
        history.append("clear windows terminal".capitalize())
        clear_console()
    #SEP
    elif bash_prompt.lower().strip() == "clear bash":
        history.append("clear bash".capitalize())
        clear_bash()
    #SEP
    elif bash_prompt.lower().strip() == "update apt lists":
        history.append("Update Package Lists")     
        update_pkg_lists()
    #SEP
    elif bash_prompt.lower().strip() == "install apt package":
        history.append("Install APT Package")
        history.append("")
    else:
        default()