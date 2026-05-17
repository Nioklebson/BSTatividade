# Desafio - Função altura(no)

# Criar nó
def criar_no(valor):

    return {
        "valor": valor,
        "esquerda": None,
        "direita": None
    }


# Inserir valores na árvore
def inserir(no, valor):

    # Se o nó estiver vazio
    if no is None:
        return criar_no(valor)

    # Vai para esquerda
    if valor < no["valor"]:

        no["esquerda"] = inserir(
            no["esquerda"],
            valor
        )

    # Vai para direita
    elif valor > no["valor"]:

        no["direita"] = inserir(
            no["direita"],
            valor
        )

    return no


# Função altura
def altura(no):

    # Caso base
    if no is None:
        return 0

    # Altura da esquerda
    esquerda = altura(no["esquerda"])

    # Altura da direita
    direita = altura(no["direita"])

    # Retorna a maior altura + 1
    return 1 + max(esquerda, direita)


# ============================================
# Valores do exercício
# ============================================

raiz = None

valores = [50, 30, 70, 20, 40, 60, 80]

# Inserção dos valores
for valor in valores:

    raiz = inserir(raiz, valor)

# Mostrar altura
print("Altura da árvore:", altura(raiz))