
# * Time: O(n) Space: O(n)
def stock_span_problem(stocks):
  st, res = [0], [1]
  n = len(stocks)
  for i in range(1, n):
    stock = stocks[i]
    while st and stocks[st[len(st)-1]] <= stock:
      st.pop()
    if st:
      res.append(i-st[len(st)-1])
    else:
      res.append(i+1)
    st.append(i)
  return res


stocks = [60, 10, 20, 40, 35, 30, 50, 70, 65]
res = stock_span_problem(stocks)
print(res)

# [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
