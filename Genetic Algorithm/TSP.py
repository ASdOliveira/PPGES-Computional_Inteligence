"""
University of Pernambuco - PPGES
Travel Salesman Problem using python
Solved by: Arysson Oliveira
Teacher: Carmelo bastos
"""
import fileText
import population
import calculate

#Import the cities
listOfCities = fileText.readDB()

fileText.writeDB("initializing")

############### "Defines" #####################
cityQtd = 52 #quantity of cities that will be used
popQtd = 10000
NumInteracoesCertas  = 10000
NumInteracoesTotal = 20000
fitvalue = 0
bestRoute = []
k = 0
j = 0
counterInt = 0
dist = [0]*popQtd
stopCondition = False
percentOfElit = 0.2

cities = [] #create an empty list with cityQtd elements.
pop = []
pop = list(pop)


#carry the amount of city chosen 
if (cityQtd != 52):
    for i in range(cityQtd):
        cities.append(listOfCities[i])
else:
    cities = listOfCities

for i in range(popQtd):
    pop.append(population.createPop(cities))
########################################

########### main::
while stopCondition == False :

    for i in range(len(pop)): #calculate the fit value to all vector
        dist = list(dist)
        dist[i] = calculate.fitness(pop[i])
    
    #sort the distance and pop in ascending order from the fit value
    dist, pop = zip(*sorted(zip(dist, pop))) 

    if(fitvalue == 0): #initial value
        fitvalue = dist[0]
        bestRoute = pop[0]
    else:
        if dist[0] < fitvalue:  
            fitvalue = dist[0]
            bestRoute = pop[0]
            k = 0
            j = j + 1
            #fileText.writeDB("j value: " + str(j)) #prints into TXT
        else:
            pop = list(pop)
            for i in range(int(percentOfElit*(len(pop)))): 
                pop[i] = population.crossover(pop[i],pop[i+1])
                pop[i] = population.mutation(pop[i])
           # fileText.writeDB("k value: " + str(k))
           # fileText.writeDB ("fitvalue: " + str(fitvalue))
            k = k + 1
            j = 0
    counterInt = counterInt + 1
    if counterInt >= NumInteracoesTotal:
        stopCondition = True
    if k >= NumInteracoesCertas: 
        stopCondition = True
fileText.writeDB("counterInt: " + str(counterInt))
fileText.writeDB("Interacoes corretas: " + str(NumInteracoesCertas))
fileText.writeDB("Last Fitvalue: " + str(fitvalue))
fileText.writeDB("Last BestRoute" + str(bestRoute))