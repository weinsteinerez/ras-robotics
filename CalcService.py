from settings import r

import threading


class Listener(threading.Thread):
    def __init__(self, r, channels_sub, channels_pub):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels_sub)
        self.publish = channels_pub

    def work(self, msg):
        try:
            output_message = eval(msg)
            self.redis.publish(self.publish, output_message)
        except TypeError:
            print 'Input: {}, is not a valid math expression'.format(msg)

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
    r = r
    client = Listener(r, ['INPUT'], 'OUTPUT')
    client.start()

# if __name__ == '__main__':
#     input_channel = 'INPUT'
#     output_channel = 'OUTPUT'
#
#     pubsub = r.pubsub()
#     pubsub.subscribe(input_channel)
#
#     print 'Listening to {input_channel} and publishing in {output_channel}'.format(**locals())
#
#     while True:
#         for item in pubsub.listen():
#             math_exp = item['data']
#             try:
#                 output_message = eval(math_exp)
#                 r.publish(output_channel, output_message)
#             except TypeError:
#                 print 'Input: {}, is not a valid math expression'.format(math_exp)