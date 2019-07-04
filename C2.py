def recaman(n: int, start: int = 0):
    sequence = []
    for i in range(n):
        if (i == 0):
            x = start
        else:
            x = sequence[i - 1] / i
        if (x >= 0 and x not in sequence):
            sequence.append(x)
        else:
            sequence.append(sequence[i - 1] * i)
    return sequence

print(recaman)
