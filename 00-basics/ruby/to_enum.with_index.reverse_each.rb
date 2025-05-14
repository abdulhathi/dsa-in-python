nums = [10,20,30,40]
nums.to_enum.with_index.reverse_each do |num, index|
  puts "#{num} #{index}"
end