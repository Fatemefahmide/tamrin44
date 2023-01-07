products=[]
f = open("4.txt","r") 
for line in f: 
    result=line.split(",") 
    my_dic={"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
    products.append(my_dic)



def show_menu():
    print("1-Remove")
    print("2-Edite")
  

def Remove():
    key=input("enter product code:")
    for product in products: 
        if product["id"] == key:
             products.remove(product) 
             print("kala  ba movafaghiat hazf shod")
             break
def Edite():
    key=input("enter product code: ")
    new_change=input("enter new change: ")
    print("which part to change? ")
    print("name")
    print("price")
    print("count")
    if user_choice== name:
       for product in products: 
           if product["id"] == key:
               product["name"]=new_change
               print(product)
               print("etelaat ba movafaghiat avas shod")
               break

    elif user_choice== price:
       for product in products: 
           if product["id"] == key:
              product["price"]=new_change
              print(product)
              print("etelaat ba movafaghiat avas shod")
              break 

    elif user_choice== count:
       for product in products: 
           if product["id"] == key:
              product["count"]=new_change
              print(product)
              print("etelaat ba movafaghiat berozresani shod")   
              break 



read_file()
show_menu()

user_choice= int(input("enter your choice: "))

if user_choice == 1:
    Remove()
elif user_choice == 2 :
    Edite()

else:
    print("select another number")