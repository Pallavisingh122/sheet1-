Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
inp = input("enter the input:\n ")
enter the input:
 raw = inp.split("#")
for i in range(len(raw)):
    raw[i]=raw[i].split(" ")
    rx = raw[0]
    ry = raw[1]
    x = [ ]
    y =[ ]
    for i in rx:
        x.append(int(i))
      for i in ry:
          
SyntaxError: unindent does not match any outer indentation level
for i in ry:
    y.append(int(i))
    print("x = ",x)
    print("y = ",y)
    