from twarc import Twarc
import json

consumer_key="zjwAsouRHgMzrMJxpWNxJtJYJ"
consumer_secret="uu2j3Do5fm266BPY2OiCajnIbUvWEiccgmfiNRZ9tGIfso1leN"
access_token="2758505181-7z1gXy1DgJDeGh1UqWwqiPeupQKmbapYPAeZ9QE"
access_token_secret="GjcjOwMzMwpjfFDW4an2qd1jwykYiYw0L5lb702PNHtYL"
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

tweetId="934131805409697792"
tweetData=t.tweet(tweetId)

maxReplies=300
replies=0

for reply in t.replies(tweetData):   	
	print(replies)
	text_file = open("replies.txt", "a")
	replyText=json.dumps(reply)
	text_file.write("\n"+replyText+"\n")
	text_file.close() 
	if(replies>maxReplies):
		break
	replies+=1