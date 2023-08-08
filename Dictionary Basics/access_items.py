#Access items of a dictionary.

#By referring to its keyname.
synonyms={
    "Beautiful": "Gorgeous",
    "Brave": "Intrepid",
    "Bright": "Radiant"
    }
x=synonyms["Beautiful"]
print("Value of the key 'Beautiful': "+str(x))

#Using get()
cars={
    "Brand":"BMW",
    "Model":"BMW X5"    
}
print("Value of the key 'Brand': "+str(cars.get("Brand")))
