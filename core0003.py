"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
rlist = [I,V,X,L,C,D,M]

rome = 2257
number = 0

if rome >= 1000:
    count = rome//1000
    result = rome%1000
    number = 'M'*count
    printer = number
    rome = result
if rome >= 500:
    count = rome//500
    result = rome%500
    number = 'D'*count
    printer += number
    rome = result
if rome >= 100:
    count = rome//100
    result = rome%100
    number = 'C'*count
    printer += number
    rome = result
if rome >= 50:
    count = rome//50
    result = rome%50
    number = 'L'*count
    printer += number
    rome = result
if rome >= 10:
    count = rome//10
    result = rome%10
    number = 'X'*count
    printer += number
    rome = result
if rome >= 5:
    count = rome//5
    result = rome%5
    number = 'V'*count
    printer += number
    rome = result
if rome >= 1:
    count = rome//1
    result = rome%1
    number = 'I'*count
    printer += number
    rome = result
print(printer)