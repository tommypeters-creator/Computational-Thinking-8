input("lets see who you are more like, i will ask five questions")
riley_points=0
tommy_points=0
gideon_points=0

answer1 = input(r"what is your fav music type out of these options. (make sure to use the number)    1.rap     2.heavy_metal     3.punk_rock ")
if answer1 == "1":
    gideon_points +=1
if answer1 == "2":
    riley_points +=1
if answer1 == "3":
    tommy_points +=1
input("great")

answer2 = input(r".what is your fav sport to watch out of these options (make sure to use the number)    1.lacrosse   2. Sumo  ")
if answer2 == "1":
    gideon_points +=1 and tommy_points
if answer2 == "2":
    riley_points +=1

    
input("great")

answer2 = input(r".what is your fav sport to play out of these options (make sure to use the number)    1.lacrosse   2. football   3. Soccer ")
if answer2 == "1":
    gideon_points +=1
if answer2 == "2":
    riley_points +=1
if answer2 == "3":
    tommy_points +=1

answer3 = input(r".fav color out of these options (make sure to use the number)    1.blue   2.red   3.green ")
if answer3 == "1":
    gideon_points +=1
if answer3 == "2":
    riley_points +=1
if answer3 == "3":
    tommy_points +=1

answer4 = input(r".do you like dogs or cats (make sure to use the number)    1.like dogs   2.sorta like dogs 3.hate dogs ")
if answer4 == "1" or "2":
    gideon_points +=1
    tommy_points +=1
if answer4 =="3":
    riley_points +=1

answer5 = input(r".fav video game out of these options (make sure to use the number)    1. fortnite  2. sea of thieves   3. GTA ")
if answer5 == "1":
    gideon_points +=1
if answer5 == "2":
    riley_points +=1
if answer5 == "3":
    tommy_points +=1

print(f"u got {tommy_points} tommy score")
print(f"u got {riley_points} riley score")
print(f"u got {gideon_points} Gideon score")
print("whichever you got the most of is who you are more alike")