import sys

dictionary = list()
sorted_dictionary = list()
def setup(inputs):
    word = inputs.readline().strip()
    while word:
        dictionary.append(word)
        word = inputs.readline().strip()
    # print dictionary
    dictionary.sort()
    for d in dictionary:
        l = list(d)
        l.sort()
        sorted_dictionary.append((d, ''.join(l)))
    # print sorted_dictionary

def run():
    response = raw_input()
    if response == "":
        return
    result = ""
    for orig_word, sorted_word in sorted_dictionary:
        if is_anagram(response, sorted_word):
            result += orig_word + " "
    if result == "":
        result += "-"
    print result
    run()
    
def is_anagram(str1, str2):
    l1 = list(str1)
    l1.sort()
    l2 = list(str2)

    return l1==l2


filename = sys.argv;
if len(filename) == 2:
    inf = open(filename[1])
    setup(inf)
    run()
else:
    print("not enough arguments")