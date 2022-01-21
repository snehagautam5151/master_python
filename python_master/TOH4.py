def TOH(n, A, B, C):
    print("TOH( ", n, A, B, C, " called")
    if n > 0:
        # move tower of size n - 1 to B:
        TOH(n - 1, A, C, B)        
        if A[0]:
            disk = A[0].pop()
            print("moving " + str(disk) + " from " + A[1] + " to " + C[1])
            C[0].append(disk)
        
        TOH(n - 1, B, A, C)
        
A = ([5,4,3,2,1], "A")
C = ([], "C")
B = ([], "B")
TOH(len(A[0]),A,B,C)

print(A, B, C)