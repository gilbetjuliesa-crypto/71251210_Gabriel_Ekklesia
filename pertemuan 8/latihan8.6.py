import re
import random
import string

random.seed(1)  

teks = input("Masukkan teks: ")

emails = re.findall(r'\S+@\S+', teks)

for email in emails:
    username = email.split("@")[0]
    
    password = ""
    for i in range(8):
        password += random.choice(string.ascii_letters + string.digits)
    
    print(email, "username:", username, ", password:", password)