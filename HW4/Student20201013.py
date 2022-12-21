#!/usr/bin/python3
import sys
import numpy as np
from os import listdir
import operator

test = sys.argv[2]
training = sys.argv[1]
trainingData = listdir(training)
testData = listdir(test)

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
  
def createDataSet(dataset):
    dlen = len(trainingData)
    group = np.zeros((dlen, 1024))
    labels = []

    for i in range(dlen):
      fName = trainingData[i]
      label = int(fName.split('_')[0])
      labels.append(label)
      group[i, :] = readFile(dataset + '/' + fName)

    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1))-dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
  
def readFile(fName):
	vector = np.zeros((1, 1024))

	with open(fName) as f:
		for i in range(32):
			str = f.readline()
			for j in range(32):
				vector[0, 32 * i + j] = int(str[j])
	return vector

group, labels = createDataSet(training)


for k in range(1, 21):
  total = 0
  fail = 0

  for i in range(len(testData)):
    testData = readFile(test + '/' + testData[i])
    answer = int(testData[i].split('_')[0])
    expect = classify0(testData, group, labels, k)

    if answer != expect:
      fail += 1
    total += 1
  error = int((fail / total) * 100)
	
  print(error)
