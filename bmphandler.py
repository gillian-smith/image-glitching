# File handling of BMP images

def bytestonumber(list):
	ans = 0
	for x in list[::-1]:
		h = hex(x)
		for char in h[2:]:
			ans = 16*ans + hexdig2decdig(char)
	return ans

def hexdig2decdig(dig):
	return ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'].index(dig)

class BMP:
	def get_dimensions(self):
		width_list = list(self.header[18:22])
		self.width = bytestonumber(width_list)
		height_list = list(self.header[22:26])
		self.height = bytestonumber(height_list)
	def __init__(self, header, pixels):
		self.header = header
		self.pixels = pixels

def readBMP(filename):
	with open(filename, "rb") as file:
		bmpfile = file.read(-1)
	pixelarray_start = bmpfile[10] # Start position of pixel array in .bmp file
	header = bmpfile[:pixelarray_start]
	pixels = bmpfile[pixelarray_start:]
	return BMP(header, pixels)

def writeBMP(filename, img):
	with open(filename, "wb") as file:
		file.write(b'')
	with open(filename, "ab") as file:
		file.write(img.header)
		file.write(img.pixels)


def main():
	print("BMP handler")
	# Load .bmp file
	filename = "image.bmp"
	myBMP = readBMP(filename)
	myBMP.get_dimensions()
	# Print info about the file
	print(list(myBMP.header)) # print file header
	print("Height = ", myBMP.height)
	print("Width = ", myBMP.width)
	# Write to new file
	newfilename = "image3.bmp"
	with open(newfilename, "ab") as file:
		file.write(myBMP.header)
		file.write(myBMP.pixels)

if __name__ == "__main__":
	main()