import snoop 

@snoop
def factorial(x):
    return 1 if x == 1 else (x * factorial(x-1))


if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")