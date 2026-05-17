# Questão 5 - Árvore Binária de Busca (BST)

class BST:

    def __init__(self):
        self.arvore = {}
        self.raiz = None

    # Inserir valores
    def inserir(self, valor):

        if self.raiz is None:

            self.raiz = valor
            self.arvore[valor] = [None, None]
            return

        atual = self.raiz

        while True:

            # Esquerda
            if valor < atual:

                if self.arvore[atual][0] is None:

                    self.arvore[atual][0] = valor
                    self.arvore[valor] = [None, None]
                    return

                atual = self.arvore[atual][0]

            # Direita
            else:

                if self.arvore[atual][1] is None:

                    self.arvore[atual][1] = valor
                    self.arvore[valor] = [None, None]
                    return

                atual = self.arvore[atual][1]

    # Buscar valor
    def buscar(self, valor):

        atual = self.raiz

        while atual is not None:

            if valor == atual:
                return True

            elif valor < atual:
                atual = self.arvore[atual][0]

            else:
                atual = self.arvore[atual][1]

        return False

    # Percurso In-Order
    def em_ordem(self, no):

        if no is not None:

            self.em_ordem(self.arvore[no][0])

            print(no, end=" ")

            self.em_ordem(self.arvore[no][1])

    # Remover valor
    def remover(self, valor):

        if valor in self.arvore:
            del self.arvore[valor]

    # Altura da árvore
    def altura(self, no):

        if no is None:
            return 0

        esquerda = self.arvore[no][0]
        direita = self.arvore[no][1]

        return 1 + max(
            self.altura(esquerda),
            self.altura(direita)
        )


# ============================================
# Valores da árvore
# ============================================

bst = BST()

valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    bst.inserir(valor)

# ============================================
# Busca de valor digitado pelo usuário
# ============================================

numero = int(input("Digite um valor para buscar na árvore: "))

if bst.buscar(numero):
    print("Valor encontrado na árvore.")

else:
    print("Valor não encontrado.")

# ============================================
# Percurso In-Order
# ============================================

print("\nPercurso In-Order:")

bst.em_ordem(bst.raiz)

# ============================================
# Altura da árvore
# ============================================

print("\n\nAltura da árvore:", bst.altura(bst.raiz))