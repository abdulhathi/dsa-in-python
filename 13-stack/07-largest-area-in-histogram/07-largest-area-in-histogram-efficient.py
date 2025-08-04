from collections import deque


def largest_area_in_histogram(bars):
  # * Left smallest value position
  st, left_smallest = [], []
  n = len(bars)
  for i in range(n):
    bar = bars[i]
    while st and bars[st[len(st)-1]] >= bar:
      st.pop()
    if st:
      left_smallest.append(st[len(st)-1])
    else:
      left_smallest.append(-1)
    st.append(i)

  # * Right smallest value position
  q, right_smallest = deque([]), deque([])
  for i in range(n-1, -1, -1):
    bar = bars[i]
    while q and bars[q[0]] >= bar:
      q.popleft()
    if q:
      right_smallest.appendleft(q[0])
    else:
      right_smallest.appendleft(n)
    q.appendleft(i)

  max_area = 0
  for i in range(n):
    bar = bars[i]
    curr_area = bar * (right_smallest[i] - left_smallest[i] - 1)
    max_area = max(max_area, curr_area)
  return max_area


res = largest_area_in_histogram([6, 2, 5, 4, 1, 5, 6])
print(res)

res = largest_area_in_histogram([2, 5, 1])
print(res)