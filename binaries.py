# Convert a binary number to an integer decimal number - my own method

bin1 = 11001111
bin2 = str(bin1)
bin3 = list(bin2)

cnt1 = 0
for x in bin3:
    cnt1 += 1
c2 = cnt1 - 1
d1 = 0
for i in bin3:
    d1 += (int(i) * (2 ** c2))
    c2 -= 1
print(d1)

# Convert a Binary character string to a real text decimal character

x = '11001111'
print(chr(int(x, 2)))

# Convert decimal characters to binary

p = bin(int.from_bytes('Johannes'.encode(), 'big'))
print(p[2:])

# Convert Binary to decimal characters

chr_str = int('0b100101001101111011010000110000101101110011011100110010101110011', 2)
result = chr_str.to_bytes((chr_str.bit_length() + 7) // 8, 'big').decode()
print(result)

# Read a binary file 8 characters at a time and convert to decimal characters

with open('binary_file1.txt', 'rb') as bf:
    data = bf.read()
    print(data)

with open('binary_file1.txt', 'r') as binf:
    data2 = binf.read(8)
    while data2 != '':
        text = chr(int(data2, 2))
        print(text, end = '')
        data2 = binf.read(8)

# Use the struct module to generate & write a binary file

import sys
sys.byteorder
import struct

bf_out = open('bin1_file', 'wb')

# # Create a [2 byte ID][4 byte value] file

id = 0
value = id

for x in range(50):
    data = struct.pack('<HI', id, value)
    id += 1
    value = id
    bf_out.write(data)
    bf_out.flush()

bf_out.close()

with open('bin1_file', 'rb') as binny:
    for x in binny:
        print(binny)

# Convert Binary number to a decimal integer number using classes & functions Number 1

class binary_to_integer():
    def __init__(self, binary_nbr):
        self._binary_nbr = binary_nbr
        self._binary_nbr = self._binary_nbr[::-1]
        self._binary_nbr = list(self._binary_nbr)
        self._l1 = [1]
        self._cntr1 = 1
        self._base2 = 2
        self._cntr2 = 0
        print(self._converted_number(self._binary_nbr))
    def _converted_number(self, bin_number):
        self._nbr2 = bin_number
        print(self._nbr2)
        for i in range(1, len(self._nbr2)):
            self._total = self._cntr1 * self._base2
            self._cntr1 = self._total
            self._l1.append(self._cntr1)
            self._deep = zip(self._nbr2, self._l1)
        for self._x, self._y in self._deep:
            if self._x == '1':
                self._cntr2 += self._y
        return self._cntr2

swannie1 = binary_to_integer('111100011101')

# Convert Binary number to a decimal integer number using classes & functions Number 2

class binary_to_integer():
    def __init__(self, binary_nbr):
        self._binary_nbr = binary_nbr
        self._binary_nbr = list(self._binary_nbr)
        print(self._converted_number(self._binary_nbr))
    def _converted_number(self, bin_number):
        self._cnt1 = 0
        for x in bin_number:
            self._cnt1 += 1
            self._c2 = self._cnt1 - 1
            self._d1 = 0
        for i in bin_number:
            self._d1 += (int(i) * (2 ** self._c2))
            self._c2 -= 1
        return self._d1

swannie2 = binary_to_integer('111100011101')

# Quickest way to convert Binary to Decimal integers

print(f'{0b111100011101:#0}')

# OR

print(int(0b111100011101))

# Quickest way to convert Decimal integers to binary

x = '27'
y = bin(int(x, 10))
print(y)

# OR

print(bin(27))
