def fib(num : int) -> int :
    return num if (num <= 1) else fib(num - 1) + fib(num - 2)

print(fib(int(input("Enter a number :"))))