#####################
# k-means:kmeans cluster
# arthor : liuzhao
# Date:2015-08-18
#####################

from numpy import *
import time
from kmeans import *
import matplotlib.pyplot as plt


## step 1: load date
print "step 1:load data...."
dataSet = []
fileIn = open('/Users/liuzhao/Documents/GitSpace/PythonDairy/Code/ML/testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split(' ')
	while '' in lineArr:
		lineArr.remove('')
	dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering.....
dataSet = mat(dataSet)
k = 4
centroids,clusterAssment = kmeans(dataSet, k)

## show the result
print "step 3:show the result"
showCluster(dataSet, k, centroids, clusterAssment)
