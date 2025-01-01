class product:
    #class attributes
    def __init__(self,name,price,deal_price,rating):
        #instance attributes
        self.name = name
        self.price = price 
        self.deal_price = deal_price
        self.rating = rating 
        self.you_save = price - deal_price
    
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Offer: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("Your_saving: {}".format(self.you_save))
    
    def get_deal_price(self):
        return self.deal_price

#Inheritance : sub_class = Electronic_items ; super_class = product 
class Electronic_items(product):
    # method overriding
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months = warranty_in_months
    
    # method overriding
    def display_product_details(self):
        super().display_product_details()
        print("warranty_in_months: {} months".format(self.warranty_in_months))

# creating a multi-sub_class or (multi-level Inheritance) ; Electronic_items = parent : Laptop = child
class Laptop(Electronic_items):
    def __init__(self,name,price,deal_price,rating,warranty_in_months,ram ,os,storage):
        super().__init__(name,price,deal_price,rating,warranty_in_months)
        self.ram = ram
        self.os = os 
        self.storage = storage
        
    def display_product_details(self):
        super().display_product_details() 
        print("RAM: {}".format(self.ram))
        print("OS: {}".format(self.os))
        print("ROM/SSD: {}".format(self.storage))
# creating New sub class 
class Grocery_item(product):
    # method overriding
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date = expiry_date
    
    # method overriding
    def display_product_details(self):
        super().display_product_details()
        print("expiry_date: {}".format(self.expiry_date))


#creating a new super class 
class Order:
    #class attributes
    delivery_charges = {
        "prime_delivery": 0 , "normal_delivery": 50 
    }
    def __init__(self,member_type,delivery_address):
        self.items_in_cart = [] # <-- list contains [(poduct, quantity)] ; product is used in another super_class so it is called comosition.
        self.member_type = member_type
        self.delivery_address = delivery_address
    
    def add_items(self,product,quantity):
        items = (product,quantity)
        self.items_in_cart.append(items)
        
    
    def display_Order_details(self):
        print("Order type: {}".format(self.member_type))
        print("Delivery address: {}".format(self.delivery_address))
        print("-------------------------------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}\n".format(quantity))
        print("-------------------------------")
        order_delivery_charges = Order.get_delivery_charge(self.member_type)
        print("Delivery_charges: {}".format(order_delivery_charges))
        print("Total price: {}".format(self.get_total_price()))
            
    #total_bill    
    
    def get_total_price(self):
        total_price = 0 
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_price += price
        order_delivery_charges = Order.get_delivery_charge(self.member_type)   
        total_price += order_delivery_charges
        return total_price    
    
    @classmethod 
    def get_delivery_charge(cls,order_type):
        return cls.delivery_charges[order_type]
        
        
        
    
#Instantiation (or) (creating an instance of class)  =   object   
tv = Electronic_items("LED TV",40000,35000,4.5,24)
keyboard = Electronic_items("ANT ESPORTS",1150,1000,4.5,12)
butter_milk = Grocery_item("Butter MIlk",100,98,4.3,"Jan 2025")
Milk = Grocery_item("Milk",12,10,4.2,"Jan 2025")
laptop = Laptop("HP",50000,49000,4.6,24," 8GB","Windows OS","1 TB/SSD")
icecream = Grocery_item("strawberry",50,49,4.1,"Jan-26")
#tv.display_product_details()
#butter_milk.display_product_details()

My_orders = Order("normal_delivery","Salem")
My_orders.add_items(tv,1)
My_orders.add_items(keyboard,1)
My_orders.add_items(butter_milk,5)
My_orders.add_items(Milk,10)
My_orders.add_items(laptop,1)
My_orders.add_items(icecream,3)

My_orders.display_Order_details()