tweet = input("Input: ")
for i in tweet:
    if i in ["a","e","i","o","u"]:
        tweet = tweet.replace(i, "")
print(tweet)

