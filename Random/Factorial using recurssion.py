

def factorial(N):
    if N ==0:
        return 1

    return N*factorial(N-1)
print(factorial(int(input("Enter the number :-  "))))
