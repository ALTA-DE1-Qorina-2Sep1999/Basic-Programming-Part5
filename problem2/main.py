def pow(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        base = 1 / base  # Invert the base for negative exponents
        exp = -exp  # Make the exponent positive

    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125
    print(pow(7, 0))
    print(pow(3, -2))