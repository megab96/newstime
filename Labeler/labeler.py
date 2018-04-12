import textrazor

textrazor.api_key = "5634740d9e8d89a14374edaa305c207bd6eda5918bbe233634beb092"

i = 0

client = textrazor.TextRazor(extractors=["topics"])  #instance of TextRazor class

response1 = client.analyze_url("https://www.nbcnews.com/news/world/catalan-independence-referendum-what-s-behind-divisive-spanish-vote-n805421")
response2 = client.analyze_url("https://www.nytimes.com/2015/09/22/opinion/why-a-brexit-looms-large.html?rref=collection%2Ftimestopic%2FEuropean%20Union&action=click&contentCollection=timestopics&region=stream&module=stream_unit&version=search&contentPlacement=53&pgtype=collection")
sameStory = False
similarCount = 0
i = 0
for topic1 in response1.topics():
	for topic2 in response2.topics():
		if (topic1.label == topic2.label and topic1.score > 0.8 and topic2.score > 0.8 ):
			similarCount = similarCount + 1
			print(topic1.label)

	if(similarCount > 3):
		sameStory = True
		print("same story")
	i = i+1

	if(i<=20):
		print(topic1.label)
	else:
		break


# facebook cambridge analytica scandal:

# zuckerberg breaks silence
# http://money.cnn.com/2018/03/21/technology/mark-zuckerberg-cambridge-analytica-response/index.html
# Facebook
# Mark Zuckerberg
# Dow Jones & Company
# Standard & Poor's
# CNN
# Privacy
# Companies
# Business
# Privacy policy
# Terms of service

# times How Trump Consultants Exploited the Facebook Data of Millions
# https://www.nytimes.com/2018/03/17/us/politics/cambridge-analytica-trump-campaign.html
# Cambridge Analytica
# Facebook
# Politics
# WikiLeaks
# Government
# Russian interference in the 2016 United States elections
# Donald Trump
# 2017 Special Counsel investigation
# Donald Trump presidential campaign, 2016
# Julian Assange

# times reaction to article
# https://www.nytimes.com/2018/03/18/us/cambridge-analytica-facebook-privacy-data.html
# Facebook
# Cambridge Analytica
# Politics
# Government
# Public sphere
# Communication
# Mark Zuckerberg
# Social media
# Fake news
# Mass media

# times
# https://www.nytimes.com/2018/03/21/technology/mark-zuckerberg-facebook.html
# Facebook
# Mark Zuckerberg
# News Feed
# Computing
# World Wide Web
# Cyberspace
# Technology
# The Social Network
# Digital media
# Cambridge Analytica

# times
# https://www.nytimes.com/2018/03/27/world/europe/whistle-blower-data-mining-cambridge-analytica.html
# Cambridge Analytica
# Politics
# Government
# Data mining
# Donald Trump
# Accountability
# Public sphere
# Culture
# Advertising
# United Kingdom

# times
# https://www.nytimes.com/2018/04/10/us/politics/zuckerberg-facebook-senate-hearing.html
# Facebook
# Mark Zuckerberg
# Cambridge Analytica
# Russian interference in the 2016 United States elections
# United States Congress
# Politics
# Government
# Privacy
# Advertising
# Public sphere

# similar but unrelated stories

# Edward Snowden comes forward as source of NSA leaks
# https://www.washingtonpost.com/politics/intelligence-leaders-push-back-on-leakers-media/2013/06/09/fff80160-d122-11e2-a73e-826d299ff459_story.html?noredirect=on&utm_term=.87ea4fe11804
# Edward Snowden
# Central Intelligence Agency
# PRISM (surveillance program)
# National Security Agency
# James Clapper
# Government information
# Security
# Government of the United States
# Law
# Military intelligence collection
