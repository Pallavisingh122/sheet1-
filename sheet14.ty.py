Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
name1 = d['Name']
sub1 = d['Subject']
ratings1 = d['Ratings']
inp = input("input: ")
input: a=[] b=[] c=[]
count = sub1.count(inp)
for i in range(count):
    j = sub1.index(inp)
    x.append(name1[j])
    y.append(sub1[j])
    z.append(ratings1[j])
    del name1[j]
    del sub1[j]
    del ratings1[j]
    newData = dict()
    newData['Name'] = a
    newData['Subject'] = b
    newData['Ratings'] = c
    print(newdata)
    