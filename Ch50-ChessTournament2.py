def playerStats(names, scores):
    lowerCount = []
    for j in range(len(names)):
        count = 0
        for k in range(len(names)):
            if scores[k] < scores[j]:
                count = count + 1
        lowerCount.append((names[j], count))
    return lowerCount

names = ["Adam", "Ben", "Carol","Davina","Enid","Fred","George","Henry","Ian","Jane","Keith"]
scores = [14, 3, 21, 14, 15, 10, 20, 6, 10, 12, 10]
lowerCount = playerStats(names, scores)
for n in range(len(names)):
    print(lowerCount[n][0], lowerCount[n][1])
    
