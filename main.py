from get_itens_txt import GetItensTxt
from sms import Sms

class Main:
    market_list = GetItensTxt()
    market_list.itens = 'itens_comprar.txt'
    msg_sms = market_list.create_msg()
    
    create_sms = Sms()
    create_sms._number_phone_twilo = ...
    create_sms._account_sid = ...
    create_sms.auth_token = ...
    to_number = ...
    create_sms.sent_sms(to_number,msg_sms)
    
if __name__ == '__main__':
    Main()
    
    