Suitors = [1, 2, 3]
Suitees = [[1, 0], [2, 0], [3, 0]]

SuitorsPrio = [[10, 9, 5], [8, 4, 3], [5, 3, 0]]
SuiteesPrio = [[10, 9, 10], [9, 4, 8], [2, 7, 10]]

free = [1, 2, 3]

while len(free) != 0:
    for i in range(len(Suitors)):
        propose = SuitorsPrio[i].index(max(SuitorsPrio[i]))
        SuitorsPrio[i][propose] = 0
        
        if Suitors[i] in free:
            if Suitees[propose][1] == 0:
                Suitees[propose][1] = Suitors[i]
                free.remove(Suitees[propose][1])

            elif Suitees[propose][1] != 0:
                if Suitees[propose][1] < SuiteesPrio[propose][i]:
                    free.append(Suitees[propose][1])
                    Suitees[propose][1] = Suitors[i]
                    free.remove(Suitors[i])

print(Suitees)