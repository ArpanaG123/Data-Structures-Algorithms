# Implement Trie (Prefix Tree)
# Link - https://leetcode.com/problems/implement-trie-prefix-tree/description/

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
# Example:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True


class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary instead of fixed 26 slots
        self.is_end = False  # Marks end of word

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 1. Insert (word)
# For each character in the word, we either follow an existing node or create a new one.
# Each step is O(1) (dictionary lookup or array index).
# TC: O(n)
# SC: In the worst case, we create a new node for every character → O(n) new space for that word. Across all insertions, space = total number of characters across all words = O(Σ |word_i|).

# 2. Search (word)
# We traverse through all characters of the word.
# Each step is O(1).
# TC: O(n)
# SC: O(1) (no extra space except a few pointers).

# 3. startsWith (prefix)
# Similar to search, we just check if the prefix path exists.
# TC: O(n)
# SC: O(1)

# 4. Overall Space Complexity of Trie
# Each node stores up to 26 children + is_end flag.
# Worst-case: if we insert k words, each of max length n, the trie can have O(k * n) nodes.
# SC: O(k * n)