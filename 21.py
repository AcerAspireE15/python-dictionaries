product = {

    "a": 200,
    "b": 300,
    "c": 400,
    "d": 500,
    "e": 600


}
print(product)
newproduct = input('enter product name:')
if(newproduct in product):
    print(product.get(newproduct))
else:
    print('product not found')
