![image](https://user-images.githubusercontent.com/110505489/223919632-c0124e01-3c5b-4cd1-9c34-dd087f791eca.png)
same thing as PW crack 3, removed the:

user_pw = input
user_pw_hash = hash_pw(user_pw)

added pos_pw_list variable from cat level4.py
added for x in pos_pw_list
    added user_pw_hash = hash_pw(x)
removed user_pw from the decryption = str_xor(flag_enc.decode(), user_pw)
    added x in place of user_pw
