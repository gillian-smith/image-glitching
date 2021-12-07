# Raw data glitcher

# Works, but isn't very elegant
def wordpad_effect1(data):
	i = 0
	newdata = b''
	while i > -1:
		i = data.find(b'\x0a')
		newdata = newdata + data[:i] + b'\x0a\x0d'
		data = data[i+1:]
	newdata = newdata[:-2] + bytes({data[-1]})
	return newdata

# Doesn't work
def wordpad_effect2(data):
	data_list = data.split()
	i = 0
	newdata = b''
	while i < len(data):
		if data[i] == b'\x0a' and (i+1 == len(data) or data[i+1] != b'\x0d'):
			newdata = newdata + b'\x0a\x0d'
		elif data[i] == b'\x0a' and (i+1 == len(data) or data[i+1] == b'\x0d'):
			i += 1
			newdata = newdata + b'\x0a\x0d'
		elif data[i] == b'\x0d':
			newdata = newdata + b'\x0a\x0d'
		#else newdata = newdata + data[i]
		i += 1
	return newdata

# Works
def wordpad_effect(data):
	data_list = data.split()
	newdata = data_list[0]
	for str in data_list[1:]:
		newdata = newdata + b'\x0a\x0d' + str
	return newdata

def main():
	test_str = b'\x0a\x0dabcdefg\x0ahijk\x0a\x0dlmnop\x0dqrst\x0d'
	print(wordpad_effect3(test_str))

if __name__=="__main__":
	main()