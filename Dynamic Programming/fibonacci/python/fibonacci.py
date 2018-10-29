def fib(n):
    if n == 0: return 0

    # Initial values of fibonacci series
    f = [1, 1]

    for i in range(2, n):
        # Use modulus to switch array indexes
        f[i%2] = f[0] + f[1]

    return f[(n+1)%2]

startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib_with_recursive(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib_with_recursive, range(startNumber, endNumber))
        
n = 9
print(fib(n))
