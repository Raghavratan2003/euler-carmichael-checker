# GCD function using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Euler's Totient Function φ(n)
def euler_totient(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

# Check if n is a Carmichael number (from known list)
def is_carmichael(n):
    carmichael_list = [561, 1105, 1729, 2465, 2821, 6601,
                       8911, 10585, 15841, 29341, 41041,
                       46657, 52633, 62745, 63973]
    return n in carmichael_list

# Check Euler's Theorem for a given number
def check_euler_theorem(n):
    phi = euler_totient(n)
    for a in range(1, n):
        if gcd(a, n) == 1:
            if pow(a, phi, n) != 1:
                print(f"Fails for a = {a}")
                return False
    return True

# Main Program
try:
    n = int(input("Enter a value of n (n > 1): "))
    if n <= 1:
        print("n should be greater than 1.")
    else:
        if is_carmichael(n):
            print(f"{n} is a Carmichael number.")

        result = check_euler_theorem(n)
        if result:
            print(f"Euler's Theorem holds for n = {n}")
        else:
            print(f"Euler's Theorem fails for n = {n}")

except ValueError:
    print("Please enter a valid integer.")
