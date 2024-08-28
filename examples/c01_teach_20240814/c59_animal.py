class Animal:
    def walk(self):
        print("走路")

    def eat(self):
        print("吃")


class Cat(Animal):
    pass


cat = Cat()
cat.walk()
cat.eat()
