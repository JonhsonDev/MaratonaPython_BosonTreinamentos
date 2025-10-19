<h1 align="center">🔠 Variáveis em Python — Entendendo a Base da Linguagem</h1>

<p align="center">
  <em>As variáveis são o coração de qualquer programa. Vamos entender como elas funcionam no Python, com exemplos simples e diretos!</em>
</p>

<hr>

<h2>👋 Introdução</h2>

<p>
Em Python, uma <strong>variável</strong> é um nome que faz referência a um <strong>objeto armazenado na memória</strong>.  
Diferente de muitas linguagens, Python não exige declarar o tipo antes de usar — ele é determinado automaticamente conforme o valor atribuído.
</p>

<pre><code class="language-python">x = 10          # 'x' aponta para o número inteiro 10
nome = "Jonhson" # 'nome' aponta para o texto "Jonhson"
</code></pre>

<p>
👉 Em resumo: <strong>uma variável não guarda o valor em si</strong>, mas sim uma <strong>referência</strong> para o objeto que contém esse valor.
</p>

<hr>

<h2>📘 Regras e Boas Práticas de Nomeação</h2>

<ul>
  <li>🔤 Deve começar com letra ou underscore (<code>_</code>).</li>
  <li>🚫 Não pode começar com número nem conter espaços.</li>
  <li>🔠 É sensível a maiúsculas e minúsculas (<code>idade</code> é diferente de <code>Idade</code>).</li>
  <li>❌ Não pode usar palavras reservadas do Python (<code>if</code>, <code>while</code>, <code>class</code>, etc).</li>
  <li>✅ Use nomes descritivos em <strong>snake_case</strong>: <code>idade_usuario</code>, <code>total_vendas</code>.</li>
</ul>

<pre><code class="language-python"># ✅ Bons exemplos:
nome_usuario = "Maria"
contador = 0

# ❌ Maus exemplos:
1nome = "José"    # começa com número
class = "A"       # palavra reservada
</code></pre>

<hr>

<h2>🧩 Tipagem Dinâmica</h2>

<p>
Python é <strong>dinamicamente tipado</strong>, ou seja, o tipo da variável muda conforme o valor atribuído.
</p>

<pre><code class="language-python">x = 10
print(type(x))  # <class 'int'>

x = "Olá"
print(type(x))  # <class 'str'>
</code></pre>

<p>
Você também pode converter tipos manualmente (chamamos isso de <em>casting</em>):
</p>


<pre><code class="language-python">idade = "21"
idade = int(idade)  # agora é um inteiro
</code></pre>

<p>
<em>OBS:</em> Vamos ver sobre casting melhor em outro momento ⚡ 
</p>

<hr>

<h2>🧠 Atribuição e Desempacotamento</h2>

<p>
É possível atribuir valores de várias formas:
</p>

<pre><code class="language-python">a = 1
b = 2
a, b = b, a   # troca de valores

# Atribuição múltipla:
x, y, z = 10, 20, 30
</code></pre>

<p>
🔁 Também existem operadores de atribuição aumentada:
</p>

<pre><code class="language-python">n = 5
n += 2   # n = n + 2 → resultado: 7
</code></pre>

<hr>

<h2>🔄 Mutabilidade e Imutabilidade</h2>

<p>
Em Python, alguns objetos são <strong>imutáveis</strong> (não podem ser alterados após criados), e outros são <strong>mutáveis</strong> (podem ser modificados).
</p>

<p>
<em>OBS:</em> Vamos entender melhor as listas em outro momento, não preste atenção nisso agora, só tente entender a lógica por trás de maneira superficial ⚡ 
</p>

<table align="center">
<tr><th>Imutáveis</th><th>Mutáveis</th></tr>
<tr><td><code>int</code>, <code>float</code>, <code>str</code>, <code>tuple</code></td><td><code>list</code>, <code>dict</code>, <code>set</code></td></tr>
</table>

<pre><code class="language-python"># Exemplo com lista (mutável)
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3] — 'a' também mudou!

# Para evitar isso:
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
</code></pre>

<hr>

<h2>🌍 Escopo: Local e Global</h2>

<p>
O <strong>escopo</strong> define onde uma variável pode ser acessada:
</p>

<ul>
  <li><strong>Local:</strong> criada dentro de uma função (só existe ali).</li>
  <li><strong>Global:</strong> criada fora de funções, acessível por todo o arquivo.</li>
</ul>

<pre><code class="language-python">x = 10  # variável global

def mostrar():
    y = 5  # variável local
    print(x, y)

mostrar()
print(x)  # funciona
print(y)  # erro: y não existe aqui
</code></pre>

<p>
Se precisar modificar uma variável global dentro de uma função:
</p>

<pre><code class="language-python">contador = 0

def incrementar():
    global contador
    contador += 1
</code></pre>

<hr>

<h2>💡 None e Booleanos</h2>

<p>
Python usa <code>None</code> para representar “sem valor”.  
E possui os booleanos <code>True</code> e <code>False</code> para condições lógicas.
</p>

<pre><code class="language-python">resultado = None
ativo = True

if ativo:
    print("Usuário ativo")
</code></pre>

<hr>

<h2>⚙️ Deletando Variáveis</h2>

<pre><code class="language-python">x = 100
del x
# print(x)  -> NameError (x foi removido)
</code></pre>

<hr>

<h2>📋 Resumo Rápido</h2>

<ul>
  <li>🐍 Variáveis são referências a objetos na memória.</li>
  <li>⚡ Tipagem dinâmica — tipo muda conforme o valor.</li>
  <li>🧱 Objetos podem ser mutáveis ou imutáveis.</li>
  <li>🌐 Escopo define onde a variável “existe”.</li>
  <li>🧩 Use nomes claros e evite variáveis globais desnecessárias.</li>
</ul>

<hr>

<h2>🚀 Exemplo Prático</h2>

<pre><code class="language-python"># Programa simples para demonstrar variáveis

nome = "José"
idade = 21
peso = 82.5
estudante = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso} kg")
print(f"É estudante? {estudante}")
</code></pre>

<hr>

<h3>📌 Autor: <strong>José Jonhson Barros Tavares</strong></h3>

<p align="center">
🧭 <em>Assunto:</em> Fundamentos do Python <br>
⭐ <em>Se este conteúdo te ajudou, deixa uma estrela no repositório!</em>
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Aprendizado-Contínuo-brightgreen?style=for-the-badge" alt="Learning">
</div>
