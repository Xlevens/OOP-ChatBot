from Modules.user import UserFront
class ZubaidaChat(UserFront):
    def __init__(self,name):
        super().__init__(name)
    def response(self):
        return f"Hey {self.name}!, welcome to Zubaida's Baby Store Support😊\nTell me how can I help you?"
       
    def queryset(self,query):
        if "did" in query:
            return f"Yeah you just made that"
        elif "what" in query:
            return f"What happen to you"
        else:
            return f"Oops looks like I don't have such kind of info you intended"
        
    