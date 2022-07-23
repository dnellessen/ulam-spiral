
_primenums = []

def isprime(num: int):
    '''
    Check if a number is prime.

    Parameters
    ----------
    num : int
        The number to check.

    Returns
    --------
    prime : bool

    Exapmles
    --------
    >>> isprime(28)
    >>> False
    >>> isprime(17)
    >>> True
    '''

    global _primenums
    for prime in _primenums:
        if num % prime == 0:
            return False
    _primenums.append(num)
    return True