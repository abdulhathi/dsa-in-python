
class TrieNode:
  def __init__(self):
    self.childs = {}
    self.isEndOfWord = False

  def insert(self, word):
    trie = self
    for c in word:
      if c not in trie.childs:
        trie.childs[c] = TrieNode()
      trie = trie.childs[c]
    trie.isEndOfWord = True
