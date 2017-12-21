from CalcService import Listener

if __name__ == '__main__':
    channel = 'OUTPUT'
    sub = Listener([channel])
    sub.print_msg()
