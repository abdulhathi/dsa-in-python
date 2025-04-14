#* First in First out

q = []

q.append(10)
q.append(20)
q.append(30)

print q
puts

print q.shift
puts
print q.shift
puts


q1, q2 = [], []

q1.append(10)

q1, q2 = q2, q1
q1.append(20)
while q2.length > 0
  q1.append(q2.shift)
end

print q1, q2