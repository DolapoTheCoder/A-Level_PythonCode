def calculatePoints(score):
    points = 0
    for n in range(0,len(score)):
        if score[n] == "W":
            points = points + 2
        elif score[n] == "D":
            points = points + 1
    return points
myscore = ["W","L","D"]
result = calculatePoints(myscore)
print("Points scored: ", result)
