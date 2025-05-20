def sum_of_digits(d: int) -> int:
  if d == 0:
    return 0
  curr_digit = d % 10
  return curr_digit + sum_of_digits(d // 10)

print(sum_of_digits(253))
print(sum_of_digits(984))