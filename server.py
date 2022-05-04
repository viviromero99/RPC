import rpyc
import time
import copy

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print('connected')
        pass
    def on_disconnect(self, conn):
        print('disconnected')
        pass

    def exposed_get_answer(self):
        print("conectouu")
        return 42
    exposed_the_real_answer_though = 43

    def exposed_soma(self, a):
        array = copy.deepcopy(a)

        # print("started processing")
        soma_total = 0

        start = time.time()
        i = 0
        array_len = len(array)
        while (i < array_len):
            print("running sum for ", array[i])
            soma_total += array[i]
            i += 1

        end = time.time()
        print(end-start)
        return soma_total

    def get_question(self):
        return "Qual é a cor do cavalo branco de Napoleão?"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18866, protocol_config={'allow_public_attrs': True, 'allow_pickle': True})
    print('started server')
    t.start()