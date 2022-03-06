def freq_digit(num: int) -> int:
    digits = []
    counts = []
    for d in str(num):
        if d in digits:
            counts[digits.index(d)] += 1
        else:
            digits.append(d)
            counts.append(1)
    return int(digits[counts.index(max(counts))])
    