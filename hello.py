class Phone:
    def __init__(self, company, name, price):
        self.company = company
        self.name = name
        self.price = price


p1 = Phone(company='Samsung', name='Samsung Galaxy S3', price=122212)

print(p1.price)
