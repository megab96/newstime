# The labeler takes a url of a news article, extracts topics and entities from the text and writes them in a text file.

# To do:
# - think about labeling multiple urls concurrently
# - output labels directly to the classifier component without the need for a file

import textrazor
textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

class labeler:

    howManyTopics = 15
    howManyEntities = 15

    def __init__(self):
        self.client = textrazor.TextRazor(extractors=["topics", "entities"])  #instance of TextRazor class

    def extractAndPrint(self, url, filename):
        self.response = self.client.analyze_url(url)
        f = open(filename, "w")
        f.write("#TOPICS\n")
        for topic in self.response.topics()[1:self.howManyTopics]:
            f.write(topic.label + "\n")
        f.write("#ENTITIES\n")
        for entity in self.response.entities()[1:self.howManyEntities]:
            f.write(entity.id + "\n")
        f.write("#END\n")
        f.close()

l1 = labeler()
l1.extractAndPrint("http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html", "labels1.txt")
l2 = labeler()
l2.extractAndPrint("https://www.nytimes.com/2018/03/27/world/europe/whistle-blower-data-mining-cambridge-analytica.html", "labels2.txt")
