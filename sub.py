# from settings import r
import redis
from CalcService import Listener
if __name__ == '__main__':
    channel = 'OUTPUT'
    sub = Listener([channel])
    sub.print_msg()
    # pubsub = r.pubsub()
    # pubsub.subscribe(channel)

    # print 'Listening to {channel}'.format(**locals())
    #
    # while True:
    #     for item in pubsub.listen():
    #         print item['data']