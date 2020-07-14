class Product:
    def __init__(self, code, name, price, weight):
        self.code = code
        self.name = name
        self.price = price
        self.weight = weight

    def get_last_code(self):
        return self.code +1