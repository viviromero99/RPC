import rpyc
import time

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

    def exposed_soma(self, array):
        start = time.time() 
        soma_total = 0
        for value in array:
            soma_total += value

        end = time.time()
        print(end-start)
        return soma_total

    def get_question(self):
        return "Qual é a cor do cavalo branco de Napoleão?"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18866, protocol_config={'allow_public_attrs': True,})
    print('started server')
    t.start()