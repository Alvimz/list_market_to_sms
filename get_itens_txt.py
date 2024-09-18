class GetItensTxt:
    def __init__(self) -> None:
        self.itens = list()

    def get_itens(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as file:
            for line in file:
                item, qnt = line.strip().split(',')
                self.itens.append(f'Item:{item},Qnt:{qnt}')

    def show_itens_in_list(self):
        print(10 * '-')
        for item in self.itens:
            print(item)
        print(10 * '-')

if __name__ == '__main__':
    a = GetItensTxt()
    a.get_itens('itens_comprar.txt')  # Carrega os itens diretamente
    a.show_itens_in_list()
