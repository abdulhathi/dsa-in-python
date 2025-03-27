const average_of_a_list = (numbers: number[]) => {
  let sum = 0
  for (const num of numbers) sum += num
  return Math.floor(sum / numbers.length)
}

console.log(average_of_a_list([10, 20, 30]))
