'''
Other reference
https://en.wikipedia.org/wiki/ID3_algorithm

implementing a decision tree based off of this pseudocode
http://www.cs.cmu.edu/~bhiksha/courses/10-601/decisiontrees/
once this is implemented then it will be optimised using numpy

Algortithm :
1. Assign all training instances to the root of the tree.
    Set current node to root node.
2. For each feature
    a. Partition all data instances at the node by the value of the feature.
    b. Compute the information gain ratio from the partitioning.
3. Identify feature that results in the greatest information gain ratio.
    Set this feature to be the splitting criterion at the current node.
    If the best information gain ratio is 0, tag the current node as a leaf and return
4. Partition all instances according to attirbute value of the best feature
5. Denmote each partition as a child node of the current node.
6. For each child node:
    a. If the child node is "pure" (has instances from only one class) tag it as a leaf node and return
    b. If not set the child node as the current node and recurse to step 2.


'''

import pandas as pd
import numpy as np

def segregate(column, value):
    """
    This function returns the indices of a column which meet a certain value
    
    pseudocode:
    def segregate(featurearray, value):
    outlist = []
    for i = 1 to len(featurearray):
        if (featurearray[i] == value):
            outlist = [outlist, i] # Append "i" to outlist
    return outlist
    """
    output = np.array([])
    for i, element in enumerate(column):
        if (element == value):
            output = np.append(output,i)
    return output


    
def computeEntropy(labels):
    """
    This function computes entropy
    https://en.wikipedia.org/wiki/Entropy_(information_theory)

    pseudocode:
    def computeEntropy(labels):
    
    #Assuming labels take values 1..M.
    I take this to mean that there are M unique labels or classes

    entropy = 0
    for i = 1 to M:
        probability_i = length(segregate(labels, i)) / length(labels)
        entropy -= probability_i * log(probability_i)
    return entropy

    the input is a vector of labels

    """
    entropy = 0
    for i in np.unique(labels): 
        probability_i = len(segregate(labels, i)) / len(labels)
        entropy -= probability_i * np.log(probability_i)
    return entropy


def mostFrequentlyOccurringValue(labels):
    """
    # Find most frequent value. Assuming labels take values 1..M 
    def mostFrequentlyOccurringValue(labels):
    bestCount = -inf
    bestId = none
    for i = 1 to M:
        count_i = length(segregate(label,i))
        if (count_i > bestCount):
            bestCount = count_i
            bestId = i
    return bestId
    """

    bestCount = np.NINF #negative infinity
    bestId = None
    for i in np.unique(labels):
        count_i = len(segregate(labels,i))
        if (count_i > bestCount):
            bestCount = count_i
            bestId = i
    return bestId


#-------- The Dtree code ------------

#Here "features" is an Num-instance x Num-features matrix. Each row is
#one training instance.

#"labels" is a Num-instance x 1 array of class labels for the training instances

# Note, we're storing a number of seemingly unnecessary variables, but
# we'll use them later for counting and pruning


class  DecisionTree:
    def __init__(self, features, labels):
        """
        Initialises a decision tree
        Here "features" is an Num-instance x Num-features matrix. Each row is
        one training instance.

        "labels" is a Num-instance x 1 array of class labels for the training instances

        """
        self.nodeGainRatio = float
        self.nodeInformationGain = float
        self.isLeaf = bool 
        self.majorityClass = int
        self.bestfeature = int
        self.children = []
        self.parent = None
        print("features")
        print(features)
        print("labels")
        print(labels)
        self.buildTree (features, labels)

    def buildTree (self, features, labels):
        numInstances = len(labels)
        nodeInformation = numInstances * computeEntropy(labels)
        
        self.majorityClass = mostFrequentlyOccurringValue(labels)
        
        if (nodeInformation == 0):  # This is a "pure" node
            self.isLeaf = True
            return

        # First find the best feature for this node
        bestFeature = None
        bestInformationGain = np.NINF
        bestGainRatio = np.NINF
        # for each column in features
        for col_id, col_name in enumerate(features):
            column = features.iloc[:,col_id]
            conditionalInfo = 0
            featureEntropy = 0
            featureCount = np.array(range(numInstances)) # initialise an array
            print(f"column: \n{column}")                                            #of length num instances
            for idy, Y in enumerate(column):
                ids = segregate(column, Y) # get ids of all instances
                                      # for which feature X == Y
 
                featureCount[idy] = len(ids)
                conditionalInfo += featureCount[idy] * computeEntropy(labels[ids])
                print(f"conditionalInfo: {conditionalInfo}")
            featureInformationGain =  nodeInformation - conditionalInfo
            gainRatio = featureInformationGain / computeEntropy(featureCount)

            if (gainRatio > bestGainRatio):
                bestInformationGain = featureInformationGain
                bestGainRatio = gainRatio
                bestfeature = column

        #If no feature provides any gain, this node cannot be split further
        if (bestGainRatio == 0):
            self.isLeaf = True
            return
        
        # Otherwise split by the best feature
        self.bestfeature = bestfeature
        self.nodeGainRatio = bestGainRatio
        self.nodeInformationGain = bestInformationGain

        for idy, Y in enumerate(bestfeature):
            ids = segregate(bestfeature, Y)
            self.children.append(DecisionTree(features.iloc[ids,:], labels.iloc[ids]))
            self.children[idy].parent = self
        return
        


#testing
df = pd.read_csv("~/Documents/python_projects/rforest/iris.csv")
df = df.iloc[0:100,:]
features = df.iloc[:,:4]

labels = df['class'].astype('category').cat.codes

DecisionTree(features,labels)


column = df.petal_width[[51,55,66,68,78,84,85,106]]
labels = labels[[51,55,66,68,78,84,85,106]]
numInstances = len(labels)
conditionalInfo = 0
featureEntropy = 0
featureCount = np.array(range(len(column)))
nodeInformation = numInstances * computeEntropy(labels)
bestFeature = None
bestInformationGain = np.NINF
bestGainRatio = np.NINF
featureCount = np.array(range(numInstances))
for idy, Y in enumerate(column):
    print(f"idy: {idy}")
    print(f"Y: {Y}")
    ids = segregate(column, Y) # get ids of all instances
    print(f"ids: {ids}")
    featureCount[idy] = len(ids)
    print(f"featureCount: {featureCount}")
    conditionalInfo += featureCount[idy] * computeEntropy(labels[ids])
    featureInformationGain =  nodeInformation - conditionalInfo
    gainRatio = featureInformationGain / computeEntropy(featureCount)

if (gainRatio > bestGainRatio):
    bestInformationGain = featureInformationGain
    bestGainRatio = gainRatio
    bestfeature = column

