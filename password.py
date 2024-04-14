import random 
def create_pass(length):
    key=('0123456789'
         'abcdefghijklmnopqrstuvwxyz'
         'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         '!@#$%^&*()_+=')
    password=''.join(random.choices(key,k=length))
    return password
print("welcome to password generator:")
length=int(input("enter the size of password you want to generate:"))
password = create_pass(length)
print("PASSWORD :", password)
