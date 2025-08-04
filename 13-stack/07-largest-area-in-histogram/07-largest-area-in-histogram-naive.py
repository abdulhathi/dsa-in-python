
# * Time: O(n^2) Space: O(1)
def largest_area_in_histogram(bars):
  n = len(bars)
  max_area = 0
  for i in range(n):
    bar = bars[i]
    curr_area = bar
    for j in range(i-1, -1, -1):
      if bars[j] >= bar:
        curr_area += bar
      else:
        break
    for k in range(i+1, n):
      if bars[k] >= bar:
        curr_area += bar
      else:
        break
    max_area = max(max_area, curr_area)
  return max_area


res = largest_area_in_histogram([6, 2, 5, 4, 1, 5, 6])
print(res)
