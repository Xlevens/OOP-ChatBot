from Modules.user import UserFront
from Modules.Ronin import *
from Modules.Zubaidas import *
from Modules.Khaadi import *
class MainChat(UserFront):
    def __init__(self,name):
        super().__init__(name)
       
    def req(self):
        return f"Hey {self.name}!, This is Ibot. Your chatbot. Tell me who do you want to chat with?"
    def response(self,res):
        res.lower()
        if "ronin" in res:
            cb = RoninChat(self.name)
          
            return f"You are now chatting with Ronin's support\n{cb.response()}",cb
        elif "zubaida" in res:
            cb = ZubaidaChat(self.name)
            return f"You are now chatting with Zubaidas support\n {cb.response()}",cb
        elif "khaadi" in res:
            cb = KhaadiChat(self.name)
            return f"You are now chatting with Khaadi Support\n {cb.response()}",cb
        else:
            return f"Sorry, I don't recognize that name. Please choose from ChaseUp, Zubaidas, or Khaadi."
        
    