from Modules.user import UserFront
class RoninChat(UserFront):
    def __init__(self,name):
        super().__init__(name)
    def response(self):
        return f"Hey {self.name}!, welcome to Ronin Lifestyles Tech Support😊\nTell me how can I help you?"

    def queryset(self,query):
        query = query.lower()
        if "warranty" in query:
            return "Our products come with a 1-year warranty. Please provide your purchase details for assistance."
        elif "return" in query:
            return "You can return any product within 30 days of purchase. Visit our website for the return process."
        elif "repair" in query:
            return "We offer repair services for all Ronin devices. Please share your device model and issue."
        elif "order status" in query:
            return "To check your order status, please provide your order ID."
        elif "technical issue" in query:
            return "Sorry for the inconvenience. Can you describe the technical issue you're facing?"
        elif "accessories" in query:
            return "We have a wide range of accessories available. What are you looking for?"
        elif "payment" in query:
            return "We accept payments via credit card, debit card, and online banking."
        elif "delivery" in query:
            return "Standard delivery takes 3-5 business days. Express options are also available."
        elif "product info" in query:
            return "Please specify the product you're interested in, and I'll share its details."
        elif "contact" in query:
            return "You can reach our support team at support@ronin.pk or call 0800-RONIN."
        else:
            return "I'm here to help with Ronin tech support. Could you please provide more details about your query?"
        
    