class GetItensTxt:
    def __init__(self) -> None:
        self._itens = list()
    
    @property
    def itens(self):
        return self._itens    
    
    def get_itens(self):
        with open('itens_comprar.txt','r',encoding='utf-8') as file:
            
            for line in file:
                item, qnt = line.strip().split(',')
                self._itens.append((f'Item:{item},Qnt:{qnt}'))
            
    def show_itens_in_list(self):
        print(10*'-')
        for item in self._itens:
            
            print(item)
            
        print(10*'-')
                
            
                
            
if __name__ == '__main__':
    a = GetItensTxt()
    a.get_itens()
    a.show_itens_in_list()
    
   
    
    
            
            
        
        
        