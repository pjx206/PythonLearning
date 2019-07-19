filename = input('Enter the file name(e.g. "D:/a/b.txt"):')

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print('File ' + filename + ' does not exist')
else:
    words = contents.split()
    num_words = len(words)
    for i in range(num_words):
        words[i] = words[i].lower()
    
    counter = {}
    for word in words:
        if word in counter.keys():
            counter[word] += 1
        else:
            counter[word] = 1

#TODO: finish the errors handling
with open('data.txt', 'w') as data:
    print('Counting................')
    for word, times in counter.items():
        if word.isalpha():
            data.write(word + ':' + str(times) +' time(s)' + '\n')
    print('DONE! the statistics has been writen to "data.txt".')