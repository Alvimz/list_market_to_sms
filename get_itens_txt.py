class GetItensTxt:
    def __init__(self) -> None:
        self._itens = list()
        self.msg = None

    @property
    def itens(self):
        return self._itens

    @itens.setter
    def itens(self, arquivo):
        with open(arquivo, "r", encoding="utf-8") as file:
            for line in file:
                item, qnt = line.title().strip().split(",")
                self._itens.append((f"item:{item},qnt:{qnt}"))

    def show_itens_in_list(self):
        print(10 * "-")
        for item in self._itens:
            print(item)

        print(10 * "-")
    
        
    def create_msg(self):
        self.msg = "\n".join(self._itens)
        return self.msg


if __name__ == "__main__":
    a = GetItensTxt()
    a.itens = "itens_comprar.txt"
    a.show_itens_in_list()
