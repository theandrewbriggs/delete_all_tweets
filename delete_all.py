from deletebot_credentials import twitter_access

import csv
import time
import tweepy


def main():

    ckey = twitter_access['consumer_key']
    csecret = twitter_access['consumer_secret']
    tkey = twitter_access['access_token_key']
    tsecret = twitter_access['access_token_secret']

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(tkey, tsecret)

    api = tweepy.API(auth)
    user = api.me()

    """
    count = 0
    r = 0
    with open('tweets.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            r += 1
            print "Row {}:".format(r)
            try:
                s = row[0].replace('"', '')
                api.destroy_status(s)
                count += 1
                print "{} destroyed, {} total".format(s, count)
            except:
                print "whoops!"
    """



    """
    # Delete Tweets
    count = 0
    for page in tweepy.Cursor(api.user_timeline, id=user.id, count=200).pages():
        count += len(page)
        for tweet in page:
            api.destroy_status(tweet.id)
            time.sleep(0.1) 
        print "Deleted {} tweets".format(count)
    """

    # 'Destroy' Favorites:
    count = 0
    for page in tweepy.Cursor(api.favorites, id=user.id, count=200).pages():
        count += len(page)
        print count
    

if __name__ == '__main__':
    main()
