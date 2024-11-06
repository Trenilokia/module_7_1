from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        create_file = open(self.__file_name, 'a')
        create_file.close()

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            for line in file:
                print(line.strip())
            products = file.read().splitlines()
        return ', '.join(products)


    def add(self, *products):
        current_products = open(self.__file_name, 'r')
        check_products = str(current_products.readlines())
        current_products.close()
        for i in products:
            if i.name and i.weight and i.category not in check_products:
                new_product_list = open(self.__file_name, 'a')
                new_product_list.write(f'{i.name} {i.weight} {i.category}\n')
                new_product_list.close()
            else:
                print(f'Продукт {i.name}, {i.weight}, {i.category} уже существует')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
