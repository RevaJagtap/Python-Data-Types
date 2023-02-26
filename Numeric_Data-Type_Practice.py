Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #data types
>>> #Numeric:int,float,complex
>>> 10
10
>>> 102.5
102.5
>>> 14.2
14.2
>>> 22.7
22.7
>>> complex
<class 'complex'>
>>> #complex
>>> 2+5
7
>>> 2+5j
(2+5j)
>>> type
<class 'type'>
>>> type(2+5j)
<class 'complex'>
>>> 5
5
>>> =2.5J
SyntaxError: invalid syntax
>>> 2
2
>>> 2+5J
(2+5j)
>>> type(2+5j)
<class 'complex'>
>>> #string
>>> #syntax
>>> ""
''
>>> ''
''
>>> 124n
SyntaxError: invalid syntax
>>> "125k"
'125k'
>>> 'bvdhfjdlsc,xznkvhdsj'
'bvdhfjdlsc,xznkvhdsj'
>>> J='REVA JAGTAP'
>>> J
'REVA JAGTAP'
>>> len(J)
11
>>> len(J)-1
10
>>> J(5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    J(5)
TypeError: 'str' object is not callable
>>> J[5]
'J'
>>> J[12]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    J[12]
IndexError: string index out of range
>>> J[4]
' '
>>> id(J)
1937958159984
>>> J
'REVA JAGTAP'
>>> J.__sizeof_()_
SyntaxError: invalid syntax
>>> J.__sizeof_()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    J.__sizeof_()
AttributeError: 'str' object has no attribute '__sizeof_'
>>> s.__sizeof_()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.__sizeof_()
NameError: name 's' is not defined
>>> J.__sizeof__()
60
>>> J[10].__sizeof__()
50
>>> J[-10]
'E'
>>> J[-2]
'A'
>>> J[:]
'REVA JAGTAP'
>>> J[0:8]
'REVA JAG'
>>> J[0:11]
'REVA JAGTAP'
>>> J[0:10]
'REVA JAGTA'
>>> J[0:4]
'REVA'
>>> J[5:11]
'JAGTAP'
>>> J[4:9]
' JAGT'
>>> J[5:]
'JAGTAP'
>>> J[-11:-5]
'REVA J'
>>> J[-4:-10]
''
>>> helpJ[-4:-10]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    helpJ[-4:-10]
NameError: name 'helpJ' is not defined
>>> J[::1]
'REVA JAGTAP'
>>> J[::2]
'RV ATP'
>>> J[::3]
'RAAA'
>>> J[::5]
'RJP'
>>> J[-4::-1]
'GAJ AVER'
>>> J[-1:-8:-1]
'PATGAJ '
>>> J[-1:-10:-1]
'PATGAJ AV'
>>> J[-2:-10:-2]
'AGJA'
>>> J[-2:-10:-3]
'AAA'
>>> J[-2:-10:-4]
'AJ'
>>> J[-2:-11:-1]
'ATGAJ AVE'
>>> J[:8:-1]
'PA'
>>> J[:10:-1]
''
>>> J[:8:-2]
'P'
>>> J[:8:2]
'RV A'
>>> J[:7:-1]
'PAT'
>>> J[:7:-2]
'PT'
>>> J[:7:-3]
'P'
>>> J[154:1562:124587]
''
>>> 