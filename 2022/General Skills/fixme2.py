armstizzy-picoctf@webshell:~$ https://artifacts.picoctf.net/c/67/fixme2.py
-bash: https://artifacts.picoctf.net/c/67/fixme2.py: No such file or directory
armstizzy-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/67/fixme2.py
--2023-03-08 19:59:08--  https://artifacts.picoctf.net/c/67/fixme2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.156.172.6, 108.156.172.120, 108.156.172.74, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.156.172.6|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1029 (1.0K) [application/octet-stream]
Saving to: 'fixme2.py'

fixme2.py                                                           100%[=================================================================================================================================================================>]   1.00K  --.-KB/s    in 0s      

2023-03-08 19:59:08 (63.7 MB/s) - 'fixme2.py' saved [1029/1029]

armstizzy-picoctf@webshell:~$ python3 fixme2.py
  File "/home/armstizzy-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
armstizzy-picoctf@webshell:~$ nano fixme2.py 
armstizzy-picoctf@webshell:~$ python3 fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
