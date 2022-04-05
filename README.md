# TUTORIAL

Click on the video to see the tutorial:

[![How to use RBTTool ](https://user-images.githubusercontent.com/47490330/160831652-4f1b6632-cc48-4a16-92bb-b2a1e6593291.png)](https://youtu.be/e1rXlWEw6yw?t=1s "How to use RBTTool ")

# DESCRIPTION

RBTTool is a password cracking tool based on the principle of rainbow table
- It can generate him own rainbow table that it use for cracking hashes.
- It can crack 19 types of hashes.
- It can crack password in using multiple rainbow table to expanse chance to found correct password.
- It work on windows, linux and other
# USAGE

- Step 1: Installation

**Download the tool**
```
$ git clone https://github.com/alexispondo/RBTTool.git
```

**Starting the tool**
```
$ cd RBTTool
$ python installer.py
$ python rbttool.py
```

- Step 2: Found your hash algorithm

Suppose you have a hash, and you want to find the resulting password.
You will first need to find the hash algorithm used to hash the password.
This step is not required, but it may make it easier to crack.
To find it you can use hash-identifier or https://gchq.github.io/CyberChef/#recipe=Analyse_hash() online hash-identifier

- Step 3: Create your dictionary

You should create dictionary/wordlist if you have not yet or if you want to personalize.
You can also download wordlists online or use wordlists in linux located in /usr/share/wordlists/

- Step 4: Create your rainbow table

For do it:

**1- Start the tool**
```
$ python rbttool.py
```
**2- Select option 1 (Create Rainbow Table from dictionary)**
```
>>> 1
```
**3- Select your hashes algorithms**

For do it you are multiple solution, if you know what algorithm is used to hash the password your can enter him letter corresponding at this algorithm. (for exemple if your algorithm is md5) you can enter 2

In this case enter
```
>>> 2
```
If you are some idea about this algorithm (for example if hash algorithm can be sha512 or whirlpool) you can choose them by separating with space.

In this case enter
```
>>> 8 19
```

And if you are not idea about algorithm used you can use all algorithm to generate your rainbow table

In this case enter
```
>>> all
```

**4- Enter your wordlist that you want used**

Here you can enter full path of your wordlist or just the name if you are in same directory with him. For exemple if wordlist that i want to found is rockyou.txt:
```
>>> /usr/share/wordlists/rockyou.txt
```

**5- Enter yes to start generating**
```
>>> yes
```
You can found output of generating in the directory **rainbow_tables_lists**

- Step 5: Crack your hash with rainbow table

You should save your hashes that you want to crack in file, you can enter unlimited.
for exemple:
we want to crack:

fb1fc235f6ad5de7ead77c0cab33d2365c324fd5

ee8d8728f435fd550f83852aabab5234ce1da528

5f4dcc3b5aa765d61d8327deb882cf99

So we save these hashes in file name hashes.txt
After verification we know that the both first hashes is hashed by sha1 and the last is md5. If we have already generate rainbow table in this algorithm we can start.

**1- launch tool**
```
$ python rbttool.py
```
**2- Select option 2 (Crack Hash by Rainbow Table)**
```
>>> 2
```
**3- Select Continue**

```
>>> 1
```

**4- Enter your hash file**

For exemple: 
```
>>> /home/username/RBTTool/hashes.txt
```

**5- Select your rainbow tables that you want to use**

here again you can choose multiple rainbow table

For exemple:
```
>>> 1 2 3
```
You can choose all rainbow table
```
>>> all
```

You can also enter specific rainbow table
```
>>> 1 2 /home/username/Path/Of/Other/Rainbow_table
```

**6- Start cracking**

```
>>> 1
```

After this we can check output file cracked_hashes.txt to view our hash cracked


# Additional

All information about this code can be found in the comments of the code.
Please contact me for any bug or anomaly detected in connection with this tool:

Linkedin: https://www.linkedin.com/in/alexis-pondo/

GitHub: https://github.com/alexispondo/

RBTTool: https://github.com/alexispondo/RBTTool
