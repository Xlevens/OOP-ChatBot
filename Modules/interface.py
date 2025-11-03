from Modules.user import UserFront
from Modules.chat import Chat
from Modules.orderlist import OrderList


class Interface(UserFront,OrderList):
    def __init__(self, name, contact, order):
        UserFront.__init__(self,name, contact, order)
        self._name = name
        self._contact = contact
        self._order = order
        self.par = None
        OrderList.__init__(self)

    # --- name property ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    # --- contact property ---
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if not value.strip():
            raise ValueError("Contact cannot be empty.")
        self._contact = value

    # --- order property ---
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if not value.strip():
            raise ValueError("Order cannot be empty.")
        self._order = value
    def ordercheck(self):
        """Check if the order exists and store it in self.par (dictionary)."""
        user_order = self.order.strip().upper()
        self.par = None
        for order_id, result in self.orders.items():
            if user_order == order_id.upper():
                self.par = result
                break

    def orderstatus(self):
        """Return formatted order status."""
        if not self.par:
            return "Order not found"
        
        status = self.par["status"]
        items = self.par["items"]
        expected_delivery = self.par["expected_delivery"]
        price = self.par["price"]

        return (
            f"Your order status: {status}\n"
            f"Expected delivery: {expected_delivery}\n"
            f"Items: {', '.join(items)}\n"
            f"Price: {price} PKR"
        )
    # --- Optional readable printout ---
    def __str__(self):
        return f"Name: {self.name}, Contact: {self.contact}, Order: {self.order}"
