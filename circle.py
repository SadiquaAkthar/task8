class circle:
    
    __pi=3.141
    radius=1
    #parameterized constructor to find area
    def area_circle(self,l):
        print("Area for the list")
        for i in l:
            area = self.__pi*(float(i)*float(i))
            print(area)
    #parameterized constructor to find perimeter            
    def perimeter_circle(self,l):
        print("Perimeter for the list")
        for i in l:
            perimeter= 2* self.__pi*i
            print(perimeter)

#creating an object and calling the methods
obj1 = circle()
list1=
obj1.area_circle(list1)
obj1.perimeter_circle(list1)
