from settings import r

if __name__ == '__main__':
    channel = 'OUTPUT'

    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print 'Listening to {channel}'.format(**locals())

    while True:
        for item in pubsub.listen():
            print item['data']