import textrazor

textrazor.api_key = "891790380ade61248e0d99dad6f0650a1e44fdb422e789c6c2181dd6"

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")
print(response.sentences)
for topics in response.topics():
    if topics.score>0.8:
        print(topics.label, topics.score)


