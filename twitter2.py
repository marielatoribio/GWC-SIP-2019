# '''
# In this program, we print out all the text data from our twitter JSON file.
# Please explain the comments to students as you code.
# '''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
import matplotlib.pyplot as pit
from wordcloud import WordCloud

text = "hello hello there its me all all"
wordscloud = WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# We use the JSON library to get data from the file as JSON data.
tb = TextBlob("You are a brilliant comupter scientist")

# print(tb.polarity)



# print(type(tweetData))
# print(type(tweetData[1]))
# print(list(tweetData[0].keys()))
#['created_at', 'favorite_count', 'hashtags', 'id', 'id_str', 'lang', 'retweet_count', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
# print(tweetData[1])


# # list(newdict.key())
# print(list(tweetData[0].keys()))
# print(tweetData[1]["favorite_count"])
favorite_count = 0

for i in range(0,len(tweetData)):
	if "favorite_count" in tweetData[i]:
		favorite_count += tweetData[i]["favorite_count"]
avg = favorite_count / len(tweetData)
# print(favorite_count)
# print(avg)

tweetlist = []
for t in range(0,len(tweetData)):
	if "text" in tweetData[t]:
		tweetlist.append(tweetData[t]["text"])
# print(tweetlist)

polarityList = []
for iteam in tweetlist:
	blob1 = TextBlob(iteam)
	polar1 = blob1.polarity
	polarityList.append(polar1)
# print(polarityList)

least = []
for i in range(len(tweetData)):
	dictionaree = {}
	dictionaree["id"] = tweetData[i]["id"]
	dictionaree["polarity"] = polarityList[i]
	dictionaree["tweet"] = tweetlist[i]
	least.append(dictionaree)
# print(least)


tweetstring = ""
for tweet in tweetlist:
	tweet = " "
	tweetstring += tweet
print(tweetstring)


wordscloud = WordCloud().generate("text")
pit.imshow(wordscloud, interpolation= 'bilinear')
pit.axis("off")
pit.show()
pit.savefig('alischart.png')








# We can close the file now that we have locally stored the data.

#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
