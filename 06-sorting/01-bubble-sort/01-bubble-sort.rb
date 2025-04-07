def bubble_sort(numbers)
  n = numbers.length
  (0..n-1).each do |i|
    li = 0
    (1..n-i-1).each do |j|
      li = j if numbers[j] > numbers[li]
    end
    numbers[li], numbers[n-i-1] = numbers[n-i-1], numbers[li]
  end
  numbers
end

print bubble_sort([30, 20, 60, 50, 40])