import threading
import redis


class Listener(threading.Thread):
    def __init__(self, channels_sub):
        threading.Thread.__init__(self)
        self.redis = redis.Redis()
        self.pubsub = self.redis.pubsub()
        self.channels_sub = channels_sub
        self.pubsub.subscribe(channels_sub)

    def print_msg(self):
        print 'Listening to {}'.format(*self.channels_sub)

        while True:
            for item in self.pubsub.listen():
                print item['data']


class MsgCalc(Listener):
    def __init__(self, channels_sub, channels_pub):
        super(MsgCalc, self).__init__(channels_sub)
        threading.Thread.__init__(self)
        self.publish = channels_pub

    def work(self, msg):
        try:
            output_message = eval(msg)
        except NameError:
            output_message = 'Input: {}, is not a valid math expression'.format(msg)
        self.redis.publish(self.publish, output_message)

    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == 1:
                continue

            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print self, "unsubscribed and finished"
                break

            else:
                self.work(item['data'])


if __name__ == "__main__":

    client = MsgCalc(['INPUT'], 'OUTPUT')
    client.start()
