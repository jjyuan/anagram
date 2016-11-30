import sys

dictionary = list()
def setup(inputs):
    word = inputs.readline().strip()
    while word:
        dictionary.append(word)
        word = inputs.readline().strip()
    print dictionary

def run():
    response = raw_input()
    if response == "":
        return
    result = ""
    for words in dictionary:
        if is_anagram(response, words):
            result += words +" "
    if result == "":
        result += "-"
    print result

    run()
def is_anagram(str1, str2):
    l1 = list(str1)
    l1.sort()
    l2 = list(str2)
    l2.sort()

    return ''.join(l1) == ''.join(l2)


filename = sys.argv;
if len(filename) == 2:
    inf = open(filename[1])
    setup(inf)
    run()
else:
    print("not enough arguments")