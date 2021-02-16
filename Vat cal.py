price = int(input("Price (THB): "))
vat = 7
result = price + (price * vat / 100)
vatr = (price * vat / 100)
print("Price     =",price, "THB")
print("VAT       =",vatr,  "THB")
print("Price+VAT =",result,"THB")