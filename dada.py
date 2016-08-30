import csv
import sys
from itertools import chain, combinations
from collections import defaultdict
import collections
from operator import itemgetter
import math
from random import randint
import numpy as np
import copy
import itertools
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def dataFromFile(fname):
        file_iter = open(fname, 'rU')
        for line in file_iter:
                line = line.strip().rstrip(',')       # Remove trailing comma
                record = line.split(',')
                # print record
                yield record    

def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = record
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))   # Generate 1-itemSets
    return itemSet, transactionList

def getAttributes(itemSet, transactionList):
    C1 = list()
    C2 = list()
    C3 = list()
    C4 = list()
    C5 = list()
    C6 = list()
    C7 = list()
    C8 = list()
    C9 = list()
    C10 = list()
    C11 = list()
    C12 = list()
    C13 = list()
    C14 = list()
    C15 = list()
    key = 0
    dummy = 0
    for transactions in transactionList:
        if list(transactions)[0] in C1: dummy += 1
        else : C1.append(list(transactions)[0])
        if list(transactions)[1] in C2: dummy += 1
        else : C2.append(list(transactions)[1])
        if list(transactions)[2] in C3: dummy += 1
        else : C3.append(list(transactions)[2])
        if list(transactions)[3] in C4: dummy += 1
        else : C4.append(list(transactions)[3])
        if list(transactions)[4] in C5: dummy += 1
        else : C5.append(list(transactions)[4])
        if list(transactions)[5] in C6: dummy += 1
        else : C6.append(list(transactions)[5])
        if list(transactions)[6] in C7: dummy += 1
        else : C7.append(list(transactions)[6])
        if list(transactions)[7] in C8: dummy += 1
        else : C8.append(list(transactions)[7])
        if list(transactions)[8] in C9: dummy += 1
        else : C9.append(list(transactions)[8])
        if list(transactions)[9] in C10: dummy += 1
        else : C10.append(list(transactions)[9])
        if list(transactions)[10] in C11: dummy += 1
        else : C11.append(list(transactions)[10])
        if list(transactions)[11] in C12: dummy += 1
        else : C12.append(list(transactions)[11])
        if list(transactions)[12] in C13: dummy += 1
        else : C13.append(list(transactions)[12])
        if list(transactions)[13] in C14: dummy += 1
        else : C14.append(list(transactions)[13])
    return C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14

def buildPieChart(supportSet):
    from pylab import *
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = []
    fracs = []
    explode= []
    nn = 0
    for items, value in supportSet.items() : 
        labels.append(items) 
        fracs.append(value)
    while nn < len(itemSet):
        explode.append(0.2)
        nn += 1
    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90)
    show()

def getSupportOfAllItems(itemSet, transactionList):
        freqSet = defaultdict(int)
        _itemSet = set()
        localSet = defaultdict(int)
        x = 0.00
        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1
        for item, count in localSet.items():
            support = float(count)/len(transactionList)
            localSet[item] = support
            # print item, support                    
        return localSet

def getSupportOfItems(localSet, transactionList, multipleItems):
        count = 0
        for transactions in transactionList:
            if multipleItems.issubset(transactions):
                    count += 1
        support = float(count)/len(transactionList)
        return support

def getConfidenceOfRule(localSet, transactionList, antecedent, consequent):
    support_xUy = getSupportOfItems(localSet, transactionList, antecedent | consequent)
    support_x = getSupportOfItems(localSet, transactionList, antecedent)
    confidence = support_xUy/support_x
    # print('%.15f' % confidence) 
    # print count2 
    return confidence

def getLiftOfRule(localSet, transactionList, antecedent, consequent):
    support_xUy = getSupportOfItems(localSet, transactionList, antecedent | consequent)
    support_x = getSupportOfItems(localSet, transactionList, antecedent)
    support_y = getSupportOfItems(localSet, transactionList, consequent)
    lift = support_xUy/(support_x*support_y)
    return lift

def getFitness(localSet, transactionList, antecedent, consequent):
    support_xUy = getSupportOfItems(localSet, transactionList, antecedent | consequent)
    support_x = getSupportOfItems(localSet, transactionList, antecedent)
    fitness = ((1 + support_xUy)*(1 + support_xUy))/(1 + support_x)
    return fitness

def int2bin(i, fill):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s.zfill(fill)

def lengthOfBits():
    print len(C1), int(math.ceil(math.log10(len(C1))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C1))/math.log10(2))))
    print len(C2), int(math.ceil(math.log10(len(C2))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C2))/math.log10(2))))
    print len(C3), int(math.ceil(math.log10(len(C3))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C3))/math.log10(2))))
    print len(C4), int(math.ceil(math.log10(len(C4))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C4))/math.log10(2))))
    print len(C5), int(math.ceil(math.log10(len(C5))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C5))/math.log10(2))))
    print len(C6), int(math.ceil(math.log10(len(C6))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C6))/math.log10(2))))
    print len(C7), int(math.ceil(math.log10(len(C7))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C7))/math.log10(2))))
    print len(C8), int(math.ceil(math.log10(len(C8))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C8))/math.log10(2))))
    print len(C9), int(math.ceil(math.log10(len(C9))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C9))/math.log10(2))))
    print len(C10),int(math.ceil(math.log10(len(C10))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C10))/math.log10(2))))
    print len(C11),int(math.ceil(math.log10(len(C11))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C11))/math.log10(2))))
    print len(C12),int(math.ceil(math.log10(len(C12))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C12))/math.log10(2))))
    print len(C13),int(math.ceil(math.log10(len(C13))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C13))/math.log10(2))))
    print len(C14),int(math.ceil(math.log10(len(C14))/math.log10(2))), pow(2,int(math.ceil(math.log10(len(C14))/math.log10(2))))

def encode(listOfAttribute):
    bits = 0
    if pow(2,int(math.ceil(math.log10(len(listOfAttribute))/math.log10(2)))) > len(listOfAttribute):
        bits = int(math.ceil(math.log10(len(listOfAttribute))/math.log10(2)))
    if pow(2,int(math.ceil(math.log10(len(listOfAttribute))/math.log10(2)))) == len(listOfAttribute):
        bits = int(math.ceil(math.log10(len(listOfAttribute))/math.log10(2))) 
    bits += 1
    power = pow(2,bits)
    encoded_data = []
    encoded_set = defaultdict(list)
    i = 1
    for items in listOfAttribute:
        encoded_set[int2bin(i, bits)] = items
        i += 1
    while i < power:
        encoded_set[int2bin(i, bits)] = "phi"
        i += 1
    # print  bits, i 
    return encoded_set
   
def generatePopulation(size, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14):
    #chromosome C1 C2 C3 ...................... C13 C14 C15
    E1 = encode(C1)
    E2 = encode(C2)
    E3 = encode(C3)
    E4 = encode(C4)
    E5 = encode(C5)
    E6 = encode(C6)
    E7 = encode(C7)
    E8 = encode(C8)
    E9 = encode(C9)
    E10 = encode(C10)
    E11 = encode(C11)
    E12 = encode(C12)
    E13 = encode(C13)
    E14 = encode(C14)
    initPop = {}

    def randomChromosome(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14) : 
        chromosome = list()
        randomNumber = randint(0,len(E1)-1)     # np.random.randint(0,len(E1)-1)
        chromosome.append(E1.keys()[randomNumber])
        randomNumber = randint(0,len(E2)-1)
        chromosome.append(E2.keys()[randomNumber])
        randomNumber = randint(0,len(E3)-1)
        chromosome.append(E3.keys()[randomNumber])
        randomNumber = randint(0,len(E4)-1)
        chromosome.append(E4.keys()[randomNumber])
        randomNumber = randint(0,len(E5)-1)
        chromosome.append(E5.keys()[randomNumber])
        randomNumber = randint(0,len(E6)-1)
        chromosome.append(E6.keys()[randomNumber])
        randomNumber = randint(0,len(E7)-1)
        chromosome.append(E7.keys()[randomNumber])
        randomNumber = randint(0,len(E8)-1)
        chromosome.append(E8.keys()[randomNumber])
        randomNumber = randint(0,len(E9)-1)
        chromosome.append(E9.keys()[randomNumber])
        randomNumber = randint(0,len(E10)-1)
        chromosome.append(E10.keys()[randomNumber])
        randomNumber = randint(0,len(E11)-1)
        chromosome.append(E11.keys()[randomNumber])
        randomNumber = randint(0,len(E12)-1)
        chromosome.append(E12.keys()[randomNumber])
        randomNumber = randint(0,len(E13)-1)
        chromosome.append(E13.keys()[randomNumber])
        randomNumber = randint(0,len(E14)-1)
        chromosome.append(E14.keys()[randomNumber])
        return chromosome
    
    i = 0
    while len(initPop) < size:
        initPop[i] = randomChromosome(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14)
        i += 1
    # print initPop
    return initPop

def crossover(chromosome1,chromosome2):
    chr1 = []
    chr2 = []
    i = 0

    def crossoverGene(gene1, gene2):
        length = len(gene1.split()[0])
        crossoverPoint = int(math.ceil((length+1)/2))
        childChromosome1 = []
        childChromosome2 = []
        childChromosome1.append(gene1.split()[0][0:crossoverPoint])
        childChromosome1.append(gene2.split()[0][crossoverPoint:length])
        childChromosome2.append(gene2.split()[0][0:crossoverPoint])
        childChromosome2.append(gene1.split()[0][crossoverPoint:length])
        # print gene1.split()[0]
        # print gene2.split()[0]
        # print gene1, childChromosome1
        # print gene2, childChromosome2
        childChromosome1  = [''.join(childChromosome1[0:2])]
        childChromosome2  = [''.join(childChromosome2[0:2])]
        # print gene1, childChromosome1
        # print gene2, childChromosome2
        return childChromosome1, childChromosome2
    while i < 14:
        x, y = crossoverGene(chromosome1[i], chromosome2[i])
        chr1.append(x)
        chr2.append(y)
        i+=1
    return chr1, chr2

def decode(chromosome, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14):
    E1 = encode(C1)
    E2 = encode(C2)
    E3 = encode(C3)
    E4 = encode(C4)
    E5 = encode(C5)
    E6 = encode(C6)
    E7 = encode(C7)
    E8 = encode(C8)
    E9 = encode(C9)
    E10 = encode(C10)
    E11 = encode(C11)
    E12 = encode(C12)
    E13 = encode(C13)
    E14 = encode(C14)
    # print E1
    items = []
    for key, val in E1.items():
        if key == chromosome[0]:
            items.append(val)
    for key, val in E2.items():
        if key == chromosome[1]:
            items.append(val)
    for key, val in E3.items():
        if key == chromosome[2]:
            items.append(val)
    for key, val in E4.items():
        if key == chromosome[3]:
            items.append(val)
    for key, val in E5.items():
        if key == chromosome[4]:
            items.append(val)
    for key, val in E6.items():
        if key == chromosome[5]:
            items.append(val)
    for key, val in E7.items():
        if key == chromosome[6]:
            items.append(val)
    for key, val in E8.items():
        if key == chromosome[7]:
            items.append(val)
    for key, val in E9.items():
        if key == chromosome[8]:
            items.append(val)
    for key, val in E10.items():
        if key == chromosome[9]:
            items.append(val)
    for key, val in E11.items():
        if key == chromosome[10]:
            items.append(val)
    for key, val in E12.items():
        if key == chromosome[11]:
            items.append(val)
    for key, val in E13.items():
        if key == chromosome[12]:
            items.append(val)
    for key, val in E14.items():
        if key == chromosome[13]:
            items.append(val)
    # print items
    randomNumber = randint(0,13)
    items.insert(randomNumber, 'break')
    items = [x for x in items if x != 'phi']
    # print items
    return items

def mutate(chromosome1, chromosome2):
    index1 = chromosome1.index('break')
    index2 = chromosome2.index('break')
    chromosome1.remove('break')
    chromosome2.remove('break')
    chromosome1.insert(index2, 'break')
    chromosome2.insert(index1, 'break')
    return chromosome1, chromosome2

def checkIfBreakIsAtEnds(chromosome):
    index = chromosome.index('break')
    if (index == 0) or (index == len(chromosome)-1):
        return 1
    else:
        return 0

def separateChromosome(chromosome):
    emptyList = []
    index = chromosome.index('break')
    if (index == 0):
        return emptyList, chromosome[1:len(chromosome)]
    if (index == len(chromosome)):
        return chromosome[0:len(chromosome)], emptyList
    else:
        return chromosome[0:index], chromosome[(index+1):len(chromosome)]

def joinChromosome(antecedent, consequent):
    joinChr = []
    joinChr = [antecedent] + [consequent]
    return joinChr

def joinChromosomeForNext(antecedent, consequent):
    joinChr = []
    joinChr = antecedent + consequent
    return joinChr

def createParentFromChild(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, newlist):
    offsppring = ['phi','phi','phi','phi','phi','phi','phi','phi','phi','phi','phi','phi','phi','phi']
    dicttion = defaultdict()
    for listitem in newlist: 
        if listitem in C1: offsppring[0] = listitem
        if listitem in C2: offsppring[1] = listitem
        if listitem in C3: offsppring[2] = listitem
        if listitem in C4: offsppring[3] = listitem
        if listitem in C5: offsppring[4] = listitem
        if listitem in C6: offsppring[5] = listitem
        if listitem in C7: offsppring[6] = listitem
        if listitem in C8: offsppring[7] = listitem
        if listitem in C9: offsppring[8] = listitem
        if listitem in C10: offsppring[9] = listitem
        if listitem in C11: offsppring[10] = listitem
        if listitem in C12: offsppring[11] = listitem
        if listitem in C13: offsppring[12] = listitem
        if listitem in C14: offsppring[13] = listitem

    return offsppring

def functionForOneGeneration(initPop, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14):

    popoForNextGen = []
    popoToExamineThisGen = []
    nan = 0
    while nan < (len(initPop)-1):
        x,y = crossover(initPop[nan],initPop[nan+1])
        decodedRule1 = decode(list(chain.from_iterable(x)), C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14)
        decodedRule2 =  decode(list(chain.from_iterable(y)), C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14)
        decodedRule1, decodedRule2 = mutate(decodedRule1, decodedRule2)

        antecedent, consequent = separateChromosome(decodedRule1)            
        newPop[nan] = joinChromosome(antecedent, consequent)
                        
        antecedent, consequent = separateChromosome(decodedRule2)    
        newPop[nan+1] = joinChromosome(antecedent, consequent)
        nan += 1
    i = 0
    for key, value in newPop.items():
        # print i, key, value
        popoToExamineThisGen.append(value)
        popoForNextGen.append(createParentFromChild(C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, joinChromosomeForNext(value[0], value[1])))
        i+=1
    return popoToExamineThisGen,popoForNextGen

def encodechild(C, gen):
    encoded_set = encode(C)
    for k, v in encoded_set.items():
        if v == gen:
            return k

def encodeChildChromosome(popSize, gen1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14):
    popo = []
    z=0
    while z<popSize:
        childlist = [encodechild(C1, gen1[z][0]), encodechild(C2, gen1[z][1]), encodechild(C3, gen1[z][2]), encodechild(C4, gen1[z][3]),
        encodechild(C5, gen1[z][4]), encodechild(C6, gen1[z][5]), encodechild(C7, gen1[z][6]), encodechild(C8, gen1[z][7]),
        encodechild(C9, gen1[z][8]), encodechild(C10, gen1[z][9]), encodechild(C11, gen1[z][10]), encodechild(C12, gen1[z][11]), 
        encodechild(C13, gen1[z][12]),encodechild(C14, gen1[z][13])]
        popo.append(childlist)
        z+=1
    return popo

def getBestFromThisIteration(popoToExamineThisGen, supportSet, transactionList):
    usefulRules = []
    for t in popoToExamineThisGen:
        if (len(t[0]) == 0) or (len(t[1]) == 0) :
            dummy = 1
        else:
            antecedent, consequent = t[0], t[1]
            try:
                if getSupportOfItems(supportSet, transactionList, set(list(antecedent))) == 0.0 or getSupportOfItems(supportSet, transactionList, set(list(consequent))) == 0.0 or getConfidenceOfRule(supportSet, transactionList, set(list(antecedent)),set(list(consequent))) == 0.0:
                    dummy  = 1
                else:
                    # print getLiftOfRule(supportSet, transactionList, set(list(antecedent)), set(list(consequent))), antecedent, consequent, getFitness(supportSet, transactionList, set(list(antecedent)), set(list(consequent))), getConfidenceOfRule(supportSet, transactionList, set(list(antecedent)),set(list(consequent)))
                    # newPop[getFitness(supportSet, transactionList, set(list(antecedent)), set(list(consequent)))] = joinChromosome(antecedent, consequent)
                    usefulRules.append(t)
            except ZeroDivisionError:
                dummy = 1
    return usefulRules

def makeUseOfRules(usefulRules, supportSet, transactionList):
    i=0 
    fitness = 0
    for t in usefulRules:
        # print t[0], t[1], getFitness(supportSet, transactionList, set(list(t[0])), set(list(t[1])))
        fitness +=  getFitness(supportSet, transactionList, set(list(t[0])), set(list(t[1])))
        i+=1
    return fitness/i


popSize = 1000
x = dataFromFile("depdiv12.csv")
itemSet, transactionList = getItemSetTransactionList(x)
supportSet = getSupportOfAllItems(itemSet, transactionList)
C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14 = getAttributes(itemSet, transactionList)
newPop = {}

l = 0
s = generatePopulation(popSize, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14)
initPop = s
generation = 0
rulesInDifferentFeneration = []
fitnessOverGenerations = []
while generation<50:
    popoToExamineThisGen, gen1 = functionForOneGeneration(initPop, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14)
    initPop = encodeChildChromosome(popSize, gen1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14) 
    discussRules = getBestFromThisIteration(popoToExamineThisGen, supportSet, transactionList)
    rulesInDifferentFeneration.append(discussRules)
    fitnessOverGenerations.append(makeUseOfRules(discussRules, supportSet, transactionList)) 
    generation += 1
    # print "#####################################################################################################################"

for t in rulesInDifferentFeneration[fitnessOverGenerations.index(max(fitnessOverGenerations))] : 
    print t[0], t[1], getConfidenceOfRule(supportSet, transactionList, set(list(t[0])), set(list(t[1]))), getLiftOfRule(supportSet, transactionList, set(list(t[0])), set(list(t[1])))
print fitnessOverGenerations.index(max(fitnessOverGenerations))
# print len(fitnessOverGenerations)




# import numpy as np
# import matplotlib.pyplot as plt

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)

# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()




fitnessOverGenerations.insert(0,0)
objects = []
i=0
while i<len(fitnessOverGenerations):
    objects.append(i)
    i += 1
objects.append(i)
y_pos = np.arange(len(fitnessOverGenerations))
performance = fitnessOverGenerations
print objects, len(performance)
plt.plot(y_pos, performance, marker='o', linestyle='--', color='r')
# plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('fitness')
plt.title('generation')
plt.show()