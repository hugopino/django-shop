class Checkout:

    def __init(self, request):
        self.request = request 
        self.session = request.session
        checkout = self.session.get('checkout')
        if not checkout:
            self.checkout = self.session['checkout'] = {}
        else:
            self.checkout = checkout

    def add_to_cart(self, product):
        if(str(product.id) not in self.checkout.keys()):
            self.checkout[product.id] = {
                "product_id" : product.id,
                "name" : product.name,
                "price" : str(product.price),
                "amount" : 1,
                "imagen" : product.imagen.url,
            }
        else:
            for key, value in self.checkout.items():
                if key == str(product.id):
                    value["cantidad"] += 1
                    break
        self.save_cart()
    
    def save_cart(self):
        self.session['checkout'] = self.checkout
        self.session.modified = True

    def delete_product(self, product):
        product.id = str(product.id)
        if product.id in self.checkout:
            del self.checkout[id]
            self.save_cart()

    def decrement_product(self, product):
        for key, value in self.checkout.items():
            if key == str(product.id):
                if value['amount'] <= 1:
                    self.delete_product(product)
                else:
                    value["amount"] -= 1
                self.save_cart()
                break
    def clear_cart(self):
        self.session['checkout'] = {}
        self.session.modified = True