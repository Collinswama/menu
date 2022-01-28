steak_treat = {"Bovian" : ["Ox", "Liver", "Stripes"],
              "Goat" : ["Ribs", "Leg", "Tanuip"],
              "Pork" :["Beacon", "Patch", "Minced"]}

vegan_treat = {"Harsh" : ["Kales", "Pig weed", "Cabbage"],
              "Smooth" : ["Corriander", "Managu", "Cheda"]}

thirsts = {"Bourbon" : ["Gunslinger", "Ramleek", "Orchidreap"],
          "Whisky" : ["Matei", "Emaltechj", "Urghichv"],
          "Childies" : ["Pepsi", "Cola", "Minute Maid"],
          "Dressings" : ["Souvinghon", "LeItaliano", "Granipe Red"]}


def processing(order):
    if order == "Bovian" or "Goat" or "Pork":
        return steak_treat
    elif order == "Harsh" or "Smooth":
        return vegan_treat
    elif order == "Bourbon" or "Whisky" or "Childies" or "Dressings":
        return thirsts
    
   


processing("Smooth")
