def fibonacci():
    """
    This function generates the Fibonacci sequence up to the 100th term.
    """
    fib_sequence = [0, 1]
    for i in range(2, 100):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence