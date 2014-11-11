#Challenge_5_2
#Dennis Gordick
#11/11/2014
points=30
STR=0
HLTH=0
WIS=0
DEX=0
yes="go"
print("Hello. You have 30 points to spend on 4 atributes. Strength, Health, Wisdom, and Dexterity. To select the atribute you want to edit, say the first letter of it. Then say take or add. Add puts more into it, while take takes away. Then finaly, enter the number of points you want to change it by. To exit and stop, just press enter with nothing typed in")
while yes!="":
    print("Points left:",str(points))
    atr=input("What atribute? S(trength), H(ealth), W(isdom), D(exterity), or nothing to quit")
    if atr=="S":
          print("Strength:",str(STR))
          add_take=input("Are you add(ing) or take(ing)?")
          if add_take=="add":
              print("You said add")
              if int(points)>0:
                  print("Points left:",str(points))
                  spend=input("How many do you want to add?")
                  if int(spend)<=int(points):
                      STR=int(STR)+int(spend)
                      points=int(points)-int(spend)
                  else:
                      print("You dont have enuff points")
                      
              else:
                  print("You dont have enuff points...")
          elif add_take=="take":
              print("You said take")
              if int(STR)==0:
                  print("You dont have enuff points to take...")
              else:
                  print("Strngth:",str(STR))
                  take=input("How many points do you want to take?")
                  if int(take)<=int(STR):
                      STR=int(STR)-int(take)
                      points=int(points)+int(take)
                  else:
                      print("You dont have enuff points to take.")
    elif atr=="H":
          print("Health:",str(HLTH))
          add_take=input("Are you add(ing) or take(ing)?")
          if add_take=="add":
              print("You said add")
              if int(points)>0:
                  print("Points left:",str(points))
                  spend=input("How many do you want to add?")
                  if int(spend)<=int(points):
                      HLTH=int(HLTH)+int(spend)
                      points=int(points)-int(spend)
                  else:
                      print("You dont have enuff points")
                      
              else:
                  print("You dont have enuff points...")
          elif add_take=="take":
              print("You said take")
              if int(HLTH)==0:
                  print("You dont have enuff points to take...")
              else:
                  print("Health:",str(HLTH))
                  take=input("How many points do you want to take?")
                  if int(take)<=int(STR):
                      HLTH=int(HLTH)-int(take)
                      points=int(points)+int(take)
                  else:
                      print("You dont have enuff points to take.")
    elif atr=="W":
          print("Wisdom:",str(WIS))
          add_take=input("Are you add(ing) or take(ing)?")
          if add_take=="add":
              print("You said add")
              if int(points)>0:
                  print("Points left:",str(points))
                  spend=input("How many do you want to add?")
                  if int(spend)<=int(points):
                      WIS=int(WIS)+int(spend)
                      points=int(points)-int(spend)
                  else:
                      print("You dont have enuff points")
                      
              else:
                  print("You dont have enuff points...")
          elif add_take=="take":
              print("You said take")
              if int(WIS)==0:
                  print("You dont have enuff points to take...")
              else:
                  print("Wisdom:",str(WIS))
                  take=input("How many points do you want to take?")
                  if int(take)<=int(WIS):
                      WIS=int(WIS)-int(take)
                      points=int(points)+int(take)
                  else:
                      print("You dont have enuff points to take.")
    elif atr=="D":
          print("Dexterity:",str(DEX))
          add_take=input("Are you add(ing) or take(ing)?")
          if add_take=="add":
              print("You said add")
              if int(points)>0:
                  print("Points left:",str(points))
                  spend=input("How many do you want to add?")
                  if int(spend)<=int(points):
                      DEX=int(DEX)+int(spend)
                      points=int(points)-int(spend)
                  else:
                      print("You dont have enuff points")
                      
              else:
                  print("You dont have enuff points...")
          elif add_take=="take":
              print("You said take")
              if int(DEX)==0:
                  print("You dont have enuff points to take...")
              else:
                  print("Dexterity:",str(DEX))
                  take=input("How many points do you want to take?")
                  if int(take)<=int(DEX):
                      DEX=int(DEX)-int(take)
                      points=int(points)+int(take)
                  else:
                      print("You dont have enuff points to take.")
    elif atr=="":
          yes=""
    else:
          print("Please try again")
print("Strngth:",str(STR))
print("Health:",str(HLTH))
print("Wisdom:",str(WIS))
print("Dexterity:",str(DEX))
