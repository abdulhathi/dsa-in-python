from TrieNode import TrieNode


def delete_trie(trie: TrieNode, word):
  st = []
  for c in word:
    if c not in trie.childs:
      return False
    st.append(trie)
    trie = trie.childs[c]

  if not trie.isEndOfWord:
    return False

  trie.isEndOfWord = False

  for c in word[::-1]:
    trie = st.pop()
    if len(trie.childs[c].childs) > 0:
      return True
    del trie.childs[c]

  return True


trie = TrieNode()
for word in ['abdul', 'ab', 'hathi', 'mohamed', 'aysha']:
  trie.insert(word)

print(delete_trie(trie, 'ab'))

print('a' in trie.childs)
print('b' in trie.childs['a'].childs)

print(trie.childs['a'].childs['b'].childs)
