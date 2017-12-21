from settings import r

if __name__ == '__main__':
    channel = 'INPUT'

    print('Welcome to {channel}'.format(**locals()))

    while True:
        message = raw_input('Enter a message: ')

        if message.lower() == 'exit':
            break

        r.publish(channel, message)