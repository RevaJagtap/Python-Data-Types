Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String-Features
>>> #Accepts all type of data.
>>> #Background data structure array.
>>> # slicing applicable
>>> # It supports +ve &- ve indexing
>>> # It preserves sequesce order
>>> # gives tempo.output
>>> ##################################
>>> #Methods of string
>>> s='Reva jagtap'
>>> s
'Reva jagtap'
>>> # convert letter into uppercase
>>> s.upper()
'REVA JAGTAP'
>>> s
'Reva jagtap'
>>> # convert letter into lower
>>> s.l
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.l
AttributeError: 'str' object has no attribute 'l'
>>> s.lower()
'reva jagtap'
>>> #Capitalize:to make first letter of first work in CAPS
>>> s.capitalize()
'Reva jagtap'
>>> #title:to make first letter of each word is CAPS
>>> s.title()
'Reva Jagtap'
>>> s.index()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
>>> s.index(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.index(2)
TypeError: must be str, not int
>>> s.index(R)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s.index(R)
NameError: name 'R' is not defined
>>> s.index('R')
0
>>> #index:it returns lowest index.
>>> #rindex: if we want highest index then use rindex
>>> s.rindex('a')
9
>>> # find():it also gives index of an element
>>> s.find('Reva')
0
>>> s.find('Jagtap')
-1
>>> # Strip:reomve space using a strip method
>>> r='        Karad'
>>> r
'        Karad'
>>> r.strip()
'Karad'
>>> q='******Reva*******'
>>> q
'******Reva*******'
>>> q.strip()
'******Reva*******'
>>> q.lstrip()
'******Reva*******'
>>> q.lstrip('*')
'Reva*******'
>>> q.rstrip('*')
'******Reva'
>>> #lstrip: removes left side space
>>> #rstrip: removes right side space
>>> q.strip('*')
'Reva'
>>> #Split:Each word seperated by space should acts as an individual object.
>>> s.split()
['Reva', 'jagtap']
>>> m='Python is very sensitive language'
>>> m.split()
['Python', 'is', 'very', 'sensitive', 'language']
>>> f=='sadiya,prajwalita,reva,pooja,sharvari'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    f=='sadiya,prajwalita,reva,pooja,sharvari'
NameError: name 'f' is not defined
>>> f = 'sadiya,prajwalita,reva,pooja,sharvari'
>>> f
'sadiya,prajwalita,reva,pooja,sharvari'
>>> f.split(',')
['sadiya', 'prajwalita', 'reva', 'pooja', 'sharvari']
>>> #Replace:in order to remove an element present in between will use replace.
>>> a = 'Yuga**##ndhar**'
>>> a
'Yuga**##ndhar**'
>>> a.replace('**##','')
'Yugandhar**'
>>> aa = a.replace('**##','')
>>> aa
'Yugandhar**'
>>> aa.strip('*')
'Yugandhar'
>>> aaa = aa.strip('*')
>>> aaa
'Yugandhar'
>>> a
'Yuga**##ndhar**'
>>> aa
'Yugandhar**'
>>> aaa
'Yugandhar'
>>> aaa.replace('dhar','')
'Yugan'
>>> fname='Reva'
>>> lname='jagtap'
>>> fnale
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    fnale
NameError: name 'fnale' is not defined
>>> fname
'Reva'
>>> lname
'jagtap'
>>> #concatenate 2 string
>>> fname+lname
'Revajagtap'
>>> fname+''+lname
'Revajagtap'
>>> fname+'  '+lname
'Reva  jagtap'
>>> #Slicing
>>> aaa
'Yugandhar'
>>> aaa[:4]
'Yuga'
>>> aaa[-1]
'r'
>>> aaa[-1:-9]
''
>>> aaa[-1:-8]
''
>>> aaa[-1:-9:-1]
'rahdnagu'
>>> aaa[-1:-10:-1]
'rahdnaguY'
>>> aaa[2:7:-1]
''
>>> aaa[2:7:2]
'gnh'
>>> aaa[3:8]
'andha'
>>> #Count:if we want to count number of occurances.
>>> s.count('r')
0
>>> s.count('R')
1
>>> s.count('a)
	
SyntaxError: EOL while scanning string literal
>>> s.count('a')
3
>>> f
'sadiya,prajwalita,reva,pooja,sharvari'
>>> result=f.split(',')
>>> result
['sadiya', 'prajwalita', 'reva', 'pooja', 'sharvari']
>>> #data is in the form of list of str
>>> # and i want string now
>>> # we can use join() method
SyntaxError: invalid syntax
>>> ','.join(result)
'sadiya,prajwalita,reva,pooja,sharvari'
>>> t=['I love my India']
>>> t
['I love my India']
>>> ','.join(t)
'I love my India'
>>> s
'Reva jagtap'
>>> s.startswith('a')
False
>>> s.startswith('R')
True
>>> s.endswith('p')
True
>>> t
['I love my India']
>>> t.endswith('dia')
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    t.endswith('dia')
AttributeError: 'list' object has no attribute 'endswith'
>>> ','.join(t)
'I love my India'
>>> res=''.join(t)
>>> res
'I love my India'
>>> res.endswith('dia')
True
>>> res.startswith('I')
True
>>> x = 'abc'
>>> x
'abc'
>>> x.isalpha()
True
>>> x = 'abc123'
>>> x.isalpha()
False
>>> x.isalnum()
True
>>> x = '    '
>>> x
'    '
>>> x.isidentifier()
False
>>> x = '_'
>>> x
'_'
>>> x.isidentifier()
True
>>> x = 'and'
>>> x
'and'
>>> x.isidentifier()
True
>>> x = 'in'
>>> x
'in'
>>> x.isidentifier()
True
>>> x = '#$'
>>> x.isidentifier()
False
>>> x = '1and'
>>> x
'1and'
>>> x.isidentifier()
False