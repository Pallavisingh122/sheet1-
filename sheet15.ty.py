Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = int(input("enter an integer: ")
        def gnrtfunc():
            for i in range(0,n):
                if i%7==0:
                    yield i
                    else:
                        break
 values = gnrtfunc()
 print(values)
 print(next(values))
 for i in values:
     print(i)
     