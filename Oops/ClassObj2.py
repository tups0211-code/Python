class laptop:
    brand = "default"
    ram = "8gb"
    price = "1 lakh"

#objects with diffrent attributes values
laptop1 = laptop()
laptop1.brand ="mackbook"
laptop1.ram = "11gb"
print(laptop1.brand,laptop1.ram,laptop1.price)

laptop2 = laptop()
laptop2.brand = "hp"
laptop2.price = "2 lakh"
print(laptop2.brand,laptop2.ram,laptop2.price)

# class level attribute value overide because we change it in the object level isinstance value 
#      when we change value with " . " > class value
