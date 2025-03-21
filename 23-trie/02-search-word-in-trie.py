from TrieNode import TrieNode

def search_word_in_trie(trie: TrieNode, word):
  for c in word:
    if c not in trie.childs:
      return False
    trie = trie.childs[c]
  
  return trie.isEndOfWord


trie = TrieNode()
trie.insert('geeks')
trie.insert('geek')
trie.insert('put')

res = search_word_in_trie(trie, 'put')
print(res)

res = search_word_in_trie(trie, 'puts')
print(res)