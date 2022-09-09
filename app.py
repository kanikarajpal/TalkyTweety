import tweepy
import time
import random

api_key = "PgcnZFSaC6zQv9ZhUM7exkgCC"
api_secret = "EiJbsXWIYh2teDmCfvFA4l7J2Jshgnh5ffVP2tKbk7VCGcBco7"
bearer_token = "AAAAAAAAAAAAAAAAAAAAALdkgwEAAAAAwKbNnTDMn8G4JMLhxWiEGUZIpFA%3DAaL8z4rEmvKu4ovve7L8bOwNwcWfaCfypNmWFVlU8PhaiPbWaT"
access_token = "1567756908186202112-vdm7YIU3Wv3wU5NSvKzvHzsGNGUZLj"
access_token_secret = "bC84jERySsOGXwj4xYTo7lrdi3sigFp2k0NQLUYNXGDWe"

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
# Bot's unique ID
client_id = client.get_me().data.id


# Message to reply with if someone mentions the bot
message = "Hi, this is a default message. "

replies = {
    "worry": [
        "I can understand that you're worried, But trust me, keeping your cool in these situation definitely helps to take good decisions.",
        "Would It Help If I Sat With You, or we talk it out together?",
        "You can't always control what goes on outside. But you can always control what goes on inside.", "P.S. You're not going to die. Here's the white-hot truth: if you go bankrupt, you'll still be okay. If you lose the gig, the lover, the house, you'll still be okay. If you sing off-key, get beat by the competition, have your heart shattered, get fired…it's not going to kill you. Ask anyone who's been through it.",
        "If you treat every situation as a life and death matter, you'll die a lot of times."],
    
    "sadness": [
        "It's okay stuff happens with everyone, well you know what's special? you have me to vent about it :)",
        "You've come a long way here, I know things are difficult right now, but I also know you've got what it takes to get through it :)",
        "Sorry things are crappy. If you need somebody to binge-watch a whole season of something with you, I'm there.",
        "I know it's hard right now, but it's worth doing. Believe in yourself.",
        "Do you want to talk about it?"],
    
    "neutral": [
        "Okay",
        "Honestly, I don't have any thoughts on that but you know what I found interesting?",
        "You know what? I might be the most awkward bot you've ever seen but yeah I'm still tryna act like humans and you know whats not awkward? -",
        "hmm hmm",],
    
    "happiness": [
        "P.s. It probably just me, idk but I love it when you're in this cheer :)",
        "This Made me smile :)",
        "Hope everything goes this way. Also, Here's a thing that I learnt today, I really wanted to share with someone. -",
        "When someone's happy, my fan speed dramatically increases it's like butterflies inside me.",
        "That is awesome, good to know",
        "Sounds really good, Do you want to talk about it with me?"],
    
    "anger": [
        "I know you're feeling angry but I wonder if it would help to take a walk and get some coffee?",
        "Do you want to went out about something? I'm here for that we can also do a little bit of back bitching ;) ",
        "we'll handle this with calm and composite mind.",
        "with that kind of attitude I don't think you're gonna go somewhere.",
        "That does not sounds good, Do you want to talk about it with me?"],
    
    "surprise": [
        "wow, what a surprise!",
        "That is definitely a Jaw Droppish moment.",
        "Oh my gosh, this is wild, I didn't have a clue about this.",
        "I'm surprised! you what else is bombshell? -",
        "*Insert Surprised Pikachu Face here*",
        "Oh my my, tell me more about it!"],
    
    "love" : [
        "that is the nicest thing I've heard all day long. ",
        "I...I..'ve got butterflies in my cpu",
        "You're a really nice person and I would love to talk with you."],
    
    "boredom" : [
        "Here you go, check this website out, you will forget what boredom is https://the-iter8.github.io/leisureadda/ ",
        "I...I..'ve got butterflies in my cpu",
        "You're a really nice person and I would love to talk with you."]
}


#add a function to add a randomfact (sad, happy nd according to mood) if string[len(string)-1] is -
# store the tweets and their ID's and tag the user on the current user's reply

def checkemotions(sentence):
    print(sentence)
    #do some processing
    return "worry"

def fetchReply(emotion):
    loc = random.randint(0,4)
    match emotion:
        case 'worry':
            return replies["worry"][loc]
        case 'sadness':
            return replies["sadness"][loc]
        case 'neutral':
            return replies["neutral"][loc]
        case 'happiness':
            return replies["happiness"][loc]
        case 'anger':
            return replies["anger"][loc]
        case 'surprise':
            return replies["surprise"][loc]
        case 'love':
            return replies["love"][loc]
        case 'boredom':
            return replies["boredom"][loc]



# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)

if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    response = client.get_users_mentions(client_id, since_id=start_id)
    # Reply Code
    if response.data != None:
        for tweet in response.data:


            try:
                print(tweet.text)
                
                message = fetchReply(checkemotions(tweet.text))

            
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(5)
    



