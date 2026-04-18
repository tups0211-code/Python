A = [ 
[1, 2], 
[3, 4] 
] 
B = [ 
[5, 6], 
[7, 8] 
] 
C = [ 
[0, 0], 
[0, 0] 
] 
for i in range(2): 
  for j in range(2): 
    C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] 
print("Multiplication of two matrices is :") 
for row in C: 
  print(row)