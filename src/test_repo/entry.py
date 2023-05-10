import verisynth


def palindrome(original: str) -> bool:
    """
    Return True if `original` is a palindrome (case sensitive), False otherwise.
    """
    return original == original[::-1]


def sum_of_digits(n: int) -> int:
    """
    Return the sum of the digits of `n`.
    """
    sum = 0
    if n < 0:
        n = -n
    while n > 0:
        sum += n % 10
        n //= 10
    return sum