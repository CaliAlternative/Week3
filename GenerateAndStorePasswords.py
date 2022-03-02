from email.generator import Generator
import random
import csv
class PasswordGenerator:
    def Generator(self, passwordLength: int):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "_!&"
        all = lower + upper + numbers + symbols
        length = passwordLength 
        password = " ".join(random.sample(all,length))
        print(password)
        return password 
    
class writeANDstorePassword    
    def savePassword(self, password_toSave: str):
        with open('savePassword.txt', 'w') as PasswordText:
         PasswordText.write(password_toSave)   
    
NewPassword = Generator(8)
SavePassword = writeANDstorePassword(NewPassword)