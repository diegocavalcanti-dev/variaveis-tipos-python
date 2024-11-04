
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




verdadeiro = True
print(verdadeiro)

falso = False
print(falso)