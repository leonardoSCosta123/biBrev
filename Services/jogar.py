
class Jogador :

    id = 0
    saldo = 300
    indice_tabulero = 0

    def __init__ (self,id) :
        self.id = id

class Propriedade():

    id = 0
    valor_venda = 0
    valor_aluguel = 0
    jogador = None

    def __init__ (self, id, valor_venda, valor_aluguel) :
        self.id = id
        self.valor_venda = valor_venda
        self.valor_aluguel = valor_aluguel

from random import randint

class Partida():
    lista_jogadores = []
    lista_propriedade = []
    

    def __init__ (self) :

        indice_jodador = 0
        while indice_jodador < 4 :
            jogador = Jogador(indice_jodador)
            self.lista_jogadores.append(jogador)

            indice_jodador = indice_jodador + 1
            pass 
        
        indice_propriedade = 1
        lista_valores = [dict(venda = 30, aluguel = 5), dict(venda = 50, aluguel = 10), dict(venda = 100, aluguel = 15),
                        dict(venda = 10, aluguel = 2),dict(venda = 40, aluguel = 10),dict(venda = 100, aluguel = 50),
                        dict(venda = 80, aluguel = 25),dict(venda = 100, aluguel = 10),dict(venda = 60, aluguel = 14),
                        dict(venda = 99, aluguel = 7),dict(venda = 77, aluguel = 40),dict(venda = 66, aluguel = 50),
                        dict(venda = 400, aluguel = 60),dict(venda = 788, aluguel = 5),dict(venda = 666, aluguel = 500),
                        dict(venda = 800, aluguel = 500),dict(venda = 100, aluguel = 58),dict(venda = 300, aluguel = 50),
                        dict(venda = 90, aluguel = 50),dict(venda = 40, aluguel = 20)]

        while indice_propriedade <= 20:
            
            propriedade = Propriedade(indice_propriedade,lista_valores[indice_propriedade-1]['venda'],lista_valores[indice_propriedade-1]['aluguel'])
            self.lista_propriedade.append(propriedade)

            indice_propriedade = indice_propriedade + 1 
            pass


    def buscarProximoJogador(self,jogador_atual):

        proximo_jogador = 0
        indice = 0
        for item in self.lista_jogadores :
            if item.id == jogador_atual.id :
                proximo_jogador = indice + 1
                break
            
            indice = indice + 1
        
        if proximo_jogador >= len(self.lista_jogadores) :
            proximo_jogador = 0

        return proximo_jogador
        
    def verifica_compra(self,jogador_atual, propriedade_tabulero):

        if jogador_atual.id == 0 :
            return True

        if jogador_atual.id == 1 :
            if propriedade_tabulero.valor_aluguel > 50 :
                return True
            
            return False

        if jogador_atual.id == 2 :
            saldo_pos_compra = jogador_atual.saldo - propriedade_tabulero.valor_venda

            if saldo_pos_compra >= 80 :
                return True
            
            return False

        if jogador_atual.id == 3 :
            return randint(False,True)