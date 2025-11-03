# orderlist.py

class OrderList:
    def __init__(self):
        # Dictionary to store orders
        # Keys = order IDs, Values = order details
        self.orders = {
            "OCJ-202": {
                "status": "Shipped",
                "items": ["Kurta", "Shalwar", "Dupatta"],
                "expected_delivery": "2025-11-10",
                "price": 12500
            },
            "A15": {
                "status": "Processing",
                "items": ["T-Shirt", "Jeans"],
                "expected_delivery": "2025-11-12",
                "price": 5200
            },
            "B20": {
                "status": "Delivered",
                "items": ["Shirt", "Trousers"],
                "expected_delivery": "2025-10-28",
                "price": 4100
            },
            "C33": {
                "status": "Cancelled",
                "items": ["Jacket"],
                "expected_delivery": None,
                "price": 8500
            }
        }


