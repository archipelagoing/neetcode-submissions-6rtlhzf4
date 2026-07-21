class TrieNode:
    def __init__(self):
        self.children = {} # empty hashmap
        self.endOfWord = False

# each node has 26 children, indexed directly using character positions
# boolean flag endOfWord tells us whether a complete word ends at that node.
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    # Insert(word)
    # 1. Start from the root.
    # 2. For each character in the word:
    # 3. Convert character to index (c - 'a')
    # 4. If the child node doesn’t exist, create it.
    # 5. Move to the child.
    # 6. After processing all characters, mark endOfWord = true. 
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

# ---------------Search(word)----------------
# 1. Start from the root.--------------------
# 2. For each character:---------------------
# 3. Move to the corresponding child.--------
# 4. If missing, return false.---------------
# 5. After traversal:------------------------
# 6. Return true only if endOfWord is true.--
    def search(self, word: str) -> bool:

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord # if true, it is a word. if not, its not a word.
        
#  StartsWith(prefix)---------------------
# 1. Start from the root.-------------------
# 2. Traverse characters of the prefix.-----
# 3. If all characters exist in sequence,--- 
#-------------------return true.------------
# 4. No need to check endOfWord.------------
    def startsWith(self, prefix: str) -> bool:
    
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur= cur.children[c]
        return True

    #   checklist of developer---------------------------------
    #   a) is this solving the correct problem?
    #   b) are there issues with this?
    #   c) is there something i dont understand about this solution?
    #   d) is there an edge case im missing?
