def palin(n):
    # way 1
    # n = str(n)
    # i, c = 0, -1
    # while i <= (len(n)//2):
    #     if n[i] != n[c]:
    #         return False
    #     i += 1
    #     c -= 1
    # return True

    # way 2
    # n = str(n)
    # if n == n[::-1]:
    #     return True
    # return False

    # way 3 (for integers)
    # res = 0
    # q = n
    # while q != 0:
    #     q, r = (q // 10), (q % 10)
    #     res = (res * 10) + r
    #
    # return res == n

    # way 4
    # while n:  # 109030901
    #     q = n  # 109030901
    #     r = n % 10  # 1
    #     divisor = 1  # 1
    #     while q >= 10:
    #         q = q // 10  # 1
    #         divisor *= 10  # 100000000
    #
    #     if q != r:
    #         return False
    #
    #     n = (n % divisor) // 10  # 0903090
    #
    # return True

    # way 5
    divisor = 1
    while n // divisor >= 10:
        divisor *= 10

    while n:
        first = n // divisor
        last = n % 10

        if first != last:
            return False

        # Remove first and last digits
        n = (n % divisor) // 10
        print(n)
        divisor = divisor // 100

    return True


# print(palin("malayalam"))
print(palin(123454321))
print(palin(123456789))
# print(palin("andugundu"))