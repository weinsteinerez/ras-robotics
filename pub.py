import redis

if __name__ == '__main__':
    channel = 'INPUT'
    r = redis.Redis()
    print('Welcome to {channel}'.format(**locals()))

    while True:
        message = raw_input('Enter a message: ')

        if message.lower() == 'exit':
            break

        r.publish(channel, message)