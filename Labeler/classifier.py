# The classifier takes two lists of labels extracted by the labeler and decided whether they belong to the same news story or not.

# To do:
# • figure out a good weight assignment
# • !! false negatives are better than false positives

class classifier:

    entitiesWeight = 3
    topicsWeight = 1
    score = 0
    scoreThreshold = 20

    def __init__(self):

    def readAndCompare(self, filename1, filename2):
        file1 = open("labels1.txt", "r")
        file2 = open("labels2.txt", "r")
        if(file1.readline() != "#TOPICS" or file2.readline() != "#TOPICS"):
            return False
        else:   # compare entities
            while (file1.readline() != "#ENTITIES"):
                while (file2.readline() != "#ENTITIES"):
                    if (file1.readline() = file2.readline()):
                        score += 3
            while (file1.readline() != "#END")
                while (file2.readline() != "#END"):
                    if (file1.readline() = file2.readline()):
                        score += 1
        if score > scoreThreshold:
            return True
        else:
            return False

    def setWeights(self, entWeight, topWeight):
        self.entitiesWeight = entWeight
        self.topicsWeight = topWeight
