
def decimal_to_binary(dec)
  res = ""
  while dec > 0
    res = (dec % 2).to_s + res
    dec = dec / 2
  end
  res
end

puts decimal_to_binary 2
puts decimal_to_binary 7