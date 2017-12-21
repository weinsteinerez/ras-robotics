import redis

if __name__ == '__main__':
    channel = 'INPUT'
    r = redis.Redis()
    print('Welcome to {channel}'.format(**locals()))
    print 'Enter a valid math expression (4+5 e.g.)'
    while True:
        message = raw_input('Expression: ')

        if message.lower() == 'exit':
            break

        r.publish(channel, message)