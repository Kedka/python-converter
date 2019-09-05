import binascii
loop = 1

def b2t(text):
	n = int(text, 2)
	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def hex(text):
	return bytes.fromhex(text).decode('ascii')

def oct(text):
	i = 0
	j = 0
	x = []
	y = []
	while i < len(text):
		x.append(int(text[i], 8))
		i += 1
	while j < len(x):
		y.append(chr(x[j]))
		j += 1
	return y

while(loop == 1):
	print("Select mode:\n1.Binary to text\n2.Hex to text\n3.Octal to text\nAny other number to end")
	menu = input()
	#Any format
	if menu == '1':
		print("Insert binary code:")
		text = input()
		print(b2t(text.replace(' ', '')))
	#Any format
	elif menu == '2':
		print("Insert hex code:")
		text = input()
		print(hex(text.replace(' ', '')))
	#Required xxx xxx xxx format
	elif menu == '3':
		print("Insert octal code:")
		text = input()
		text = list(text.split(' '))
		print(''.join(oct(text)))
	else:
		print("Goodbye!")
		loop = 0
