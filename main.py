
# Fibonacci Generator

def fibo_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    try:
        n = int(input("Enter how many Fibonacci numbers you want: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci Series:")
            print(*fibo_gen(n))  
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
