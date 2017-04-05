# Word-Predict

The program uses array to implement the trie. Starting with 31 None elements in the trie, for each character in the word, it will open a list contains 31 None elements at the index which is convert by the ascii code of the character of the array.
The first 26 elements is the alphabet contains from a to z.

The 27th element is “$” symbol for the end of the word.
The 28th element is the biggest frequency.
The 29th element is mean of the word.
The 30th element is used to count the number of word has the same prefix.
The 31th element is the word has biggest frequency.
The program will run through each character of the prefix to find the word has biggest frequency. Then run through each character of that word to achieve the meaning of it.


Space complexity: O(T)
Time complexity: O(M+N)
