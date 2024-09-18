class GetItensTxt:
    def __init__(self) -> None:
        self._itens = list()
        
    
   
         
    
    def get_itens(self,arquivo):
        with open(arquivo,'r',encoding='utf-8') as file:
            
            for line in file:
                item, qnt = line.strip().split(',')
                self._itens.append((f'Item:{item},Qnt:{qnt}'))
            
    def show_itens_in_list(self):
        print(10*'-')
        for item in self._itens:
            
            print(item)
            
        print(10*'-')

    @property
    def itens(self):
        return self._itens
    
    @itens.setter
    def itens(self,nomearquivo):
        self.get_itens(nomearquivo)
            
                
            
if __name__ == '__main__':
    a = GetItensTxt()
    a.itens='itens_comprar.txt'
    a.show_itens_in_list()
    
   
    
    
            
            
        
        
        