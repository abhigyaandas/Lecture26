items=["Pencil","Eraser","Notebook","Sharpner","Glue"]
stock=[10,4,0,13,6]

inventory={item:count for item,count in zip(items,stock)}
print(inventory)

in_stock_items=[item for item in items if inventory[item]>0]
print("Sutff in stock: ",in_stock_items )

prices=[5,3,10,7,12]
mark=int(input("Put in maked pricing otherwise no good"))

markupprice=list(map(lambda p:p+mark,prices))
print("New price, which is all your fault is ",markupprice)