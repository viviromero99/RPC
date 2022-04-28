import rpyc
class MyService(rpyc.Service):
    def on_connect(self, conn):
        print('connected')
        pass
    def on_disconnect(self, conn):
        print('disconnected')
        pass

    def exposed_get_answer(self):
        return 42
    exposed_the_real_answer_though = 43

    def exposed_soma(self, array):
        soma_total = 0
        for value in array:
            soma_total += value
        return soma_total

    def get_question(self):
        return "Qual é a cor do cavalo branco de Napoleão?"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, "localhost", port=18861)
    print('started server')
    t.start()