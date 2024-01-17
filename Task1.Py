class Catalogue:
    def __init__(self):
        self.products = {
            "Product A": 20,
            "Product B": 40,
            "Product C": 50
        }
        self.rules = {
            "flat_10_discount": {"threshold": 200, "discount": 10},
            "bulk_5_discount": {"threshold": 10, "discount": 5},
            "bulk_10_discount": {"threshold": 20, "discount": 10},
            "tiered_50_discount": {"quantity_threshold": 30, "single_product_threshold": 15, "discount": 50}
        }
        self.gift_wrap_fee = 1
        self.shipping_fee_per_package = 5
        self.units_per_package = 10

    def calculate_discount(self, cart_total, quantities):
        applicable_discounts = {}

    
        if cart_total > self.rules["flat_10_discount"]["threshold"]:
            applicable_discounts["flat_10_discount"] = self.rules["flat_10_discount"]["discount"]

  
        for product, quantity in quantities.items():
            if quantity > self.rules["bulk_5_discount"]["threshold"]:
                applicable_discounts["bulk_5_discount"] = self.rules["bulk_5_discount"]["discount"]

     
        total_quantity = sum(quantities.values())

     
        if total_quantity > self.rules["tiered_50_discount"]["quantity_threshold"]:
            for product, quantity in quantities.items():
                if quantity > self.rules["tiered_50_discount"]["single_product_threshold"]:
                    applicable_discounts["tiered_50_discount"] = self.rules["tiered_50_discount"]["discount"]

       
        if applicable_discounts:
            max_discount = max(applicable_discounts.values())
            discount_name = [k for k, v in applicable_discounts.items() if v == max_discount][0]
            return discount_name, max_discount
        else:
            return None, 0

    def calculate_shipping_fee(self, total_units):
        return (total_units // self.units_per_package) * self.shipping_fee_per_package

    def run_program(self):
        quantities = {}
        total_amount = 0

        for product, price in self.products.items():
            quantity = int(input(f"Enter quantity for {product}: "))
            is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"

            
            product_total = quantity * price
            if is_gift_wrapped:
                product_total += quantity * self.gift_wrap_fee

            quantities[product] = quantity
            total_amount += product_total

            print(f"{product}: Quantity: {quantity}, Total Amount: ${product_total}")


        subtotal = sum(quantities.values()) * total_amount

       
        discount_name, discount_amount = self.calculate_discount(subtotal, quantities)
        print(f"\nSubtotal: ${subtotal}")
        if discount_name:
            print(f"Discount Applied: {discount_name}, Amount: ${discount_amount}")
            subtotal -= discount_amount

        shipping_fee = self.calculate_shipping_fee(sum(quantities.values()))
        print(f"Shipping Fee: ${shipping_fee}")

     
        total = subtotal + shipping_fee
        print(f"\nTotal: ${total}")


if __name__ == "__main__":
    catalogue = Catalogue()
    catalogue.run_program()
