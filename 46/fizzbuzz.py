def fizzbuzz(num):
    string: str = ''
    if num % 3 == 0:
        string = 'Fizz'
    if num % 5 == 0:
        string += ' Buzz'

    if string != '':
        return string.strip()
    return num

# smarter and generalized solution from forum
def fizzbuzz_smart(num, *, coprimes = {3: "Fizz", 5: "Buzz"}):
    out = [word for p, word in coprimes.items() if num % p == 0]
    if out:
        return ' '.join(out)
    else:
        return num