# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# person1 = Person("Alice",30)
# person2 = Person("Bob",25)

# print(person1.name)
# print(person2.age)

# message = person1.greet()
# print(message)



# class Person:
#     def greet(self,name,age):
#         return f"Hello, my name is {name} and I am {age} years old."

# person1 = Person()
# person2 = Person()

# value = person1.greet("Alice", 30 )
# print(value)



# class Car:
#     wheels = 4 # class attributes

#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
    
#     def display(self):
#         return f"This is {self.make} and model is {self.model}. This car can run fast cause it has {self.wheels}"

# print (Car.wheels)

# car1 = Car("Toyota","Camry")
# car2 = Car("Honda", "Accord")

# print (car1.display())


#  ------------------------ Inheritance ------------------------

# Singal Inheritance

# class animal:
#     def speaks(self):
#         print("Animal Speaks.")

# class dog(animal):
#     def abc(self):
#         print("Dog Barks.")

# animal1 = animal()
# animal1.speaks()

# dog1 = dog()
# dog1.speaks()

# MulitLevel Interiance

# class A:
#     def method_A(self):
#         return "Method_A"

# class B(A):
#     def method_B(self):
#         return "Method_B"
    
# class C(B):
#     def method_C(self):
#         return "Method_C"
    
# obj_c = C()

# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())



# Multiple Inheritance


# class A:
#     def method_A(self):
#         return "Method_A"

# class B:
#     def method_B(self):
#         return "Method_B"
    
# class C(A,B):
#     def method_C(self):
#         return "Method_C"
    
# obj_c = C()

# print(obj_c.method_A())
# print(obj_c.method_B())
# print(obj_c.method_C())



# Super KeyWord()

# class rectangle:
#     def area(self,w,l):
#         return w*l

# class square(rectangle):
#     def __init__(self,side):
#         self.length = side
    
#     def Squar_Area(self):
#         value = super().area(self.length,self.length)
#         print("Area of Squar is : " ,value)

# box = square(5)
# box.Squar_Area()
# box.area(5,10)


class Calc:

    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2
calc = Calc()
print(calc.add(5,6))
print(calc.sub(10,6))
print(calc.mul(5,5))
print(calc.div(10,2))
