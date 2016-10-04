def exponent(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    else:
        if n % 2 != 0:
            return exponent(a,n/2) * exponent (a,n/2) * a
        else:
            return exponent(a,n/2) * exponent (a,n/2)
