from Modules.user import UserFront
from Modules.responselist import Responselist

class KhaadiChat(UserFront,Responselist):
    def __init__(self,name):
        UserFront.__init__(self,name)
        Responselist.__init__(self)
        
    def response(self):
        
        return f"IBOT: Hey {self.name}!, welcome to Khaadi Clothing Support 😊\nTell me how can I help you?"

    def chatbot_response(self,query):
        query = query.lower().strip()
        for keywords, response in self.responses.items():
            if any(keyword in query for keyword in keywords):
                self.result =  response
                break
        else:
                self.result= "IBOT: Oops 😅, I don’t have information on that yet. Try asking about delivery, deals, or returns!"

    
    def __str__(self):

        return self.result

 



