# 🎲🏴‍☠️ Caça ao Tesouro - Jogo em Python 🐍

Este é um jogo de **Caça ao Tesouro** desenvolvido em Python, jogado por **2 jogadores** em um tabuleiro **10x10**.  
O objetivo é encontrar tesouros escondidos e evitar armadilhas para acumular a maior pontuação ao final das rodadas.

---

## 🚀 Como jogar!
*-- REGRAS DO JOGO: CAÇA AO TESOURO --*
- Tabuleiro 10x10. Jogadores começam na posição (0,0)
- Tesouros valem +10 pontos (símbolo: T)
- Armadilhas tiram -5 pontos (símbolo: A)
- Cada jogador começa com 10 pontos
- Serão 20 rodadas (10 para cada jogador)
- Em cada rodada, rola-se dois dados: define a posição
- Quem tiver mais pontos no final, vence!

Rodada 1 - Pressione ENTER para jogar os dados...
Jogador1 encontrou um TESOURO! +10 pontos
Rodada 2 - Pressione ENTER para jogar os dados...
Jogador2 caiu em uma ARMADILHA! -5 pontos

##⚙️ Funcionalidades
criar_tabuleiro() → cria o tabuleiro 10x10 vazio.
mostrar_tabuleiro() → exibe o tabuleiro com jogadores e elementos.
definir_jogadores() → cadastra os dois jogadores.
gerar_sigla() → gera uma sigla única para cada jogador.
posicao_inicial() → define a posição inicial (0,0) para os jogadores.
esconder_T() → esconde os tesouros no tabuleiro.
esconder_A() → esconde as armadilhas no tabuleiro.
verificar_posicao() → garante que não haja sobreposição de T e A.
exibir_regras() → mostra as regras do jogo no terminal.
start() e verificar_rodada() → controlam as rodadas.
dado() → simula a jogada dos dados.
atualizar_posicao() → move o jogador para a nova posição.
contador() → calcula e exibe o vencedor.
main() → executa o jogo principal.
