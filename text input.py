from PIL import Image
a=input("enter the word:")

if a=="prepare the sandwiches":
    print("step 1:Bring the saucer and knife")
    print("step 2:Bring bread and cheese from the fridge")
    print("step 3:Remove the bread from the bag")
    print("step 4:Open the cheese tray and help it")
    print("step 5: Put the cheese on the bread")
    
    img1=Image.open("D:\speech\image\sw.jpg")
    img2=Image.open("D:\speech\image\sw2.jpg")
    img3=Image.open("D:\speech\image\bared.jpg")
    #img1.show()
    img2.show()
    img2.show()

elif a=="Make the bed":
    print("step 1:Remove the folds from the bottom of the bed cover")
    print("step 2:Drag the top of the cover to the front of the bed")
    print("step 3:Make sure the top cover is mounted on the side of the bed")
    print("step 4:Place the headrests on the front of the bed")
    print("step 5:Pull the front end to the front of the bed")
    
    #img1=Image.open("D:\speech\image\bad.jpg")
    img2=Image.open("D:\speech\image\write1.jpg")
    #img3=Image.open("D:\speech\image\bad1.jpg")
    img1.show()
    img2.show()
    #img3.show()

    
    
    
elif a=="Drink water":
    print("step 1:Bring the water cannula from the refrigerator")
    print("step 2:Put it on the table")
    print("step 3:Bring the cup")
    print("step 4:Pour water into the cup")
    print("step 5:Drink water")
    
    img1=Image.open("D:\speech\image\drink water.jpg")
    img2=Image.open("D:\speech\image\water2.jpg")
    img3=Image.open("D:\speech\image\water.jpg")
    img1.show()
    img2.show()
    img3.show()

    

elif a=="write":
    print("step 1:Bring the notebook from the bag")
    print("step 2:Bring the pen")
    print("step 3:Write the pen on the book")
    
    img1=Image.open("D:\speech\image\pen.jpg")
    img2=Image.open("D:\speech\image\pen2.jpg")
    img3=Image.open("D:\speech\image\write1.jpg")
    img1.show()
    img2.show()
    img3.show()
    
else:
    print("Sorry Not Found -_-")
