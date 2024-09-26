# class P1:
#     __name='Abhishek'
#     def display(self):
#         print(P1.__name) 
           
# obj=P1()
# obj.display()         

# Calculator

# class A:
#     def add(*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print (sum)

# obj=A
# obj.add(20,30)
# obj.add(20,25,45,56,85,75,65,10,15,35)        


# super

# class A:
#     def display(self):
#         print("this is from class A")
        
# class B(A):
#     def display(self):
#         print("this is from class B")
        
#     def show(self):
#         super().display()
        
# obj=B()
# obj.display()
# obj.show()


# Overloading

class A:
    def add(x=0,y=0):
        return x+y
        
    def add(x=0,y=0,z=0):
        return x+y+z
        
obj=A
x=obj.add(4,5)
print(x)