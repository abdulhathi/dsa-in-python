def reverse_a_string(s)
  l, r = 0, s.length - 1
  while l < r
    s[l], s[r] = s[r], s[l]
    l, r = l+1, r-1
  end
  s
end

puts reverse_a_string 'abdul'

puts reverse_a_string 'hathi'