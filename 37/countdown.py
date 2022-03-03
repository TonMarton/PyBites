def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    print(start)
    print('time is up') if start == 1 else countdown_recursive(start - 1)
