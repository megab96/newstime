import textrazor
textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

# set to eextract topics, entities categories for now
class labeler:

    howManyTopics = 15
    howManyEntities = 15

    def __init__(self):  # pass list of categories to extract (topics, entities, etc.)
        self.client = textrazor.TextRazor(extractors=["topics", "entities", "categories"])  #instance of TextRazor class

    def extractAndPrint(self, url):
        self.response = self.client.analyze_url(url)
        f = open("labels.txt", "w")
        f.write("#TOPICS\n")
        for topic in self.response.topics()[1:self.howManyTopics]:
            f.write(topic.label + "\n")
        f.write("#ENTITIES\n")
        for entity in self.response.entities()[1:self.howManyEntities]:
            f.write(entity.id + "\n")
        f.close()

l1 = labeler()
l1.extractAndPrint("http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html")
