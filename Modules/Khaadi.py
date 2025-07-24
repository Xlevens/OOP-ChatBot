from Modules.user import UserFront

class KhaadiChat(UserFront):
    def __init__(self, name):
        super().__init__(name)

    def response(self):
        return f"IBOT: Hey {self.name}!, welcome to Khaadi Clothing Support 😊\nTell me how can I help you?"

    def queryset(self, query):
        query = query.lower()

        if "delivery" in query:
            return "IBOT: Your order is on the way and will be delivered soon."
 
        elif "deal" in query:
            return "IBOT: Our deals are updated weekly. Please check our website for the latest offers."
        elif "website" in query:
            return "IBOT: You can visit our website at www.khaadi.com for more information."
        elif "return" in query or "exchange" in query:
            return "IBOT: Our return and exchange policy allows returns within 30 days. Visit our website for details."
        elif "store" in query or "location" in query:
            return "IBOT: You can find our store locations on our website under the 'Store Locator' section."
        elif "size" in query or "fit" in query:
            return "IBOT: We provide a detailed size guide on our website to help you choose the perfect fit."
        elif "payment" in query or "method" in query:
            return "IBOT: We accept credit cards, debit cards, and cash on delivery."
        elif "order status" in query or "track" in query:
            return "IBOT: You can track your order by logging into your account on our website."
        elif "feedback" in query or "complaint" in query:
            return "IBOT: We value your feedback. Please share your concerns and we will address them promptly."
        elif "thank you" in query or "thanks" in query:
            return "IBOT: You're welcome! 😊"
        else:
            return "IBOT: Oops, looks like I don't have info on that. Please ask something else."
