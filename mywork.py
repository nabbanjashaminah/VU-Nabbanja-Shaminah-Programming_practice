#loops
n=4
for i in range(0,n):
    print(i)


    for i in range(1,5):
        for j in range(i):
            print(i,end='')
    print()        


    #conditional statements
    age = 20
    if age>= 18:
        print("allowed to marry")


        age = 10
        if age <= 12:
            print("Travel for free")
        else:
            print("pay for ticket")

            #functions

        def add_numbers(j,k):
            return j+k

        result =add_numbers(5,2)
        print(result)


 #lambda
a  ="Nabbanja Shaminah"
upper= lambda x:x.upper()
print(upper(a))


#LISTS
a  =[1,2,3]
print(a)

b =["boy","girl"]
print(b)

a = list((1,2,3,'apple',2.5))
print(a)

b =list("MGH")
print(b)

x =[3]* 2
y =[0]* 6

print(x)
print(y)


#Tuples
tup =()
print()

# using string
li =[4,7,6,8]
print(tuple(li))

#Using Built_in Function
tup = tuple('shamie')
print(tup)


#dictionaries
data ={"name":"Nabbanja","age":20}
print(data)


a ={"z": 3,"y": 2}
print(a)


# numpy
import numpy as np

a1 = np.array([1,2,3]) # 1D

a2 =np.array([[1,2],[3,4]]) #2D

a3 =np.array([[[1,2],[3,4],[5,6],[7,8]]]) #3D

print(a1)
print(a2) 
print(a3)



a0 = np.zeros((3,3))
a1 = np.ones((2,2))
ar = np.arange(0,10,2)

print(a0)
print(a1)
print(ar)


x =np.array([1,2,3,4])
y =np.array([4,5,6,7])

print(x+y)
print(x-y)
print(x*y)
print(x/y)



    










        


            
            
            

            
            




                
