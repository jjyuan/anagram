import sys                  # System library.

dictionary = list()         # Initializes an empty list.
sorted_dict = list()  # Initializes another empty list.

def setup(inputs):
    """
    The offline step. Stores all the words in the input dictionary into a list.
    Sorts that list. Stores tuples of the original word and a sorted version of that word
    into another list.
    """
    word = inputs.readline().strip()                # First word.
    while word:                                     # While the input file has lines.
        dictionary.append(word)                     # Adds each word into the dictionary list.
        word = inputs.readline().strip()            # Reads in the next word from the input.

    dictionary.sort()                               # Sorts this dictionary list.

    for d in dictionary:                            # Loop through each word of the newly sorted dictionary list.
        l = list(d.lower())                         # Converts the word into a list, where each character is now an element.
        l.sort()                                    # Sorts that list.
        sorted_dict.append((d, ''.join(l)))         # Appends a tuple (original word, sorted word) to the second list.

def run():
    """
    The online step. Functional called to print out anagrams of the inputed word.
    """
    response = raw_input().lower()                  # Prompts user for an input word.
    if response == "":                              # Checks if the word is an empty string.
        return                                      # Returns (exits) if it is.
    result = ""                                     # Initializing an empty string.
    l1 = list(response)                             # Memoization feature.
    l1.sort()                                       # Memoization feature^.
    for orig_word, sorted_word in sorted_dict:      # Looping through the tuples of (original word, sorted word).
        l2 = list(sorted_word)                      # Converts sorted_word into a list.
        if l1 == l2:                                # Checks if original word is an anagram of the input word.
            result += orig_word + " "               # If so, append that word to to the result string.
    if result == "":                                # Is the result string empty?
        result += "-"                               # If so, result should just be a dash.
    print(result)                                   # Prints result.
    run()                                           # Calls this function again, waiting for user input once more.


filename = sys.argv;                # filename is a list of arguments, i.e. ["anagrams.py", "dict.txt"].
if len(filename) == 2:              # Ensures that there are two arguments.
    inf = open(filename[1])         # Opens the file.
    setup(inf)                      # Offline step.
    run()                           # Online step.
else:
    print("not enough arguments")   # Something went wrong!

                                                                                                       
"""                                                                                          
TTTTTTTTTTTTTTTTTTTTTTThhhhhhh                                                kkkkkkkk                
T:::::::::::::::::::::Th:::::h                                                k::::::k                
T:::::::::::::::::::::Th:::::h                                                k::::::k                
T:::::TT:::::::TT:::::Th:::::h                                                k::::::k                
TTTTTT  T:::::T  TTTTTT h::::h hhhhh         aaaaaaaaaaaaa  nnnn  nnnnnnnn     k:::::k    kkkkkkk     
        T:::::T         h::::hh:::::hhh      a::::::::::::a n:::nn::::::::nn   k:::::k   k:::::k      
        T:::::T         h::::::::::::::hh    aaaaaaaaa:::::an::::::::::::::nn  k:::::k  k:::::k       
        T:::::T         h:::::::hhh::::::h            a::::ann:::::::::::::::n k:::::k k:::::k        
        T:::::T         h::::::h   h::::::h    aaaaaaa:::::a  n:::::nnnn:::::n k::::::k:::::k         
        T:::::T         h:::::h     h:::::h  aa::::::::::::a  n::::n    n::::n k:::::::::::k          
        T:::::T         h:::::h     h:::::h a::::aaaa::::::a  n::::n    n::::n k:::::::::::k          
        T:::::T         h:::::h     h:::::ha::::a    a:::::a  n::::n    n::::n k::::::k:::::k         
      TT:::::::TT       h:::::h     h:::::ha::::a    a:::::a  n::::n    n::::nk::::::k k:::::k        
      T:::::::::T       h:::::h     h:::::ha:::::aaaa::::::a  n::::n    n::::nk::::::k  k:::::k       
      T:::::::::T       h:::::h     h:::::h a::::::::::aa:::a n::::n    n::::nk::::::k   k:::::k      
      TTTTTTTTTTT       hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa nnnnnn    nnnnnnkkkkkkkk    kkkkkkk     
                                                                                                      
                                                           !!!                                        
                                                          !!:!!                                       
                                                          !:::!                                       
                                                          !:::!                                       
yyyyyyy           yyyyyyy ooooooooooo   uuuuuu    uuuuuu  !:::!                                       
 y:::::y         y:::::yoo:::::::::::oo u::::u    u::::u  !:::!                                       
  y:::::y       y:::::yo:::::::::::::::ou::::u    u::::u  !:::!                                       
   y:::::y     y:::::y o:::::ooooo:::::ou::::u    u::::u  !:::!                                       
    y:::::y   y:::::y  o::::o     o::::ou::::u    u::::u  !:::!                                       
     y:::::y y:::::y   o::::o     o::::ou::::u    u::::u  !:::!                                       
      y:::::y:::::y    o::::o     o::::ou::::u    u::::u  !!:!!                                       
       y:::::::::y     o::::o     o::::ou:::::uuuu:::::u   !!!                                        
        y:::::::y      o:::::ooooo:::::ou:::::::::::::::uu                                            
         y:::::y       o:::::::::::::::o u:::::::::::::::u !!!                                        
        y:::::y         oo:::::::::::oo   uu::::::::uu:::u!!:!!                                       
       y:::::y            ooooooooooo       uuuuuuuu  uuuu !!!                                        
      y:::::y                                                                                         
     y:::::y                                                                                          
    y:::::y                                                                                           
   y:::::y                                                                                            
  yyyyyyy                                                                                             
                                                                                                                                                                                                       

"""