const reverse_a_string = (s: string) => {
  const str = [...Array(s.length)].map(() => '')
  let [l, r] = [0, s.length - 1]
  while (l <= r) {
    str[l] = s[r]
    str[r] = s[l]
    l = l + 1
    r = r - 1
  }
  return str.join('')
}

console.log(reverse_a_string('abdul'))
console.log(reverse_a_string('hathi'))

console.log(reverse_a_string('aysha'))
