
### Implementation

- In this task, I completed TrieNode and Trie classes
- Each TrieNode includes a boolean attribute and a dictionary, the key is char, and value is a pointer to the next Trienode 
- Each Trie includes insert and find opearations
- I defined a helper function to find suffixes in the outside,so the suffixes finding function can recall the helper function directly

define n as number of characters
define m as number of words
Worst case time:O(n*m)
Space complexity: O(n*m)
