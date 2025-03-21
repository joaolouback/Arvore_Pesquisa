import matplotlib.pyplot as plt

# Classe para representar um nó da árvore binária


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Filho à esquerda
        self.right = None  # Filho à direita

# Classe para representar a Árvore Binária de Pesquisa (BST)


class BST:
    def __init__(self):
        self.root = None  # Raiz da árvore

    # Método para inserir um valor na árvore
    def insert(self, value):
        if self.root is None:
            # Se a árvore estiver vazia, o primeiro nó será a raiz
            self.root = Node(value)
            print(f"Número {value} inserido como raiz da árvore.")
        else:
            self._insert_recursive(self.root, value)
            print(f"Número {value} inserido com sucesso.")

    # Método recursivo para inserir um valor no local correto
    def _insert_recursive(self, node, value):
        if value == node.value:
            print("Valor já existe na árvore. Ignorando inserção.")
            return
        if value < node.value:
            if node.left is None:
                # Insere à esquerda se o espaço estiver livre
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                # Insere à direita se o espaço estiver livre
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Método para excluir um valor da árvore
    def delete(self, value):
        if not self.search(value):
            print("Valor não encontrado na árvore.")
            return
        self.root = self._delete_recursive(self.root, value)
        print(f"Número {value} excluído com sucesso.")

    # Método recursivo para deletar um nó
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(
                node.right, min_larger_node.value)
        return node

    # Método auxiliar para encontrar o menor valor de um nó (utilizado na remoção)
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # Método para buscar um valor na árvore
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Método recursivo para busca
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Método para atualizar um valor na árvore
    def update(self, old_value, new_value):
        if not self.search(old_value):
            print("Valor antigo não encontrado na árvore.")
            return
        if self.search(new_value):
            print("Novo valor já existe na árvore. Atualização cancelada.")
            return
        self.delete(old_value)
        self.insert(new_value)
        print(f"Número {old_value} atualizado para {new_value} com sucesso.")

    # Método para listar valores em ordem crescente (in-order traversal)
    def inorder(self):
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        if node:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)

    # Método para calcular a altura da árvore
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

# Função para exibir graficamente a árvore


def plot_tree(bst):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title("Árvore Binária de Pesquisa", fontsize=14, fontweight='bold')

    def _plot(node, x, y, dx):
        if node:
            ax.plot(x, y, 'ro', markersize=12)
            ax.text(x, y, str(node.value), fontsize=10, ha='center', va='center',
                    bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='circle'))
            if node.left:
                ax.plot([x, x - dx], [y - 1, y - 2], 'k-', lw=1)
                _plot(node.left, x - dx, y - 2, dx * 0.7)
            if node.right:
                ax.plot([x, x + dx], [y - 1, y - 2], 'k-', lw=1)
                _plot(node.right, x + dx, y - 2, dx * 0.7)

    _plot(bst.root, 0, 0, 5)
    ax.set_xlim(-7, 7)
    ax.set_ylim(-8, 2)
    ax.axis('off')
    plt.show()


# Menu interativo para testar as operações
if __name__ == "__main__":
    bst = BST()
    while True:
        print("\nMenu:")
        print("1 - Inserir um número")
        print("2 - Excluir um número")
        print("3 - Atualizar um número")
        print("4 - Listar valores em ordem")
        print("5 - Mostrar altura da árvore")
        print("6 - Exibir árvore graficamente")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite um número para inserir: "))
            bst.insert(valor)
        elif opcao == "2":
            valor = int(input("Digite um número para excluir: "))
            bst.delete(valor)
        elif opcao == "3":
            old_value = int(input("Digite o valor a ser atualizado: "))
            new_value = int(input("Digite o novo valor: "))
            bst.update(old_value, new_value)
        elif opcao == "4":
            print("Valores em ordem:", bst.inorder())
        elif opcao == "5":
            print("Altura da árvore:", bst.height())
        elif opcao == "6":
            plot_tree(bst)
        elif opcao == "7":
            print("Saindo... Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Tente novamente.")
