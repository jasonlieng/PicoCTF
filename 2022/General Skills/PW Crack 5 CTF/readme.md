![image](https://user-images.githubusercontent.com/110505489/223926703-3bdb198e-a876-4768-9a3f-4b0729be775a.png)


cleared user_pw = input
cleared user_pw_hash = hash_pw(user_pw)

set pw_list = open("dictionary.txt", "r") #opens dictionary.txt as the file

Created a for loop:
for x in pw_list:
    y = x.strip("\n") #strips the newline space
    user_pw_hash = hash_pw(y)
    
cleared user_pw in decryption = str_xpr(flag_enc.decode(), user_pw) replace with y

Make sure the have everything under the for loop indented enough to be included in the for loop
Caused issue by ending the loop at the last entry of the dictionary.txt and wasn't able to return to continue loop
