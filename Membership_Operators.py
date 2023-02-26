Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10 is 10
True
>>> 10 is 10.
False
>>> id(10)
3077552302672
>>> id(10.)
3077591702544
>>> 10. is 10.
True
>>> 10==10.
True
>>> # == content equality
>>> # is checks address id():Performs address equality
>>> #-----------------------------------
>>> id(10.)
3077591702544
>>> id(10.)
3077591702576
>>> 3077591702576
3077591702576
>>> 10. is 10.
True
>>> Trueg1=10.
>>> g2=10.
>>> g1=10.
>>> g1 is g2
False
>>> id(g1)
3077591044560
>>> id(g2)
3077591044400
>>> 3077591044400# Operators
3077591044400
>>> # Membership Operators
>>> #To chcek either object is memer of collection or not.
>>> # Two types: in,not in
>>> s='Reva jagtap'
>>> s
'Reva jagtap'
>>> 'r' in s
False
>>> 'R'
'R'
>>> 'R' in s
True
>>> 'Jagtap' in s
False
>>> 'jagtap in s
SyntaxError: EOL while scanning string literal
>>> 'jagtap' in s
True
>>> 'yug' in s
False
>>> 100 in s
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    100 in s
TypeError: 'in <string>' requires string as left operand, not int
>>> '100' in s
False
>>> k=[1,2,3,4,5]
>>> k
[1, 2, 3, 4, 5]
>>> 5 in k
True
>>> 9 in k
False
>>> k1=['1',2,3,4,'5','6',7]
>>> k1
['1', 2, 3, 4, '5', '6', 7]
>>> '5' in k1
True
>>> 7 in k1
True
>>> '8' in k1
False
>>> #Bitwise operator: & (and), | (or), ~ (not), ^ (XOR)
>>> s=[1,2,3]
>>> s1=[1,2,3,4]
>>> s & s1
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s & s1
TypeError: unsupported operand type(s) for &: 'list' and 'list'
>>> # print() function
>>> print()

>>> # print(value,...,sep = ' ',end='\n')
>>> print(100)
100
>>> print(100,200,300)
100 200 300
>>> print(100,'python',30.99)
100 python 30.99
>>> print(100,'python',30.99,sep = '--') #change sep
100--python--30.99
>>> # sep works between 2 objects only
>>> print(100,sep='==>')
100
>>> print(100,'A',sep='==>')
100==>A
SyntaxError: invalid syntax
>>> end: default it \n means a new line at end
>>> # we can modify end with any oher string
>>> # other*
>>> print(100,'A')
100 A
>>>  print(100,'A',end='end of stetemnt')
SyntaxError: unexpected indent
>>> print(100,'A',end='end of stetemnt')
100 Aend of stetemnt
>>> # ramesh is 28 yrs old
>>> print(100)
100
>>> print(100,end='\n\n')
100

>>> print(100,end='\n\n\n')
100


>>> # take the help of help() function
SyntaxError: invalid syntax
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> name  = 'sarang'
     
>>> place = 'Pune'
     
>>> name
     
'sarang'
>>> place
     
'Pune'
>>> # Hello, your name is sarang, and place is Pune
     
>>> print('Hello, your name is:',name)
     
Hello, your name is: sarang
>>> print('Hello, your name is:',name,', and place is:',place)
     
Hello, your name is: sarang , and place is: Pune
>>> # Q> can we use escape sequences: \n(new line), \t(tab 4 space)
     
SyntaxError: multiple statements found while compiling a single statement
>>> print('Hello, your name is:',name,', and place is:',place)
     
Hello, your name is: sarang , and place is: Pune
>>> print('Hello, your name is:',name,',\nand place is:',place)
     
Hello, your name is: sarang ,
and place is: Pune
>>> print('Hello, your name is:',name,',\n and place is:',place)
     
Hello, your name is: sarang ,
 and place is: Pune
>>> print('Hello,         your name is:',name,',\n and place is:',place)
     
Hello,         your name is: sarang ,
 and place is: Pune
>>> # space is also a part of string
     
print('Hello, your name is:',name,',\tand place is:',place)
     
Hello, your name is: sarang ,	and place is: Pune
>>> print(1,2,3)
     
1 2 3
>>> print(1,2,3,sep='\t')
     
1	2	3
>>> print(1,'\t',2,'\t',3)
     
1 	 2 	 3
>>> print('Milind','Dhavale')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print('Hello, your name is:',name,', and place is:',place)
NameError: name 'name' is not defined
>>> Milind Dhavale
>>> print('Milind'+'Dhavale')
     
MilindDhavale
>>> 'Milind'+'Dhavale' #it does concatention
     
'MilindDhavale'
>>> 'Milind'+' Dhavale'
     
'Milind Dhavale'
>>> 'Milind '+'Dhavale'
     
'Milind Dhavale'
>>> 'Milind'+' '+'Dhavale'
     
'Milind Dhavale'
>>> pi = 3.14
     
>>> r = 4
     
>>> print('Area of circle is:',pi*r**2)
     
Area of circle is: 50.24
>>> area = pi*r*r
     
>>> area
SyntaxError: invalid syntax
>>> 50.24
>>> print('Area of circle is:',area)
     
Area of circle is: 50.24
>>> # input(): it is a function, used to take input from user
     
>>> r = input('Enter the radius of a circle:')
     
Enter the radius of a circle:2.1
>>> r
     
'2.1'
>>> type(r)
     
<class 'str'>
>>> # input always takes value in str form
     
>>> # so we need to convert/typecast
     
r = float(input('Enter the radius of a circle:'))
     
Enter the radius of a circle:2.1
>>> r
     
2.1
>>> type(r)
     
<class 'float'>
>>> print('Area of circle is:',pi*r**2)
     
Area of circle is: 13.8474
>>> #---------------
     
>>> 12.33
     
12.33
>>> int(12.33)
     
12
>>> #Typecast means converting a data from one type to other type
     
str(12.33)
     
'12.33'
>>> print('Area of circle is:',round(pi*r**2,2))
     
Area of circle is: 13.85
>>> 
