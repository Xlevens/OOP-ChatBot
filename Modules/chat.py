from abc import ABC,abstractmethod
class Chat(ABC):
    @abstractmethod
    def chatfront(self):
        pass
    @abstractmethod
    def response(self):
        pass
       

        
    