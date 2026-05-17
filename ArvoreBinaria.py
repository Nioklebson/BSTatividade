# Árvore Binária de Busca (BST)

def criar_no(valor):

    return {
        "valor": valor,
        "esquerda": None,
        "direita": None
    }


# Inserir valores
def inserir(no, valor):

    if no is None:
        return criar_no(valor)

    # Esquerda
    if valor < no["valor"]:

        no["esquerda"] = inserir(no["esquerda"], valor)

    # Direita
    elif valor > no["valor"]:

        no["direita"] = inserir(no["direita"], valor)

    return no


# Buscar valor
def buscar(no, valor):

    if no is None:
        return None

    # Valor encontrado
    if no["valor"] == valor:
        return no

    # Esquerda
    if valor < no["valor"]:
        return buscar(no["esquerda"], valor)

    # Direita
    return buscar(no["direita"], valor)


# Menor valor da subárvore
def menor_valor(no):

    atual = no

    while atual["esquerda"] is not None:

        atual = atual["esquerda"]

    return atual


# Remover valor
def remover(no, valor):

    if no is None:
        return None

    # Esquerda
    if valor < no["valor"]:

        no["esquerda"] = remover(no["esquerda"], valor)

    # Direita
    elif valor > no["valor"]:

        no["direita"] = remover(no["direita"], valor)

    # Valor encontrado
    else:

        # Sem filho esquerdo
        if no["esquerda"] is None:
            return no["direita"]

        # Sem filho direito
        if no["direita"] is None:
            return no["esquerda"]

        # Nó com dois filhos
        menor = menor_valor(no["direita"])

        no["valor"] = menor["valor"]

        no["direita"] = remover(
            no["direita"],
            menor["valor"]
        )

    return no


# Percurso In-Order
def em_ordem(no):

    if no is None:
        return

    em_ordem(no["esquerda"])

    print(no["valor"], end=" ")

    em_ordem(no["direita"])


# ============================================
# Exercício
# ============================================

raiz = None

valores = [50, 30, 70, 20, 40, 60, 80]

# Inserção
for valor in valores:

    raiz = inserir(raiz, valor)

# Buscar 60
resultado = buscar(raiz, 60)

if resultado:
    print("Valor 60 encontrado.")

else:
    print("Valor não encontrado.")

# Remover 30
raiz = remover(raiz, 30)

# In-Order final
print("\nIn-Order final:")

em_ordem(raiz)