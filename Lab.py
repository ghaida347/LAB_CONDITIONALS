movie:str = "Titanic"
rating:int=1.99
popularity_score:float= 72.65

if rating >= 4 and popularity_score > 80:
    print("Highly recommended")
elif rating >= 3 and popularity_score > 70:
    print("I recommended it . It is good")
elif rating >= 2 and popularity_score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
