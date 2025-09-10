import random

def criar_tabuleiro():
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append('.')
        tabuleiro.append(linha)
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, posicao_atual, siglas_jogadores):
    print("   ", end="")
    for j in range(10):
        print(j, end="  ")
    print()

    for i in range(10):
        print(i, end="  ")
        for j in range(10):
            ocupado = False
            for jogador, pos in posicao_atual.items():
                if pos == (i, j):
                    print(siglas_jogadores[jogador], end="  ")
                    ocupado = True
                    break
            if not ocupado:
                print(tabuleiro[i][j], end="  ")
        print()

def definir_jogadores():
    jogadores = {}
    for i in range(2):  
        nome = ''
        while(nome.strip() == '' or nome in jogadores):        
            nome = input(f"Digite o nome do jogador {i+1}: ").strip()
            if(nome.strip() == ''):
                print('O nome não pode ser vazio')
            elif(nome in jogadores):
                     print('Esse nome já foi usado. Escolha outro.')
        jogadores[nome] = 0 
    return jogadores
    
def posicao_inicial(jogadores):
    posicao_atual = {}
    for nome in jogadores.keys():
        posicao_atual[nome] = (0, 0)
    return posicao_atual

def esconder_T(tabuleiro):
    usadas = []
    qtd_T = 0
    while(qtd_T < 5 or qtd_T > 10):
        try:
            qtd_T = int(input('Digite a quantidade de tesouros que serão escondidos no tabuleiro (5 a 10): '))
            if qtd_T < 5 or qtd_T > 10:
                print('A quantidade de tesouros deve ser entre 5 e 10!')
        except ValueError:
            print('Você deve digitar um número válido!')

    for i in range(qtd_T):
        linha, coluna = verificar_posicao(usadas)
        tabuleiro[linha][coluna] = "T"
        usadas.append((linha, coluna))
    return usadas, tabuleiro

def esconder_A(usadas, tabuleiro):      
    qtd_A = 0
    while(qtd_A < 5 or qtd_A > 10):
        try:
            qtd_A = int(input('Digite a quantidade de armadilhas que serão escondidas no tabuleiro (5 a 10): '))
            if qtd_A < 5 or qtd_A > 10:
                print('A quantidade de armadilhas deve ser entre 5 e 10!')
        except ValueError:
            print('Você deve digitar um número válido!')

    for i in range(qtd_A):
        linha, coluna = verificar_posicao(usadas)
        tabuleiro[linha][coluna] = "A"
        usadas.append((linha, coluna))
    return tabuleiro
         
def verificar_posicao(usadas):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        if (linha, coluna) not in usadas:
            return linha, coluna
        
def exibir_regras():
    print("\n*-- REGRAS DO JOGO: CAÇA AO TESOURO --*")
    print("- Tabuleiro 10x10. Jogadores começam na posição (0,0)")
    print("- Tesouros valem +10 pontos (símbolo: T)")
    print("- Armadilhas tiram -5 pontos (símbolo: A)")
    print("- Cada jogador começa com 10 pontos")
    print("- Serão 10 rodadas (5 para cada jogador)")
    print("- Em cada rodada, rola-se um dado (1 a 6) e o jogador escolhe a direção")
    print("- Quem tiver mais pontos no final, vence!\n")

def start():
    rodada = 0
    return rodada

def verificar_rodada(rodada):
    return rodada < 10
    
def contador(jogadores, liberacao):
    if(liberacao == False):
        print('\n*-- FIM DO JOGO --*')
        for jogador, pontos in jogadores.items():
            print(f'{jogador}: {pontos} pontos')

        maior_pontuacao = -9999
        for jogador, pontos in jogadores.items():
            if pontos > maior_pontuacao:
                maior_pontuacao = pontos
                vencedor = jogador
        print(f'\nVencedor: {vencedor} com {maior_pontuacao} pontos!')

def mover(pos, dado, direcao):
    x, y = pos
    if direcao == "cima":
        x -= dado
    elif direcao == "baixo":
        x += dado
    elif direcao == "esquerda":
        y -= dado
    elif direcao == "direita":
        y += dado

    if x < 0:
        x = 0
    elif x > 9:
        x = 9

    if y < 0:
        y = 0
    elif y > 9:
        y = 9

    return (x, y)


def dado(liberacao, rodada, jogadores, posicao_atual):
    if liberacao:
        nomes = list(jogadores.keys())
        jogador = nomes[rodada % 2]

        print(f"\nVez do jogador: {jogador}")
        dado_valor = random.randint(1, 6)
        print(f"🎲 O dado rolou e saiu: {dado_valor}")

        direcao = input("Digite a direção (cima, baixo, esquerda, direita): ").lower()

        pos_atual = posicao_atual[jogador]
        nova_posicao = mover(pos_atual, dado_valor, direcao)

        rodada += 1
        return nova_posicao, rodada, jogador

def atualizar_posicao(posicao_atual, nova_posicao, jogador, tabuleiro):
    linha_antiga, coluna_antiga = posicao_atual[jogador]
    tabuleiro[linha_antiga][coluna_antiga] = "."

    posicao_atual[jogador] = nova_posicao

    return posicao_atual, tabuleiro

def gerar_sigla(nome, siglas_usadas ):
    for letra in nome.upper():
        if letra not in siglas_usadas:
            return letra

def main():
    repetir = 'SIM'
    while(repetir == 'SIM'):
        exibir_regras()
        tabuleiro = criar_tabuleiro()
        jogadores = definir_jogadores()
        siglas_jogadores = {}
        siglas_usadas = []
        for nome in jogadores:
            sigla = gerar_sigla(nome, siglas_usadas)
            siglas_usadas.append(sigla)
            siglas_jogadores[nome] = sigla

        posicao_atual = posicao_inicial(jogadores)

        usadas, tabuleiro = esconder_T(tabuleiro)
        tabuleiro = esconder_A(usadas, tabuleiro)

        rodada = start()

        while verificar_rodada(rodada):
            mostrar_tabuleiro(tabuleiro, posicao_atual, siglas_jogadores)

            input(f"\nRodada {rodada+1} - Pressione ENTER para jogar os dados...")

            nova_posicao, rodada, jogador = dado(True, rodada, jogadores, posicao_atual)
            posicao_atual, tabuleiro = atualizar_posicao(posicao_atual, nova_posicao, jogador, tabuleiro)

            linha, coluna = nova_posicao
            if tabuleiro[linha][coluna] == "T":
                jogadores[jogador] += 10
                print(f"🎉 {jogador} encontrou um TESOURO! +10 pontos")
            elif tabuleiro[linha][coluna] == "A":
                jogadores[jogador] -= 5
                print(f"💀 {jogador} caiu em uma ARMADILHA! -5 pontos")

        contador(jogadores, False)
        repetir = input('Jogar denovo? \n').upper()
    print('\nObrigado por jogar!\n')

# Principal
main()