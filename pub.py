import redis

if __name__ == '__main__':
    channel = 'INPUT'
    r = redis.Redis()
    print('Welcome to {}'.format(channel))
    print('Enter a valid math expression (4+5 e.g.)\nType EXIT to terminate publisher ' \
          '\nType KILL to terminate pulisher and subscriber\n *****')
    while True:
        message = raw_input('Expression: ')

        if message.lower() == 'exit':
            break

        r.publish(channel, message)
        if message.lower() == 'kill':
            break
