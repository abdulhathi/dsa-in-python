const separate_even_and_odd = (numbers: number[]) => {
  return numbers.reduce<[number[], number[]]>(
    (acc, curr) => {
      const [even, odd] = acc
      if (curr % 2 === 0) even.push(curr)
      else odd.push(curr)
      return [even, odd]
    },
    [[], []]
  )
}

console.log(separate_even_and_odd([1, 2, 3, 4, 5]))
