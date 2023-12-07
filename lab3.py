# making menu of given site
print("menu\n 1.WELCOME TO THE AMANDO SHOPPING SITE\n 2.ADD A PRODUCT TO THE cart\n 3.DELETE A PRODUCT FROM THE cart\n 4.DISPLAY THE CONTENT OF THE CART 5.Purchase items\n 6.EXIT")
given_num=int(input("enter number from menu: "))
shoppingcart={}

while (given_num!=6):
    if given_num==1:
        product_name=input("enter product name: ")
        product_price=int(input("enter product price: "))
        shoppingcart[product_name]={"product_price":product_price}
        print("added",product_name)
        print("price:",product_price)
        print(shoppingcart)
        
        
    elif given_num==2:
        searchproduct=input("enter product name that search: ")  
        if searchproduct in shoppingcart:
            print("found:",shoppingcart[searchproduct])
            print(shoppingcart)
        else:
            print("No product exists with this name")  
            
    elif given_num==3:
        a=input("enter product name to delete: ")  
        del shoppingcart[a]  
        if shoppingcart is None:
            print("No product exists with this name")
            if product_name is not shoppingcart: 
                print("Product not found in cart") 
                
    elif given_num ==4:
        if shoppingcart=={}:
         print("shopping cart is empty")
        else:
            print(shoppingcart)
            
    elif given_num==6: 
       print("NOW you are exiting the menu")
       
       
    print("menu\n 1.WELCOME TO THE AMANDO SHOPPING SITE\n 2.ADD A PRODUCT TO THE cart\n 3.DELETE A PRODUCT FROM THE cart\n 4.DISPLAY THE CONTENT OF THE CART 5.Purchase items\n 6.EXIT")
    given_num=int(input("enter number from menu: "))               
    
                
                 
            
            
  
    
