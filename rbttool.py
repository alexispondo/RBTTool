"""
Coded By Alexis Pondo
Github: http://github.com/alexispondo/
Linkedin: https://www.linkedin.com/in/alexis-pondo/
"""
from datetime import datetime
import os
from pathlib import Path
import tempfile
import itertools as IT
import hashlib
import platform


Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Bold_Green = "\u001b[1;92m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"

Underline = "\u001b[4m"

OS_platform = platform.system()
#################################################################################################################################################################
####################### Somme importante function
#################################################################################################################################################################


# For clean terminal
def clear_term():
    if OS_platform != "Windows":
        os.system("clear") # On Unix
    else:
        os.system("cls") # On windows
#################################################################################################################################################################

def our_input(mess):
    if OS_platform != "Windows": # On Unix
        from prompt_toolkit import prompt
        r = prompt(mess)
        return r
    else: # On windows
        r = input(mess)
        return r

# Get file encoging
def get_encoding(file):
    try:
        import magic
        return magic.Magic(mime_encoding=True).from_file(file)
    except:
        print("encoding not found for "+ file)
        print("We will use utf-8")
        return "utf-8" # By default
#################################################################################################################################################################


# Get filename only
def get_basename(path):
    if OS_platform != "Windows":
        file_name_base = path.split("/")[-1] # On linux
    else:
        file_name_base = path.split("\\")[-1] # On windows
    return file_name_base
#################################################################################################################################################################


# For not erase existing file
# If rainbow table exist already with the same name it will create another file with incremental number
def uniquify(path, sep = '-'):
    def name_sequence():
        count = IT.count()
        yield ''
        while True:
            yield '{s}{n:d}'.format(s = sep, n = next(count))
    orig = tempfile._name_sequence
    with tempfile._once_lock:
        tempfile._name_sequence = name_sequence()
        path = os.path.normpath(path)
        dirname, basename = os.path.split(path)
        filename, ext = os.path.splitext(basename)
        fd, filename = tempfile.mkstemp(dir = dirname, prefix = filename, suffix = ext)
        tempfile._name_sequence = orig
    return filename
#################################################################################################################################################################

# Display banner
def banner(message = "RainBowTable Tool [RBTTool]"):
    infos = """
[+] Author: @alexispondo
[+] Name: RBTTool
[+] Version: 1.0
[+] Github: https://github.com/alexispondo/
[+] Linkedin: https://www.linkedin.com/in/alexis-pondo/
"""

    ban1 = infos+"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _______     | || |   ______     | || |  _________   | || |  _________   | || |     ____     | || |     ____     | || |   _____      | |
| | |_   __ \    | || |  |_   _ \    | || | |  _   _  |  | || | |  _   _  |  | || |   .'    `.   | || |   .'    `.   | || |  |_   _|     | |
| |   | |__) |   | || |    | |_) |   | || | |_/ | | \_|  | || | |_/ | | \_|  | || |  /  .--.  \  | || |  /  .--.  \  | || |    | |       | |
| |   |  __ /    | || |    |  __'.   | || |     | |      | || |     | |      | || |  | |    | |  | || |  | |    | |  | || |    | |   _   | |
| |  _| |  \ \_  | || |   _| |__) |  | || |    _| |_     | || |    _| |_     | || |  \  `--'  /  | || |  \  `--'  /  | || |   _| |__/ |  | |
| | |____| |___| | || |  |_______/   | || |   |_____|    | || |   |_____|    | || |   `.____.'   | || |   `.____.'   | || |  |________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""+message+"""
"""


    ban2= """
   ▄████████ ▀█████████▄      ███         ███      ▄██████▄   ▄██████▄   ▄█       
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄ ███    ███ ███    ███ ███       
  ███    ███   ███    ███    ▀███▀▀██    ▀███▀▀██ ███    ███ ███    ███ ███       
 ▄███▄▄▄▄██▀  ▄███▄▄▄██▀      ███   ▀     ███   ▀ ███    ███ ███    ███ ███       
▀▀███▀▀▀▀▀   ▀▀███▀▀▀██▄      ███         ███     ███    ███ ███    ███ ███       
▀███████████   ███    ██▄     ███         ███     ███    ███ ███    ███ ███       
  ███    ███   ███    ███     ███         ███     ███    ███ ███    ███ ███▌    ▄ 
  ███    ███ ▄█████████▀     ▄████▀      ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ 
  ███    ███                                                            ▀         
                                                                                  
"""

    ban3 = """
    ██████╗ ██████╗ ████████╗████████╗ ██████╗  ██████╗ ██╗     
    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██████╔╝██████╔╝   ██║      ██║   ██║   ██║██║   ██║██║     
    ██╔══██╗██╔══██╗   ██║      ██║   ██║   ██║██║   ██║██║     
    ██║  ██║██████╔╝   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═╝  ╚═╝╚═════╝    ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

    """

    ban = [ban1, ban2, ban3]
    return ban
#################################################################################################################################################################





#################################################################################################################################################################
################## Functions used
#################################################################################################################################################################


## Create Rainbow table from Dictionary #########################################################################################################################
#################################################################################################################################################################

# Choice hash algorithm
def choice_hash():
    out = False # We initialize Out at False
    while not out:
        print("""Select your hash algorithm
1= md4                 7= sha384                  13= sha3_384               19= whirlpool
2= md5                 8= sha512                  14= sha3_512
3= md5-sha1            9= sha512_224              15= blake2b
4= sha1                10= sha512_256             16= blake2s
5= sha224              11= sha3_224               17= sm3
6= sha256              12= sha3_256               18= ripemd160

99= return
""")
        print("\nIf you want to choice multiple algorithm you can do this by separating number with space. \n"
              "ex: >>> 1 2 3 (For choice md4, md5 and md5-sha1)\n"
              "If you want to choose all algorithm you should enter \"all\"\n"
              "ex: all (For choice all algorithm)")
        hash0 = our_input(">>> ") # We enter our hashs chooses


        if hash0 == "all": # If we want all algorithm
            list_hash = [str(i) for i in range(1,20)] # Take all algorithm
        else: # Else
            list_hash = hash0.split(" ") # We change our chooses in list. ex: 1 2 3 will be ["1", "2", "3"]
        if list_hash != ["99"]: # If we have not choose return
            for hash in list_hash: # For each items
                try:
                    if int(hash) in range(1,20): # We check if it is int and if it is in our list of choice
                        out = True # We can continue
                    else: # Else
                        clear_term() # We clean terminal
                        print(Red+"Your entered is incorrect !"+Cyan)
                        out = False # We should choose again
                        break
                except: # If something is wrong
                    clear_term() # We clean terminal
                    print(Red + "Your entered is incorrect !" + Cyan)
                    out = False # We should choose again
                    break
        else: # If we have chosen return
            out = True # We continue
    return list_hash # We return list of hash
#################################################################################################################################################################


# Select dictionary
def choice_dictionary_file():
    file_exist = False # We initialize at False
    while not file_exist:
        print("entrer the full path of your dictionary ex: /home/user/my/dict.txt")
        dict_path = our_input(">>> ") # Enter dictionary file
        if Path(dict_path).is_file(): # Check if file exist
            return dict_path # return it
        else:
            print(Red+"This file not found (Enter correct path of file)"+Cyan) # Try again
#################################################################################################################################################################


# function to hash dictionary with the list of hash algo
# It takes in argument list of algo and dictionary path
def hash_dictionary(list_algo, dict_path):
    encoding = get_encoding(dict_path) # Get encoding
    with open(dict_path, "r", encoding=encoding, errors='ignore') as dict_base: # We open Dictionary file
        passwords = dict_base.readlines() # We read all lines il the list passwords
        file_name_base = get_basename(dict_path)  # we take basename of dictionary
        current_dir = os.getcwd() # We get current directory
        rbt_list_dir = current_dir + "/rainbow_tables_lists" # We add directory of rainbow tables list
        if not os.path.exists(rbt_list_dir): # We check if directory exist
            os.mkdir(rbt_list_dir) # Else we create it

        start_time = str(datetime.now()).split(".")[0] # Start time
        print(Red+"\n\n"+start_time+": Starting..."+Cyan)
        algo_num = 0 # we initialize algo number at 0
        for algo_hash in list_algo: # we take each algo of the list algo
            algo_num = algo_num + 1 # we increment algo number of 1
            print("\n[*] Start creation of "+algo_hash+" rainbow table: ["+str(algo_num)+"/"+str(len(list_algo))+"]:\n==> ", end="")
            end_file_name = rbt_list_dir+"/rbt_"+algo_hash+"_"+file_name_base # We create output filename
            end_file_name = uniquify(end_file_name) # We check if this filename is not exist. If it exists we will increment it
            with open(end_file_name, "w", encoding=encoding) as dict_rbt: # We create new file for algo
                i = 0 # We initialize password number at 0
                for passw in passwords: # For each password in passwords list
                    passwd = passw.split("\n")[0] # take only password without "\n"
                    passwd_hash = hashlib.new(algo_hash, passwd.encode()).hexdigest() # Hash it with algo hash and password encoded in bytes and return hex value
                    line = passwd_hash + "\t\t" + passwd + "\n" # Create a new line for the new file
                    dict_rbt.writelines(line) # Add this line in the rainbow table file

            print("The Rainbow Table Output for "+ Magenta+algo_hash+Cyan+ " algorithm can be found in: "+ Magenta+ end_file_name+ Cyan)
        end_time = str(datetime.now()).split(".")[0] # End Time
        print(Red+"\n"+end_time + ": End"+Cyan)
    input("\n\nTap Enter to finish: ") # Wait Enter to continue
#################################################################################################################################################################

# Main function to create rainbow tables
def create_rbt():
    print(Cyan+banner()[1])
    hash_algorithm = {
        "1": "md4",
        "2": "md5",
        "3": "md5-sha1",
        "4": "sha1",
        "5": "sha224",
        "6": "sha256",
        "7": "sha384",
        "8": "sha512",
        "9": "sha512_224",
        "10": "sha512_256",
        "11": "sha3_224",
        "12": "sha3_256",
        "13": "sha3_384",
        "14": "sha3_512",
        "15": "blake2b",
        "16": "blake2s",
        "17": "sm3",
        "18": "ripemd160",
        "19": "whirlpool",

        # "20": "shake_128", # Work with length
        # "21": "shake_256", # Work with length
        # "22": "mdc2", # Don't work
    } # dictionary of hash (hash available in hashlib) common used
    print("Great!\nCreate your own RainbowTable from your custom dictionary\n")
    list_hash = choice_hash()  # Choose list of hash algorithm
    if list_hash == ["99"]:  # If return is selected
        return ""
    else:
        algo = []  # Initialize Algorithm
        for num in list_hash: # For each item
            hash = hash_algorithm[num] # Select algorithm corresponding at the hash number in the hashs dictionary
            algo.append(hash) # Append hash
    dict_path = choice_dictionary_file() # Chose dictionary file
    print(Yellow+"""
We will apply """+Underline+", ".join(algo)+Reset+Yellow+""" algorithms in the """+Underline+get_basename(dict_path)+Reset+Yellow+""" dictionary to get our rainbow table.
"""+Green+"""[+]"""+Yellow+"""Hash Algorithm: """+", ".join(algo)+"""
"""+Green+"""[+]"""+Yellow+"""Dictionary Path: """+dict_path+"""
"""+Cyan)
    print("Do you want to continue ?")
    continu = our_input("(yes or  y / no or n)>>> ") # Continue ?
    while continu.lower() not in ["y", "n", "yes", "no"]:
        print("Do you want to continue ?")
        continu = our_input("(yes or y / no or n)>>> ")
    if continu.lower() in ["y", "yes"]: # If yes
        hash_dictionary(algo, dict_path) # We can start creation of rainbow table by dictionary and hash list
#################################################################################################################################################################





## Crack hash from Rainbow table ################################################################################################################################
#################################################################################################################################################################

# Select file contain hases
def select_hash_file():
    out = False
    while not out:
        print(Cyan + banner()[2])
        print("Crack your hashs password with rainbow tables")
        print("To crack hash password you must generate rainbow table firstly")
        print("If your are not rainbow tables corresponding to your hash fonction you should create it to crack password")
        print("If you want to know what is your hash")
        print("To generate rainbow table you should give your dictionary file in argument of the option 1 \n" + Magenta + "\"1- Create Rainbow Table from dictionary\"" + Cyan + " of home page")
        print("\nEnter your hash file\n")
        hash_file = our_input(">>> ")
        if Path(hash_file).is_file(): # Check if file exist
            return hash_file # return it
        else:
            clear_term()
            print(Red+"This file not found (Enter correct path of file)"+Cyan) # Try again
#################################################################################################################################################################


# Select list of rainbow table that we want use
def select_rainbow_tables_lists():
    error = True
    while error:
        print(Cyan+"\nSelect your rainbow table")
        print("You can select multiple rainbow table by separate with space. If you want to select other table you can enter full path of this")
        print("ex: >>> 1 2 /home/user/rbt/rbt1.txt 5 (This exemple well choice rainbow table 1, 2, 5 in the display rainbow table list and other rainbow table locate at \"/home/user/rbt/rbt1.txt\")")
        print("Also you can enter \"all\" to select all rainbow table display in list")

        rainbow_tables_dir = os.getcwd() + "/rainbow_tables_lists/" # dir of rainbow_tables_lists

        if not os.path.exists(rainbow_tables_dir):
            os.mkdir(rainbow_tables_dir)

        for (current_dir, list_dir, files) in os.walk(rainbow_tables_dir):
            file = sorted(files) # get all rainbow table in dir rainbow_tables_lists


        print("\nList of rainbow table")
        if len(file) == 0: # If this directory is empty
            print(Red+"\t\t\tNo Rainbow Table in directory rainbow_tables_lists :("+Cyan)
            print("\n")
        else: # else
            i = 0
            print(White)
            rainbow_tables_list_file = [] # list of rainbow tables initialized
            for r in file: # we list rainbow table found in the dir rainbow_tables_lists
                i = i + 1
                rainbow_tables_list_file.append(str(rainbow_tables_dir + r)) # We append full name of the rainbow table
                print("  "+str(i) + "= "+ str(rainbow_tables_dir + r))
            print(Cyan+"\n")

        rbt_choice = our_input(">>> ") # We do our choice
        rbt_choice = rbt_choice.split(" ") # We trasform it in list contain number, "all", and/or other path
        rbt_list = [] # Initialization of real list with all full path of rainbow table
        for rbt_c in rbt_choice:
            try:
                if rbt_c == "all": # If we want all algorithm
                    for i in rainbow_tables_list_file:
                        rbt_list.append(i)
                        error = False
                else: # Else
                    try:
                        if int(rbt_c) > 0 and int(rbt_c) <= len(rainbow_tables_list_file): # if correct number is entered
                            r = rainbow_tables_list_file[int(rbt_c)-1] # We choose equivalent rainbow table in function of number
                            rbt_list.append(r) # We add append it in real list with all full path of rainbow table
                            error = False
                        else: # Wrong number
                            error = True
                            clear_term()
                            print(Red+"Your input is incorrect.."+Cyan)
                    except: # If other full path is entered
                        if Path(rbt_c).exists() and rbt_c != "": # If path exist
                            rbt_list.append(rbt_c) # we append it
                            error = False
                        else: # Else
                            error = True
                            clear_term()
                            print(Red+"Your input is incorrect.."+Cyan)
            except: # Something is wrong
                error = True
                clear_term()
                print(Red+"Something is Wrong..."+Cyan)
    return rbt_list # We return list of hash
#################################################################################################################################################################


def cracking(hash_file, rainbow_tables_lists):
    encoding = get_encoding(hash_file) # We get encoding of file
    with open(hash_file, "r", encoding=encoding, errors="ignore") as hash_f:
        hashes = [i.split("\n")[0].lower() for i in hash_f.readlines()] # we get all hashes contains in file
        end = False
        #print(hashes)
    #print(rainbow_tables_lists)
    num_rbt = 0 # We initialize number of rainbow table at 0
    len_rbtl = len(rainbow_tables_lists) # size of rainbow table
    print("\nCracking Started...")
    founded = os.getcwd() + "/cracked_" + get_basename(hash_file) # Output of found password
    with open(founded, "w", encoding="utf-8") as fou:
        for rbtl in rainbow_tables_lists: # For each rainbow tables
            num_rbt = num_rbt + 1 # We increment of 1 number of rainbow table
            print("\n"+"["+str(num_rbt)+"/"+str(len_rbtl)+"] "+rbtl)
            encoding2 = get_encoding(rbtl) # We get encoding of rainbow table
            with open(rbtl, "r", encoding=encoding2, errors="ignore") as rbt_f: # We open it in reading mode
                print("[*] Loading ", end="")
                rbt_l = rbt_f.readlines()
                print(Green+"OK"+Cyan)
                start_time = str(datetime.now()).split(".")[0] # Start time
                print("[*] Starting: " + start_time)
                for rbt in rbt_l: # For each line of rainbow table
                    for hash in hashes: # for each hash of list of hashes
                        if hash == rbt.split("\n")[0].split("\t\t")[0]: # if hash is found
                            password = "\t\t".join(rbt.split("\n")[0].split("\t\t")[1:]) # we get password
                            print(Bold_Green+"Found: " + Green + hash + Cyan + "\t<<==>>\t" + Green + password + Cyan)
                            fou.write(hash+"\t\t"+password+"\n") # we add it in hash founded file
                            hashes.remove(hash) # We remove it in list of hashes
                    if len(hashes) == 0: # Is all hashes are founded
                        end = True
                        break
                end_time = str(datetime.now()).split(".")[0] # End time
                print("End: " + end_time)
                if end:
                    break
        print("\nYou can found file cracked output in: " + Blue + Underline + founded + Reset + Cyan)
        if len(hashes) != 0: # If some hashes are not founded
            print(Red+"\n[x] Hash not Found\n"+Cyan)
            for k in hashes: # We list them
                print(Red+"[-] " + Cyan + k)
    print()
    input("Tap Enter to Finish: ")
#################################################################################################################################################################


# Main function of crack option
def crack_hash():
    out = False # We initialize Out at False
    while not out:
        print(Cyan + banner()[2]) # Print Banner
        print("Crack your hashs password with rainbow tables")
        print("To crack hash password you must generate rainbow table firstly")
        print("If your are not rainbow tables corresponding to your hash fonction you should create it to crack password")
        print("To generate rainbow table you should give your dictionary file in argument of the option 1 \n" + Magenta + "\"1- Create Rainbow Table from dictionary\"" + Cyan + " of home page")
        print("\nif you are ready :) let's go !!!")
        print("\n1- continue\n99- return")
        choix = our_input(">>> ") # Select if we want to continue or return
        try:
            if int(choix) == 1: # Continue
                clear_term()
                out = True
            elif int(choix) == 99: # Return
                return ""
            else: # Bad Enter
                clear_term()
                out = False
        except: # Something is wrong
            clear_term()
            out = False
    hash_file = select_hash_file() # We get hashes file chose
    rainbow_tables_lists = select_rainbow_tables_lists() # We get rainbow tables chooses
    print("\nGreat, it's already done :)")
    print(Yellow)
    print("=========================================================================================================")
    print("================================================ Summary ================================================")
    print("= [*] Your Hashes passwords files")
    print("= \t"+hash_file)

    print("= [*] Yours Rainbow Table lists:")
    for i in rainbow_tables_lists:
        print("= \t"+i)
    print("=========================================================================================================")
    print("=========================================================================================================")
    print(Cyan)
    ok = False
    while not ok:
        print("\n1- Start cracking\n99- Abort")
        choix = our_input(">>> ") # Ask if we want to start cracking
        if choix == "1":
            ok = True
        elif choix == "99":
            return ""
        else:
            print(Red+"Your input is invalid"+Cyan)
            ok = False
    cracking(hash_file, rainbow_tables_lists) # We start cracking




#################################################################################################################################################################
################## Main program
#################################################################################################################################################################
def main():
    ban = banner()[0] # Display Banner
    clear_term()
    print(Cyan+ban)
    print("""
1- Create Rainbow Table from dictionary
2- Crack Hash by Rainbow Table
99- Exit""")
    choix = our_input(">>> ") # Select Option
    while choix != "99": # While we not select exit
        clear_term()
        if choix == "1": # If we select create dictionary
            create_rbt() # Create dictionary
        elif choix == "2": # Else if we select Cracke Hash password
            crack_hash() # Crack hash  password

        clear_term()
        print(Cyan+ban)
        print("""
1- Create Rainbow Table from dictionary
2- Crack Hash by Rainbow Table
99- Exit""")
        choix = our_input(">>> ")

main()