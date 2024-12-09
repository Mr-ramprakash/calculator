import random
passwd = int (input("Enter the length of the password"))
c = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
output="" .join(random.sample(c,passwd))
print(output)