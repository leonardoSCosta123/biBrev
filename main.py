
from Services import jogar
from random import randint

# vars para o relatório
qtd_partida_time_out = 0
qtd_turno_partida = 0
qtd_vitoria_impulsivo = 0
qtd_vitoria_exigente = 0
qtd_vitoria_cauteloso = 0
qtd_vitoria_aleatorio = 0

simulacoes = 300
indice_simulacao = 0

rodadas = 1000
indice_rodada = 0

volta_completa = 20
indice_volta_completa = 1

partida = jogar.Partida()

while indice_simulacao < simulacoes :

    indice_jogador = 0
    indice_rodada = 0

    while indice_rodada < rodadas :
        
        if len(partida.lista_jogadores) == 2 :
            print("ok")

        if len(partida.lista_jogadores) == 1 :
            jogador_atual = partida.lista_jogadores[0]
            if jogador_atual.id == 0 :
                qtd_vitoria_impulsivo = qtd_vitoria_impulsivo + 1

            if jogador_atual.id == 1 :
                qtd_vitoria_exigente = qtd_vitoria_exigente + 1

            if jogador_atual.id == 2 :
                qtd_vitoria_cauteloso = qtd_vitoria_cauteloso + 1

            if jogador_atual.id == 3 :
                qtd_vitoria_aleatorio = qtd_vitoria_aleatorio + 1

            break

        qtd_turno_partida = qtd_turno_partida + 1

        jogador_atual = partida.lista_jogadores[indice_jogador]
        dado = randint(1,6)
        jogador_atual.indice_tabulero = jogador_atual.indice_tabulero + dado

        if jogador_atual.indice_tabulero >= 20 :
            jogador_atual.indice_tabulero = 1
            jogador_atual.saldo = jogador_atual.saldo + 100
            
            indice_jogador = partida.buscarProximoJogador(jogador_atual)

            indice_rodada = indice_rodada + 1

            if indice_rodada == rodadas :
                qtd_partida_time_out = qtd_partida_time_out + 1

            continue

        propriedade_tabulero = partida.lista_propriedade[jogador_atual.indice_tabulero - 1]

        vai_comprar = partida.verifica_compra(jogador_atual ,propriedade_tabulero)
        
        valor_restante_apos_aluguel = jogador_atual.saldo - propriedade_tabulero.valor_aluguel
        if jogador_atual.saldo == 0 or valor_restante_apos_aluguel < 0 and propriedade_tabulero.jogador != None:
            indice_jogador = partida.buscarProximoJogador(jogador_atual)
            partida.lista_jogadores.remove(jogador_atual)

            print("\njogador removido"+str(jogador_atual.id))

            if len(partida.lista_jogadores) == 1 :
                continue

            jogador_aux = partida.lista_jogadores[indice_jogador - 1]
            indice_jogador = partida.buscarProximoJogador(jogador_aux)

            for item in partida.lista_propriedade :
                if item.jogador != None and item.jogador.id == jogador_atual.id :
                    item.jogador = None

            indice_rodada = indice_rodada + 1

            if indice_rodada == rodadas :
                qtd_partida_time_out = qtd_partida_time_out + 1

            continue
        
        valor_restante_apos_compra = jogador_atual.saldo - propriedade_tabulero.valor_venda
        saldo_repasse = 0
        jogador_repasse = None

        if vai_comprar == True and valor_restante_apos_compra >= 0 and propriedade_tabulero.jogador == None:
            jogador_atual.saldo = valor_restante_apos_compra
            propriedade_tabulero.jogador = jogador_atual
        else :
            if propriedade_tabulero.jogador != None and propriedade_tabulero.jogador.id != jogador_atual.id:
                saldo_repasse = propriedade_tabulero.valor_aluguel
                jogador_repasse = propriedade_tabulero.jogador

                jogador_atual.saldo = valor_restante_apos_aluguel

        if saldo_repasse > 0 :
            for itemJogador in partida.lista_jogadores :
                if itemJogador.id == jogador_repasse.id :
                    jogador_cobrador_aluguel = itemJogador
                    jogador_cobrador_aluguel.saldo = jogador_cobrador_aluguel.saldo + saldo_repasse
                    break

        indice_jogador = partida.buscarProximoJogador(jogador_atual)

        indice_rodada = indice_rodada + 1

        if indice_rodada == rodadas :
            qtd_partida_time_out = qtd_partida_time_out + 1

        pass

    indice_simulacao = indice_simulacao + 1
    pass

print(" Quantidade de partidas que acabaram em time out : "+ str(qtd_partida_time_out))
print("\n Turno médio por partida : "+ str(qtd_turno_partida/indice_simulacao))

perc_jogador_impulsivo = 0
perc_jogador_exigente = 0
perc_jogador_cauteloso = 0
perc_jogador_aleatorioo = 0

if qtd_vitoria_impulsivo > 0 :
    perc_jogador_impulsivo = (qtd_vitoria_impulsivo / indice_simulacao) * 100

if qtd_vitoria_exigente > 0 :
    perc_jogador_exigente = (qtd_vitoria_exigente / indice_simulacao) * 100

if qtd_vitoria_cauteloso > 0 :
    perc_jogador_cauteloso = (qtd_vitoria_cauteloso / indice_simulacao) * 100

if qtd_vitoria_aleatorio > 0 :
    perc_jogador_aleatorioo = (qtd_vitoria_aleatorio / indice_simulacao) * 100


print("\n Percentual de vitórias jogador impulsivo : "+ str( perc_jogador_impulsivo ) + "%")
print("\n Percentual de vitórias jogador exigente : "+ str(perc_jogador_exigente) + "%")
print("\n Percentual de vitórias jogador cauteloso : "+ str(perc_jogador_cauteloso) + "%")
print("\n Percentual de vitórias jogador aleatório : "+ str(perc_jogador_aleatorioo) + "%")


lista_vitorias = [dict(comport = "impsulvio", qtd = qtd_vitoria_impulsivo),
                dict(comport = "Exigente" ,qtd = qtd_vitoria_exigente) ,
                dict(comport = "Cauteloso", qtd = qtd_vitoria_cauteloso), 
                dict(comport = "Cauteloso",qtd = qtd_vitoria_aleatorio ) ]


maior = max(range(len(lista_vitorias)), key=lambda index: lista_vitorias[index]['qtd'])

print("\n\n Comportamento mais vitorioso : "+ str( lista_vitorias[maior]['comport'] ))







