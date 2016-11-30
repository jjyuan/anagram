Answers:
1. The complete runtime for offline step is: O(N + NlogN + NMlogM) where N is the number of words in the dictionary, and M is the length of the longest word in the dictionary. This simplifies to O(N*MlogM) if the dictionary includes long words, otherwise it's O(NlogN). 
The runtime for the online step is: O(N*M*MlogM) where N is the number of words in the dictionary and M is the length of the longest word(s). 
2. If N is the number of words in the dictionary, my program consumes O(N + N), or O(N).
3. With this little memory, available, we'll have to compromise runtime significantly. We can use read in the dictionary as an iterator and as we process each word and its anagrams, we'll be iterating through that dictionary iterator. 

*More explanation to runtime is included in comments in my code.
