class GetItensTxt:
    def __init__(self) -> None:
        self.itens = list()
        
    
    def get_itens(self):
        with open('itens_comprar.txt','r',encoding='utf-8') as file:
            
            for line in file:
                item, qnt = line.strip().split(',')
                self.itens.append((f'Item:{item},Qnt:{qnt}'))
            
    def exibir_lista_compras(self):
        print(10*'-')
        for item in self.itens:
            
            print(item)
            
        print(10*'-')
                
            
                
            
if __name__ == '__main__':
    a = GetItensTxt()
    a.get_itens()
    a.exibir_lista_compras()
    
   
    
    
            
            
        
        
        