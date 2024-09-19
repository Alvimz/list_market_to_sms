from get_itens_txt import GetItensTxt
from sms import Sms

class Main:
    market_list = GetItensTxt()
    market_list.itens = 'itens_comprar.txt'
    print(market_list.create_msg())
    
if __name__ == '__main__':
    Main()
    
    