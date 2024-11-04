
# Definição
idade = 30 
print(idade)

idade = 27
print(idade)

nome = "diego"
print(nome)


# Tipos nativos
preco = 1000
tipo_preco = type(preco)

print(preco)
print(tipo_preco)

juros = 0.05
tipo_juros = type(juros)

print(juros)
print(tipo_juros)


# Tipos de texto: strings
primeiro_nome = "Diego"

print(primeiro_nome)
print(type(primeiro_nome))

pais = 'Brasil'

print(pais)
print(type(pais))



# Tipos lógicos: booleanos (bool):
usuario_maior_de_idade = True

print(usuario_maior_de_idade)
print(type(usuario_maior_de_idade))



# Tipo vazio (NoneType):
telefone_fixo = None

print(telefone_fixo)
print(type(telefone_fixo))

# ///////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////



# Números


### **3.2. Definição** 

# Armazenam **valores numéricos**: 

# *   `10, 37, 500` (inteiros);
# *   `0.333, 10.1` (decimais);
# *   `1 + 2j` (complexos).



# São dos tipos:

# *   `int` (inteiros);
# *   `float` (decimais);
# *   `complex` (complexos).



print(type(37))
print(type(10.1))
print(type(1 + 2j))

preco = 47
quantidade = 0.250

total_a_pagar = quantidade * preco
print(total_a_pagar)

#############################

# Ticket médio diário do dia 19/01.
#svv = soma do valor das vendas
svv_19 = 153.98
sqv_19 = 3

tkt_19 = svv_19 / sqv_19
print(tkt_19)

# Ticket médio diário do dia 20/01.
svv_20 = 337.01
sqv_20 = 7

tkt_20 = svv_20 / sqv_20
print(tkt_20)

# Ticket médio diário do dia 23/01.
svv_23 = 295.33
sqv_23 = 5

tkt_23 = svv_23 / sqv_23
print(tkt_23)


# Ticket médio
tkt = (tkt_19 + tkt_20 + tkt_23) / 3
print(tkt)



# Boleanos

# True (verdadeiro);
# False (falso).

verdadeiro = True
print(verdadeiro)

falso = False
print(falso)

# São resultados de comparações lógicas. Os operadores de comparação lógica são:

# > (maior);
# < (menor);
# == (igual);
# >= (maior ou igual);
# <= (menor ou igual);
# != (diferente).


saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)



codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

# ---------


# Operações
# As operações de variáveis booleanas são:

# | (operador ou)
# & (operador e)
# not (operador não)

# Tabela da verdade do operador | (ou).

print(True | True)
print(True | False)
print(False | False)
print(False | True)

#  Tabela da verdade do operador & (e).

print(True & True)
print(True & False)
print(False & False)
print(False & True)

# Tabela da verdade do operador not (não).

print(not True)
print(not False)


# -------------------------------------------

#  Conversão
# Podemos converter tipos numéricos e strings para booleanos através do método nativo bool:

idade = 19
tipo_sangue = 'O-'
filhos = 0
telefone_fixo = None
telefone_fixo = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo))


# -----------------------


usuario = 'andre.perez'
senha = 'andre123'

usuario_cadastro = 'andre.perez'
senha_cadastro = 'andre321'


# ----
usuario_igual = usuario == usuario_cadastro
senha_igual = senha == senha_cadastro

print(usuario_igual)
print(senha_igual)