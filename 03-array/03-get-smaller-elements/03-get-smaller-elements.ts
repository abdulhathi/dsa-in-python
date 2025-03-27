const get_smaller_elements = (numbers: number[], key: number) => {
  return numbers.reduce<number[]>((acc, curr) => {
    if (curr < key) acc.push(curr)
    return acc
  }, [])
}

console.log(get_smaller_elements([1, 2, 3, 4, 5], 4))
