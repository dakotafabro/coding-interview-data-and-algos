# real-world application/visualization - factorial

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

int = 3
print(f"Factorial {int} is {factorial(int)}")