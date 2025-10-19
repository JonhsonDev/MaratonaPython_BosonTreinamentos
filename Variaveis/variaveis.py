# A variável é um espaço reservado na memória do computador que guarda dados temporariamente durante a execução de um programa
# Ela serve para armazenar valores que podem ser usados, modificados e manipulados pelo código.

# dei um nome para a variável e usei o sinal de atribuição (=) para definir o valor a ser armazenado
nome = 'josé jonhson'

# toda variável tem um nome, o tipo de dado associado, um tamanho que ocupa na memória, e o valor em sí que vai ser gravado na memória
# não precisamos informar o tipo de dado a ser armazenado na variável, pois o python possúi tipagem dinâmica, que identifica automaticamente o tipo do dado que vai ser armazenado na variável

# a função print() exibe saída para o usuário via terminal. Nesse caso, estamos usando a função para exibir o valor associado a variável 'nome'
print(nome)

# +++++_REGRAS_DA_CRIAÇÃO_DE_VARIÁVEIS_+++++
# Na hora de declarar uma variável no Python temos que levar em consideraação pontos importantes
# Pontos esses que na grande maioria das vezes poderão ser aplicados na criação de variáveis em outras linguagens de programação
# 1 - o nome pode apresentar um ou mais caractéres
# 2 - o primeiro caracter precisa ser uma letra
# 3 - não pode conter espaços em branco
# 4 - em caso de nome composto, usar (-), (_), ou 'CamelCase' para separar o nome da variável
# 5 - o Python é 'case sensitive', significa que ele faz a diferenciação de letras maiúsculas e minúsculas

# Declarando outras variáveis 
media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Makoto', 51

status = True

# A função type() é usada para verificar o tipo de dado de uma variável
print(type(nome))
print(type(media))
print(type(n1))
print(type(status))
# Em python temos o tipo de dado "número complexo", muito útil para áreas da engenharia
print(type(1+2j))

# Função isinstance() retorna True se a variável ou dado foir do determinado tipo especificado, ou False se não for
a = 10
b = 'Carro'
print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(b, str))
