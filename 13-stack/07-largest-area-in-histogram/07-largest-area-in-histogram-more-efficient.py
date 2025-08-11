from collections import deque
import math

def largest_area_in_histogram_more_efficient(bars):
  st, left_smallest = [], []
  n = len(bars)
  for i in range(n):
    bar = bars[i]
    while st and bars[st[len(st)-1]] >= bar:
      st.pop()
    left_smallest.append(st[len(st)-1] if st else -1)
    st.append(i)

  max_area = 0
  dq = deque([])
  for i in range(n-1, -1, -1):
    bar = bars[i]
    while dq and bars[dq[0]] >= bar:
      dq.popleft()
    right_smallest = dq[0] if dq else n
    curr_area = bar * (right_smallest - left_smallest[i] - 1)
    max_area = max(max_area, curr_area)
    dq.appendleft(i)

  return max_area


res = largest_area_in_histogram_more_efficient([6, 2, 5, 4, 1, 5, 6])
print(res)
