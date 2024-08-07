import os
import webbrowser

history = list()

def delete(path):
    os.remove(path)

def rmdir(path):
    os.removedirs(path)

def opendir(dir):
    os.system("cd " + path)

def list(dir):
    os.system("ls")

def makedir(dirname):
    os.system("mkdir " + dirname)

def read(path):
    try:
        with open(path, mode="r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file.")

def wrt(path, contents):
    try:
        with open(path, mode="w") as file:
            file.write(contents)
            print("New file content: \n" + file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file.")

def afc(path, appendents):
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

def ctmcmd(cmd):
    os.system(cmd)

def rb(path):
    try:
        with open(path, mode="rb") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Cannot access file!")

def wb(path, content):
    with open(path, mode="wb") as file:
        if input("Are you sure you want to write binary? This mode is only for devolopers! (Yes) You should provide strings, not bytes.") == "Yes":
            try:
                with open(path, mode="wb") as file:
                    file.write(content.encode(encoding='utf-8)'))
            except FileNotFoundError:
                print("File not found.")
            else:
                print("Cannot access file!")

def rename(target, name):
    if name and target:
        os.system(f"mv {target} {name}")

def move_file(path, target_path):
    if path and target_path:
        os.system(f"mv {path} target_path/")

def sig(path):
    if input("This commad only works for Macintosh and Linux users, are you sure you want to continue? (Yes)").lower().strip() == "yes":
        os.system("chmod +x " + path)
def winlog():
    os.system("dir")

def exit():
    exit("Program exited with a value of 0.", 0)

def scan(path):
    if os.path.exists(path):
        with os.scandir(path) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
    else:
        print("Paths doesn't exists!")

def find_file_core(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def find_file_entry(name, path):
    search_path = path
    filename = name

    file_path = find_file_core(filename, search_path)
    if file_path:
        print(f"File found at: {file_path}")
    else:
        print("File not found.")
    
def find_directory_core(dirname, search_path):
    for root, dirs, files in os.walk(search_path):
        if dirname in dirs:
            return os.path.join(root, dirname)
    return None

def find_directory_entry(path, dir):
    search_path = path
    dirname = dir

    dir_path = find_directory(dirname, search_path)
    if dir_path:
        print(f"Directory found at: {dir_path}")
    else:
        print("Directory not found.")

def websurf(link, browser=None):
    if browser == None:
        webbrowser.open(link)
        print("Make sure that you at least have a default broswer installed, and added to PATH.")
    else:
        webbrowser.get(browser).open(link)
        print("Make sure that you at least have a default broswer installed, and added to PATH.")

def clear_console():
    os.system("cls")

def clear_bash():
    os.system("clear")

class apt:
    def __init___(self)
