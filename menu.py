# project1, making a menu
#sort available delicaies into groups

def vegetables():
    {"Bitter": "kales",
    "soft": "Spinach", 
    "scented": "Corriander",
    "traditional": "pig weed"}
def carnivore():
    {"goat": "ribs",
    "beef": "steak",
    "mutton": "tail roast",
    "ostrich": "meatballs",
    "pork": "beacon",}  
def drinks():
    {"cold": ["coke", "drips"],
    "hot": ["camel chai", "expresso"],
    "smooth": ["lager", "dawa"],
    "burn": ["labels", "matei black"]}


# customer presentation

waiter = "What will you have today? "
customers = input()

if customers == "salads":
    vegetables()
elif customers == "meat":
    carnivore()
elif customers == "sips":
    drinks()    
