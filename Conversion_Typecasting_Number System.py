Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> b=10.0
>>> b
10.0
>>> id(a)
2206473611856
>>> id(b)
2206513734000
>>> a==b
True
>>> a is b
False
>>> id(a) ==id(b)
False
>>> id(a) is id(b)
False
>>> a == b #content equality
True
>>> a is b # address quality which gives boolean op
False
>>> hekp(print())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hekp(print())
NameError: name 'hekp' is not defined
>>> help(print())

Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> # use of \n,\t
>>> print('Hello Reva,\n How r u')
Hello Reva,
 How r u
>>> print('Hello Reva,\t How r u')
Hello Reva,	 How r u
>>> #Typecasting-TypeConversion
>>> #Typeconversion-Converting one form of type to another
>>> a=10
>>> a
10
>>> type(a)
<class 'int'>
>>> #convert int to str
>>> str(a)
'10'
>>> type(a)
<class 'int'>
>>> a=float(a)
>>> a
10.0
>>> type(a)
<class 'float'>
>>> a=str(a)
>>> a
'10.0'
>>> type(a)
<class 'str'>
>>> a=complex(a)
>>> a
(10+0j)
>>> type(A)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    type(A)
NameError: name 'A' is not defined
>>> type(a)
<class 'complex'>
>>> # There are two types of conersion
>>> #1.Implicite Conversion
>>> x=5
>>> y=10
>>> x+y
15
>>> x*y
50
>>> 10/2
5.0
>>> 10//2
5
>>> #2.Explicite Converion
>>> # Conversion performed by user as per the requirements.
>>> int(10+20)
30
>>> int(10+15.5)
25
>>> float(10+15.5)
25.5
>>> complex(10+20)
(30+0j)
>>> quantity=input('enter your quantity:')
enter your quantity:10
>>> quantity
'10'
>>> #final bill
>>> rate*quantity
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    rate*quantity
NameError: name 'rate' is not defined
>>> rate=20
>>> rate*quantity
'1010101010101010101010101010101010101010'
>>> #in above case it performs repetititons
>>> rate*int(quantity)
200
>>> ########################
>>> # Number System:
>>> # Binary [0,1]- base 2
     
>>> # Octal [0-7]-  base 8
     
>>> # Decimal [0-9]- base 10
     
>>> # Hexa decimal [0-9A-F]
     
>>> # Default number system we have is Decimal
SyntaxError: invalid syntax
>>> n=200
>>> n
200
>>> # dec to binary
>>> bin(n)
'0b11001000'
>>> bin(20)
'0b10100'
>>> help(bin)
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'

>>> #Decimal to octal
>>> oct(n)
'0o310'
>>> oct(20)
'0o24'
>>> # Decimal tohexa decimal
>>> hex(n)
'0xc8'
>>> hex(45)
'0x2d'
>>> 