"""
Pep8 - Python Enchament Proposal

São propostas de melhoria para a linguagem python

import this

A ideia da Pep8 ẽ que possamos escrever códigos Python de forma Pythonica

[1] - Utilize camel Case para nomes de Classes;
[2] - utilize nomes em minuscolo por urdeline para funcoes ou variaveis;
[3] - Utilize 4 espaços para identação.
[4] - Linhas em branco
- Separar fuções e deficições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco
[5] - imports devem ser feitos em linha separadas
- imports devem ser colocados no topo do arquivo, logo depois de quaiquer comentários ou docstrings,
antes de constantes 
[6] - Espaçoes em expressões e instruções
[7] - termine sempre uma instrução com uma nova linha
"""


"[1]-------------------------------"


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


"[2]--------------------------------"


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

"[3]--------------------------------"
if "a" in "banana":
    print("tem")  # quarto espaços de diferença.


"[4]--------------------------------"


class Classe:
    pass


class OutraClase:
    def test1(self):
        pass

    def test2(self):
        pass


"[5]--------------------------------"

# import errado

"import sys, os"

# import certo

"import sys"
"import os"

# Não há problema em utilizar:
"from types import StringType, ListType"

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

" from types import( "
" StopAsyncIteration "
" cached__"
" )"

"[6]--------------------------------"

# Não faça:
"funcao (algo[ 1 ], {outro: 2 })"

# faça
"funcao(algo[1], {outro:2})"


"[7]--------------------------------"
