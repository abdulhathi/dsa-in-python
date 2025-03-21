from TrieNode import TrieNode


def insert_trie(trie: TrieNode, word):
  for c in word:
    if c not in trie.childs:
      trie.childs[c] = TrieNode()
    trie = trie.childs[c]
  trie.isEndOfWord = True


trie = TrieNode()
insert_trie(trie, 'geeks')
insert_trie(trie, 'geek')

print(trie.childs['g'].childs['e'].childs['e'].childs['k'].isEndOfWord)

print(trie.childs['g'].childs['e'].childs['e'].childs['k'].childs['s'].isEndOfWord)
