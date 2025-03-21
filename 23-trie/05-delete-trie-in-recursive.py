from TrieNode import TrieNode


def delete_trie(trie: TrieNode, word):

  def delete(trie: TrieNode, i):
    if i == len(word):
      trie.isEndOfWord = False
      print(trie.childs, trie.isEndOfWord)
      return False if len(trie.childs) > 0 else True
    char = word[i]
    res = delete(trie.childs[char], i+1)
    if res:
      print(char, trie.childs, trie.isEndOfWord)
      if trie.childs[char].isEndOfWord:
        return False
      del trie.childs[char]
      if len(trie.childs) > 0:
        return False

    return res

  return delete(trie, 0)


trie = TrieNode()
for word in ['abdul', 'abdullah']:
  trie.insert(word)

res = delete_trie(trie, 'abdullah')
print(res)

print(trie.childs['a'].childs['b'].childs['d'].childs['u'].childs['l'].isEndOfWord)
