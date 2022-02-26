Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = input("enter a string: ")
enter a string: 67
a=0
b=0
for c in s:
    if c.isdigit():
        a=a+1
    elif c.isalpha():
        b=b+1
    else:
        pass
print("letters: ",b)
print("digits: ",a)