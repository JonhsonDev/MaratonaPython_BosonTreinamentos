<h1 align="center">➗ Operadores Aritméticos em Python — Dominando os Cálculos</h1>

<p align="center">
  <em>Os operadores aritméticos permitem realizar cálculos matemáticos em Python. Vamos entender como cada um funciona, com exemplos práticos e diretos!</em>
</p>

<hr>

<h2>👋 Introdução</h2>

<p>
Em Python, os <strong>operadores aritméticos</strong> são usados para realizar operações matemáticas básicas, como soma, subtração, multiplicação e divisão.  
Eles funcionam com números inteiros (<code>int</code>), decimais (<code>float</code>) e até com expressões mais complexas.
</p>

<pre><code class="language-python">a = 10
b = 3

soma = a + b
print(soma)  # 13
</code></pre>

<hr>

<h2>🧮 Operadores e Suas Funções</h2>

<table align="center">
<tr><th>Operador</th><th>Descrição</th><th>Exemplo</th><th>Resultado</th></tr>
<tr><td><code>+</code></td><td>Adição</td><td><code>5 + 2</code></td><td>7</td></tr>
<tr><td><code>-</code></td><td>Subtração</td><td><code>5 - 2</code></td><td>3</td></tr>
<tr><td><code>*</code></td><td>Multiplicação</td><td><code>5 * 2</code></td><td>10</td></tr>
<tr><td><code>/</code></td><td>Divisão</td><td><code>5 / 2</code></td><td>2.5</td></tr>
<tr><td><code>//</code></td><td>Divisão inteira</td><td><code>5 // 2</code></td><td>2</td></tr>
<tr><td><code>%</code></td><td>Resto da divisão (módulo)</td><td><code>5 % 2</code></td><td>1</td></tr>
<tr><td><code>**</code></td><td>Exponenciação</td><td><code>5 ** 2</code></td><td>25</td></tr>
</table>

<hr>

<h2>⚙️ Exemplos Práticos</h2>

<pre><code class="language-python">x = 10
y = 3

print("Soma:", x + y)
print("Subtração:", x - y)
print("Multiplicação:", x * y)
print("Divisão:", x / y)
print("Divisão inteira:", x // y)
print("Resto da divisão:", x % y)
print("Exponenciação:", x ** y)
</code></pre>

<p>🧩 Saída:</p>

<pre><code>Soma: 13
Subtração: 7
Multiplicação: 30
Divisão: 3.3333333333333335
Divisão inteira: 3
Resto da divisão: 1
Exponenciação: 1000
</code></pre>

<hr>

<h2>📊 Ordem das Operações (Precedência)</h2>

<p>
Python segue a mesma <strong>ordem matemática padrão</strong> (PEMDAS):  
Parênteses → Expoentes → Multiplicação e Divisão → Adição e Subtração.
</p>

<pre><code class="language-python">resultado = 2 + 3 * 4
print(resultado)  # 14, e não 20!

resultado = (2 + 3) * 4
print(resultado)  # 20
</code></pre>

<p>
✅ Sempre use <strong>parênteses</strong> para deixar o cálculo mais claro e evitar erros de lógica.
</p>

<hr>

<h2>🔄 Operadores Aritméticos Combinados</h2>

<p>
Você pode usar operadores aritméticos junto com o operador de atribuição (<code>=</code>) para atualizar o valor de uma variável.
</p>

<pre><code class="language-python">n = 10

n += 2   # n = n + 2 → 12
n -= 3   # n = n - 3 → 9
n *=*
