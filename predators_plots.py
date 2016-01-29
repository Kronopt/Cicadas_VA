# -*- coding: cp1252 -*-

import pylab
import csv
import gc




# line on the CSV file where the necessary information is located
lineOfInterest = 28
# end file path with "\\" (escape character and actual slash)
locationOfFiles = 'Hybrid + Predator\Results\Predator Theory\Spreadsheets\\'
fileName_withoutIncrement = 'PREDATORS lifecycle '
# end file path with "\\" (escape character and actual slash)
outputLocation = 'Hybrid + Predator\Results\Predator Theory\Plots\\'




def histogram(figureObject, graphData):
    """
    Adds 2 histograms to an existent figure.
    Returns the max cycle for cicadas and predators.
    
    REQUIRES:
        figureObject is a matplotlib.figure.Figure object, obtained through pylab.figure().
        graphData is a  tuple (cicada, predator), data corresponding to ONE experiment.
        In the end, the given figure will have a grid 1X2 where both histograms will be inserted.
    ENSURES:
        Histograms added to the figure (figureObject).
        Returns a tuple (maxCicadaCycle, maxPredatorCycle).
    """

    representedCycles_Cicadas = sorted(set(graphData[0]))
    representedCycles_Predators = sorted(set(graphData[1]))
    countCicadasCycles = [0] * len(representedCycles_Cicadas)
    countPredatorsCycles = [0] * len(representedCycles_Predators)
    
    count = 0
    for i in representedCycles_Cicadas:
        for f in graphData[0]:
            if f == i:
                countCicadasCycles[count] += 1
        count += 1

    count = 0
    for i in representedCycles_Predators:
        for f in graphData[1]:
            if f == i:
                countPredatorsCycles[count] += 1
        count += 1

    # Cicada histogram
    barGraphCicadas = figureObject.add_subplot(1, 2, 1)
    barGraphCicadas.bar(representedCycles_Cicadas, countCicadasCycles)
    barGraphCicadas.set_xlabel('Lifecycle duration (years) Cicadas')
    barGraphCicadas.set_ylabel('Number of Cicadas')
    barGraphCicadas.set_xticks(representedCycles_Cicadas)

    # Predator histogram
    barGraphPredators = figureObject.add_subplot(1, 2, 2)
    barGraphPredators.bar(representedCycles_Predators, countPredatorsCycles)
    barGraphPredators.set_xlabel('Lifecycle duration (years) Predators')
    barGraphPredators.set_ylabel('Number of Predators')
    barGraphPredators.set_xticks(representedCycles_Predators)

    print '--- CICADAS ---'
    print 'Cicadas cycles:', representedCycles_Cicadas
    print 'Cicadas number:', countCicadasCycles
    print '--- PREDATORS ---'
    print 'Predators cycles:', representedCycles_Predators
    print 'Predators number:', countPredatorsCycles


    # Max cicadas' cycle
    maxCicadaCycle = 0
    currentMax = 0
    count = 0
    for i in countCicadasCycles:
        if i > currentMax:
            currentMax = i
            maxCicadaCycle = count
        count += 1

    # Max predators' cycle
    maxPredatorCycle = 0
    currentMax = 0
    count = 0
    for i in countPredatorsCycles:
        if i > currentMax:
            currentMax = i
            maxPredatorCycle = count
        count += 1

    if len(representedCycles_Cicadas) > 0 and len(representedCycles_Predators) > 0:
        return (representedCycles_Cicadas[maxCicadaCycle], representedCycles_Predators[maxPredatorCycle])
    elif len(representedCycles_Cicadas) == 0:
        return (0, representedCycles_Predators[maxPredatorCycle])
    elif len(representedCycles_Predators) == 0:
        return (representedCycles_Cicadas[maxCicadaCycle],0)




# ALTER RANGE DEPENDING ON THE NUMBER OF FILES IN THE DIRECTORY
for experiment in range(1,21):
    # [[int, int, int, ...], [int, int, ...], ...]
    cicadas = []
    predators = []

    with open(locationOfFiles + fileName_withoutIncrement + str(experiment) + '.csv', 'rb') as csvFile:
        data = csv.reader(csvFile, delimiter=',')

        # jump to the needed line
        for _ in range(lineOfInterest - 1):
            data.next()

        # excluding the first column (which is always empty), EVEN columns have cicada data and ODD columns have predator data
        count = 1
        for i in data.next():
            # removes leading "[" and trailing "]"
            trimmedString = i[2 : -2]
            if count != 1:
                if count % 2 == 0:
                    cicadas.append(trimmedString)
                else:
                    predators.append(trimmedString)
            count += 1;

    # translates strings in ints
    for i in xrange(len(cicadas)):
        if cicadas[i] != '':
            cicadas[i] = cicadas[i].split()
            cicadas[i] = map(int, cicadas[i])
        else:
            cicadas[i] = []
        if predators[i] != '':
            predators[i] = predators[i].split()
            predators[i] = map(int, predators[i])
        else:
            predators[i] = []




    cicadasCountCycles = [0] * 30
    cicadasNcycles = [0] * 30
    predatorsCountCycles = [0] * 30
    predatorsNcycles = [0] * 30
    
    # Creates and manipulates a figure object
    for i in range(len(cicadas)):
        print '---------- EXPERIMENT ' + str(experiment) + ' simulation ' + str(i + 1) + ' ----------'
        
        if i != []:
            finalFigure = pylab.figure()
            finalFigure.suptitle('Experiment ' + str(experiment) + ' simulation ' + str(i + 1))
            finalFigure.set_facecolor('w')


            # histogram function and max cycles
            maxCicadaCycle, maxPredatorCycle = histogramCicadasPredators = histogram(finalFigure, (cicadas[i], predators[i]))
            if maxCicadaCycle != 0:
                cicadasCountCycles[maxCicadaCycle] += 1
                cicadasNcycles[maxCicadaCycle] = maxCicadaCycle
            if maxPredatorCycle != 0:
                predatorsCountCycles[maxPredatorCycle] += 1
                predatorsNcycles[maxPredatorCycle] = maxPredatorCycle


            finalFigure.tight_layout()
            finalFigure.subplots_adjust(top = .9)
        else:
            finalFigure = pylab.figure()
            finalFigure.suptitle('Experiment ' + str(experiment) + ' simulation ' + str(i + 1))
            finalFigure.set_facecolor('w')

        pylab.savefig(outputLocation + fileName_withoutIncrement + str(experiment) + ' simulation ' + str(i + 1) + '.png')
        #pylab.show()

        finalFigure.clf()
        pylab.close()
        gc.collect()




    # Summary graph
    MaxFigure = pylab.figure()
    MaxFigure.suptitle('Experiment ' + str(experiment))
    MaxFigure.set_facecolor('w')

    # Cicada histogram
    barGraphCicadas = MaxFigure.add_subplot(1, 2, 1)
    barGraphCicadas.bar(cicadasNcycles, cicadasCountCycles)
    barGraphCicadas.set_xlabel('Lifecycle duration (years) Cicadas')
    barGraphCicadas.set_ylabel('Frequency of Cicadas')
    barGraphCicadas.set_xticks(cicadasNcycles)

    # Predator histogram
    barGraphPredators = MaxFigure.add_subplot(1, 2, 2)
    barGraphPredators.bar(predatorsNcycles, predatorsCountCycles)
    barGraphPredators.set_xlabel('Lifecycle duration (years) Predators')
    barGraphPredators.set_ylabel('Frequency of Predators')
    barGraphPredators.set_xticks(predatorsNcycles)

    print 'FINAL GRAPH'
    print '--- CICADAS ---'
    print 'Cicadas cycles:', cicadasNcycles
    print 'Cicadas number:', cicadasCountCycles
    print '--- PREDATORS ---'
    print 'Predators cycles:', predatorsNcycles
    print 'Predators number:', predatorsCountCycles

    MaxFigure.tight_layout()
    MaxFigure.subplots_adjust(top = .9)

    pylab.savefig(outputLocation + fileName_withoutIncrement + str(experiment) + '.png')
    
    finalFigure.clf()
    pylab.close()
    gc.collect()
