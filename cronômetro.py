from time import sleep
my_time = 1

print('Welcome to your stopwatch!')
sleep(1)

while True:
    my_time += int(input('Enter the time in seconds:'))
    sleep(0.3)
    for x in reversed(range(0, my_time)):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        sleep(1)
    print("Time's up!")
    question = str(input('Do you wanna to continue [Y] or [N]?: ')).upper()
    if question == 'N':
        print('The end!')
        break
