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
    garbage = "123456:;7890(){}[]!$%*&=:?,.+-\\\/\"\"'"
    for line in input_file:
        tempLine = line
        for i in range(0, len(garbage)):
            tempLine = tempLine.replace(garbage[i],'')
            tempLine = tempLine.replace('<b>','')
            tempLine = tempLine.replace('</b>','')
            tempLine = tempLine.replace('<i>','')
            tempLine = tempLine.replace('</i>','')
            tempLine = tempLine.replace('<pd>','')
            tempLine = tempLine.replace('</pd>','')
            tempLine = tempLine.replace('<u>','')
            tempLine = tempLine.replace('</u>','')
            tempLine = tempLine.replace('<>','')
            tempLine = tempLine.replace('<','')
            tempLine = tempLine.replace('>','')
        lineList = tempLine
        words = lineList.split()
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
    output_file = open('cleanCount.txt', 'wb')
    for word in words:
        output_file.write (word + " " + str(word_count[word]) + "\n")
    output_file.close()


if __name__ == '__main__':
    main()
