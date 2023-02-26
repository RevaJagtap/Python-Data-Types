Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2j
2j
>>> type(2j)
<class 'complex'>
>>> '4j'
'4j'
>>> type('4j')
<class 'str'>
>>> ''
''
>>> type('')
<class 'str'>
>>> r=5
>>> pi=3.14
>>> area= pi*r**2
>>> area
78.5
>>> r=4
>>> r
4
>>> area
78.5
>>> area=pi*r**2
>>> area
50.24
>>> #operators
>>> # Assignment Operators
>>> a=200
>>> a
200
>>> a+150
350
>>> a
200
>>> a=a+150
>>> a
350
>>> a
350
>>> a=a+250
>>> a
600
>>> a=a-200
>>> a
400
>>> a
400
>>> a=a*=2
SyntaxError: invalid syntax
>>> a=a*2
>>> a
800
>>> a*=2
>>> a
1600
>>> a+100
1700
>>> a
1600
>>> a=a+150
>>> a
1750
>>> a*2
3500
>>> a
1750
>>> a%2
0
>>> a%=2
>>> a
0
>>> #conditional operator
>>> 20>40
False
>>> 10<14
True
>>> id(20)
2549035002768
>>> id (40)
2549035003408
>>> 20>=
SyntaxError: invalid syntax
>>> 
>>> 20<=20.0
True
>>> id (20)
2549035002768
>>> id(20.0)
2549054025104
>>> x=102
>>> y=125
>>> x==y
False
>>> x=100
>>> y=100
>>> x==y
True
>>> id(x)
2549035193808
>>> id
<built-in function id>
>>> id(y)
2549035193808
>>> x==y
True
>>> r=50
>>> s=50.0
>>> r==s
True
>>> r is s
False
>>> id(r)
2549035003728
>>> id(s)
2549054025104
>>> id(r)==id(s)
False
>>> 40!=59
True
>>> s1=
SyntaxError: invalid syntax
>>> s1='Raya'
>>> s2='raya'
>>> s1==s2
False
>>> s1is s2
SyntaxError: invalid syntax
>>> s1!=s2
True
>>> s1 is s2
False
>>> d1=60
>>> d1
60
>>> id(d1)
2549035192528
>>> d2=60
>>> d2
60
>>> id(d2)
2549035192528
>>> d3=60.0
>>> d3
60.0
>>> id(d3)
2549054025168
>>> d4=60.00
>>> d4
60.0
>>> id(d4)
2549053365264
>>> name=Reva
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    name=Reva
NameError: name 'Reva' is not defined
>>> name='reva'
>>> name
'reva'
>>> age=28
>>> age
28
>>> name=='Reva' and age 23
SyntaxError: invalid syntax
>>> name=='Reva' and age=23
SyntaxError: cannot assign to operator
>>> name=='Reva' and age=23
SyntaxError: cannot assign to operator
>>> name=='reva' and age=23
SyntaxError: cannot assign to operator
>>> name='reva'
>>> name
'reva'
>>> age=28
>>> name=='reva'
True
>>> age==4
False
>>> name=='reva' and age==25
False
>>> name=='reva' and age==28
True
>>> name=='reva' or age==28
True
>>> name=='reva' or age==23
True
>>> name=='rekha' or age==28
True
>>> name=='rekha' or age==27
False
>>> not name=='reva''
SyntaxError: EOL while scanning string literal
>>> not name=='reva'
False
>>> not name=='radha'
True
>>> age==25
False
>>> not age==26
True
>>> not name=='isha'
True
>>> bool('reva')
True
>>> bool(12.35)
True
>>> bool(none)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    bool(none)
NameError: name 'none' is not defined
>>> bool(None)
False
>>> bool('')
False
>>> 10.25 and 75
75
>>> -14 and -52
-52
>>> 