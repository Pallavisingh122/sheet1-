Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = input("Input words: ")
Input words: pallavi taru
word_list= x.split(",")
words_list.sort()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    words_list.sort()
NameError: name 'words_list' is not defined. Did you mean: 'word_list'?
word_list.sort()
print((',').join(word_list))
pallavi taru
