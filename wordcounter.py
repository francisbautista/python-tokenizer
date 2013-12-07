import sys
def main():
	filename = raw_input('Enter a file name: ')
	fileWriter(filename)
	print "File written successfully"
	sys.exit(1)


#wordCounter takes in a file, parses through it,
#and returns the count per word in map
def wordCounter(filename):
	word_count = {}
	input_file = open(filename, 'r')
	for line in input_file:
		words = line.split()
		for word in words:
			word = word.lower()
			if not word in word_count:
				word_count[word] = 1
			else:
				word_count [word] = word_count[word] + 1
	input_file.close()
	return word_count

def fileWriter(filename):
	word_count = wordCounter(filename)
	words = sorted(word_count.keys())
	output_file = open('wordCountDirty.txt', 'wb')
	for word in words:
		output_file.write (word + " " + str(word_count[word]) + "\n")
	output_file.close()


if __name__ == '__main__':
	main()
