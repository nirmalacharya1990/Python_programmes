class Animal:
  def _init_(self):
    print('Animal Created')
  
  def whoAmI(self):
    print('Animal')
  
  def eat(self):
    print('Eating')

class Dog(Animal):
  def _init_(self):
    Animal._init_(self)
    print('Dog Created')
  
  def whoAmI(self):
    print("Dog")

  def bark(self):
    print('Bow')

d = Dog()
d.whoAmI