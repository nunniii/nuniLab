from _collections import deque  #Classe para tornar filas mais eficientes

queue = deque(["Eric", "John", "Michael"])
print(type(queue))

queue.append("Terry")   # Terry chega
print(queue)

queue.append("Graham")  # Graham chega
print(queue)

queue.popleft()         # O primeiro a chegar agora sai
print(queue)

queue.popleft()         # O segundo a chegar agora parte
print(queue)
print(queue)