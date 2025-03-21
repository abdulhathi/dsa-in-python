from TrieNode import TrieNode


def search_prefix(trie: TrieNode, prefix):
  for c in prefix:
    if c not in trie.childs:
      return False
    trie = trie.childs[c]

  return True


trie = TrieNode()
for word in ['abdul','hathi','mohamed','aysha']:
  trie.insert(word)

print(search_prefix(trie, 'abdulhathi'))
print(search_prefix(trie, 'abd'))
print(search_prefix(trie, 'ab'))
