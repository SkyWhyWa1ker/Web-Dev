n = int(input().strip())

if (n % 2):
    print('Weird')
elif not n % 2 and 2 <= n <= 5:
    print('Not Weird')
elif not n % 2 and 6 <= n <= 20:
    print('Weird')
elif not n % 2 and n > 20:
    print('Not Weird')
