
#   Задание 1.

string_one = "разработка"
string_two = "сокет"
string_three = "декоратор"

bytes_string_one = string_one.encode()
bytes_string_two = string_two.encode()
bytes_string_three = string_three.encode()

print('"разработка" в байтах: ', bytes_string_one, '\n')
print('"сокет" в байтах: ', bytes_string_two, '\n')
print('"декоратор" в байтах: ', bytes_string_three)

print("-"*55)

#   Задание 2.

bytes_string_one = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
bytes_string_two = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
bytes_string_three = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

string_one = bytes_string_one.decode()
string_two = bytes_string_two.decode()
string_three = bytes_string_three.decode()

print(string_one, '\n')
print(string_two, '\n')
print(string_three)

print("-"*55)

#   Задание 3.

string_one = "разработка"

# привожу строку к байтам
a = string_one.encode()

# декодирую используя latin-1
c = a.decode('latin-1')
print(c)

import chardet
print(chardet.detect(a))

# декодирую используя utf-8
b = a.decode('utf-8')
print(b)
