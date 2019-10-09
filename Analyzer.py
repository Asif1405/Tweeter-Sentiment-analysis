#get the followings from twitter
ckey="consumer key"
csecret="consumer secret"
atoken="access token"
asecret="access secret"

#generating data
class listener(StreamListener):

    def on_data(self, data):

                data = json.loads(data)
                tweet = data["text"]

                sentiment_value, confidence = m.sentiment(tweet)
                print(tweet, sentiment_value, confidence)

                if confidence*100 >= 80:
                        output = open("twitter.txt","a")
                        output.write(sentiment_value)
                        output.write('\n')
                        output.close()

                return True

    def on_error(self, status):
        print(status)

#authenticating connection
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

live stream
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["CR7"])  #use any word you want
