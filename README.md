# 🎲🏴‍☠️ Caça ao Tesouro - Jogo em Python 🐍

Este é um jogo de **Caça ao Tesouro** desenvolvido em Python, jogado por **2 jogadores** em um tabuleiro **10x10**.  
O objetivo é encontrar tesouros escondidos e evitar armadilhas para acumular a maior pontuação ao final das rodadas.

---

## 🚀 Como jogar!
*-- REGRAS DO JOGO: CAÇA AO TESOURO --*
- Tabuleiro 10x10. Jogadores começam na posição (0,0)
- Tesouros valem +10 pontos (símbolo: T)
- Armadilhas tiram -5 pontos (símbolo: A)
- Cada jogador começa com 0 pontos
- Serão 10 rodadas (5 para cada jogador)
- Em cada rodada, rola-se dois dados: define a posição
- Quem tiver mais pontos no final, vence!

Rodada 1 - Pressione ENTER para jogar os dados...
Jogador1 encontrou um TESOURO! +10 pontos
Rodada 2 - Pressione ENTER para jogar os dados...
Jogador2 caiu em uma ARMADILHA! -5 pontos

##⚙️ Funcionalidades
###🗺️ Tabuleiro
- **`criar_tabuleiro()`** → cria o tabuleiro 10x10 vazio.
- **`mostrar_tabuleiro()`** → exibe o tabuleiro com jogadores e elementos.
- **`esconder_T()`** → esconde os tesouros no tabuleiro.
- **`esconder_A()`** → esconde as armadilhas no tabuleiro.
- **`verificar_posicao()`** → garante que não haja sobreposição de T e A.

###🧑‍🤝‍🧑 Jogadores
- **`definir_jogadores()`** → cadastra os dois jogadores.
- **`gerar_sigla()`** → gera uma sigla única para cada jogador.
- **`posicao_inicial()`** → define a posição inicial (0,0) para os jogadores.

###🎲 Movimento e Rodadas
- **`dado()`** → sorteia o valor do dado, mostra de quem é a vez e pede a direção de movimento.
- **`mover()`** → movimenta o jogador conforme dado e direção, respeitando os limites do tabuleiro.
- **`atualizar_posicao()`** → atualiza a posição no tabuleiro.
- **`exibir_regras()`** → mostra as regras do jogo no terminal.
- **`start()`** e **`verificar_rodada()`** → controlam a quantidade de rodadas.
###🏆 Finalização
- **`contador()`** → mostra a pontuação final de cada jogador e o vencedor.
- **`main()`** → executa o jogo principal.
