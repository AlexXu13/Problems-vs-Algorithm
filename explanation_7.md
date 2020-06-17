
### Implementation

- I completed this task according to the instructions.

define n as unique URLs
define m as length of the longest piece of URL separated by backslash
- Worst case time:  
RouteTrie: insert and find O(n)
RouteTrieNode: lookup O(1)
Router:add_handlerO(n) lookup O(n*m)                    
- Space complexity: 
RouteTrie: insert and find O(n)
RouteTrieNode: O(1)
Router:add_handlerO(n) lookup O(n*m) 
