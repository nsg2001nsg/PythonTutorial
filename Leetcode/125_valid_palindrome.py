def isPalin(str1):
    str1 = "".join(ch for ch in str1.lower() if ch.isalnum())
    return str1 == str1[::-1]


print(isPalin("A man, a plan, a canal: Panama"))
print(isPalin("race a car"))
print(isPalin(" "))
