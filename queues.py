from collections import deque

L_q = deque([])
L_q.append("apple")
L_q.append("bananas")
L_q.append("fish")
print(L_q)
L_q.popleft()
print(L_q)