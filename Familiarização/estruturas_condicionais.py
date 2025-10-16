# estruturas condicionais

# usando estruturas condicionais o código toma diferentes caminhos dependendo do resultado da verificação
# ao trocarmos o valor da variável podemos ver as diferentes saídas, recomendo que faça isso caso não tenha muita familiaridade ainda com as estruturas condicionais
tomei_banho_hoje = 'não ... mas'

if tomei_banho_hoje == 'sim':
    print('Estou cheiroso!')
elif tomei_banho_hoje == 'não ... mas':
    print('Não estou cheiroso e estou inventando desculpas!')
elif tomei_banho_hoje == 'não':
    print('Não estou cheiroso!')
else:
    print('Não mude de assunto!')
