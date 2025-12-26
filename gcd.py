
def gcd(a, b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

# Call the gcd method
print(gcd(20, 8))