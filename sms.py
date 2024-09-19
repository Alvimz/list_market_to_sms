from twilio.rest import Client
class Sms:
    def __init__(self) -> None:
        self._number_phone_twilo = None
        self._auth_token = None
        self._account_sid = None

    @property
    def account_sid(self):
        return self._number_phone_twilo
    @account_sid.setter
    def account_sid(self,number):
        self._account_sid = number
        
    @property
    def auth_token(self):
        return self._auth_token
    
    @auth_token.setter
    def auth_token(self,token):
        self._auth_token = token
    
    def sent_sms(self,destinatario:str,msg:str):
        client = Client(self._account_sid, self.auth_token)
        message = client.messages.create(
            body=msg,
            from_=self._number_phone_twilo,  
            to= destinatario  
        )

        print(f"Mensagem enviada com sucesso!: {message.sid}")
        



    

        