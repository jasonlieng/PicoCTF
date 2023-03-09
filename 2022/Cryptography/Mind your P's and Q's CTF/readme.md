Given: In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

armstizzy-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values
--2023-03-09 06:07:19--  https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 205 [application/octet-stream]
Saving to: 'values'

values                                                              100%[=================================================================================================================================================================>]     205  --.-KB/s    in 0s      

2023-03-09 06:07:19 (73.6 MB/s) - 'values' saved [205/205]

armstizzy-picoctf@webshell:~$ cat values
Decrypt my super sick RSA:
c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e: 65537

![image](https://user-images.githubusercontent.com/110505489/223935307-82f8b25f-788b-4b10-a5c4-ae2b5dac5296.png)

Flag: picoCTF{sma11_N_n0_g0od_23540368}
