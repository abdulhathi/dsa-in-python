const balanced_parenthesis = (parenthesis: string) => {
  const st = []
  const dic = { '}': '{', ')': '(', ']': '[' }

  for (const c of parenthesis) {
    if (c in dic) {
      if (st.length === 0 || dic[c] !== st.pop())
        return false 
    }
    else
      st.push(c)
  }

  return st.length === 0
}

console.log(balanced_parenthesis('({[]})'))
console.log(balanced_parenthesis('((())'))
console.log(balanced_parenthesis('([)]'))
console.log(balanced_parenthesis('{}([()])'))
console.log(balanced_parenthesis('(()))'))