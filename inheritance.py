# single level inheritance

# class p:
#     city="Bhopal"
#     def display(self):
#         print("this is from display")
        
# class c(p):
#     def show(self):
#         print("this is from show")
#         print("city=",p.city)
        
# obj=c()
# obj.show()
# print(obj.city,obj.display())  

# multilevel inheritance

# class p:
#     city="Bhopal"
#     def display(self):
#         print("this is from display")
        
# class c(p):
#     def show(self):
#         print("this is from show")
#         print("city=",p.city)
        
# class c1(c):
#     city1=p.city
#     def show1(self):
#         self.display()
#         self.show()      
        
# obj=c1()
# print(obj.city1)  
# obj.show1()
# obj.show()
# obj.display()
# print(obj.city)   


 # Multiplae inheritance
 
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
        pass

print(D.mro())        