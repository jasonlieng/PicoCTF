![image](https://user-images.githubusercontent.com/110505489/223917817-269b51ba-472d-4695-8d6e-17d086144582.png)

Received a lot of 
SyntaxError: 'return' outside function
armstizzy-picoctf@webshell:~$ nano level3.py
armstizzy-picoctf@webshell:~$ python3 level3.py
  File "/home/armstizzy-picoctf/level3.py", line 35
    return
    
Problem was that:

user_pw = input
user_pw_hash = hash_pw(user_pw)

was interfering with the return function and the for loop, so once it was gone the code worked.
