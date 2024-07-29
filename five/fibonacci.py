
# This program prints the Fibonacci sequence up to a specified number of terms
terms = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
