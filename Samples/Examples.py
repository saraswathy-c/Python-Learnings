Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(9)
<class 'int'>
>>> type(9.8)
<class 'float'>
>>> name = 'youtube'
>>> name
'youtube'
>>> name[0]
'y'
>>> name[2]
'u'
>>> name[-1]
'e'
>>> nmae[-3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    nmae[-3]
NameError: name 'nmae' is not defined
>>> name[-3]
'u'
>>> name[-7]
'y'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[0:3]
'you'
>>> name[3]
't'
>>> name[1:4]
'out'
>>> name[2:5]
'utu'
>>> name[5]
'b'
>>> name[1:]
'outube'
>>> name[3:]
'tube'
>>> name[:3]
'you'
>>> name[:4]
'yout'
>>> name[3:6]
'tub'
>>> 'my' + name[4:]
'myube'
>>> name[0:3] = 'abc'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name[0:3] = 'abc'
TypeError: 'str' object does not support item assignment
>>> name[1]
'o'
>>> name[1] ='l'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name[1] ='l'
TypeError: 'str' object does not support item assignment
>>> 
>>> len(name)
7
>>> 