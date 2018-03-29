import csv
import random
import math
import operator

def loadDataset(file,split,train_set=[],test_Set=[]):
    with open(file,'rb') as csvfile:
        lines=csv.reader(csvfile)
        dataset=list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y]=float(dataset[x][y])
                if random.random()<split:
                    train_Set.append(dataset[x])
                else:
                    test_Set.append(dataset[x])
                    
                    
def euclidian_dis(ins1,ins2,len):
    dist=0
    for x in range(len):
        dist+=pow((ins1[x]-ins2[x]),2)
    return ath.sqrt(dist)
    
def getNeighbors(trainset,testinst,k):
    distan=[]
    length=len(testinst)-1;
    for x in range(len(trainset)):
        dist=euclidian_dis(testinst,trainset,length)
        distan.append((trainset[x],dist))
        distan.sort(key=operator.itemgetter(1))
        neighbours=[]
        for x in range(k):
            neighbours.append(distan[x][0])
        return neighbours
def response(neighbours):
    classVotes={}
    for x in range(len(neighbours)):
        respon=neighbours[x][-1]
        if respon in classVotes:
            classVotes[respon]+=1
        else:
            classVotes[respon]=1
    sortedVotes=sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]
    
def accuracy(testset,prediction):
    correct=0
    for x in range(len(testset)):
        if testset[x][-1]==predictions[x]:
            correct+=1
    return (correct/float(len(testset)))*100.0

def main():
    trainset=[]
    testset=[]
    split=0.67
    loadDataset('iris.csv',split,trainset,testset)
    print("Train Set:"+repr(len(trainset)))
    print("Test set:"+repr(len(testset)))
    predictions=[]
    k=3
    for x in range(len(testset)):
        neigh=neighbours(trainset,testset[x],k)
        result=response(neigh)
        predictions.append(result)
        print(">predicted="+repr(result)+"Actual="+repr(testset[x][-1]))
        accu=accuracy(testset,predictions)
        print("Accuracy:"+repr(accu)+"%")
        
        
main()        
    
    
        
