def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 1000))))
