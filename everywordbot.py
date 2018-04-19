
import tweepy
import os
try:
    import json
except ImportError:
    import simplejson as json


#Need to edit these. Copy and paste your twitter app keys and tokens betwwen the quotes here:    
consumer_key = "put your consumer key between these quotes"
consumer_secret = "put your consumer secret between these quotes"
access_token = "put your access token between these quotes"
access_token_secret = "put your token secret between these quotes"

#Name of the text file containing one tweet per line
source_file="words.txt" 

#Your prefix and suffix here. If you don't want one or the other leave the quotes empty: ""
#If you want a space between the prefix/suffix and the word from words.txt, put that in the quotes too 
suffix=" swag" # " your suffix, probably want a space after the first quotation"
prefix= ""#"your prefix, probably want a space before the last quotation "

#your twitter handle without the @ in between the quotes
place_id="your twitter handle here" 



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#your twitter handle without the @ in between the quotes
user = api.get_user('your handle here')

#This program assumes you're starting with a fresh account, and that you won't be using it for other tweets, replies, or retweets
#when your number of tweets--aka statuses--is zero, this will take the word(s) from line 1 of words.txt
#If you are not starting with a clean account, you can subtract the number of tweets you currently have at the end of this line:
postnumber=user.statuses_count 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#=========================================================
#      DO NOT NEED TO EDIT ANYTHING BELOW THIS LINE
#=========================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class EverywordBot(object):

    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret,
                 source_file_name, 
                 lat=None, long=None, place_id=None,
                 prefix=None, suffix=None, bbox=None):
        self.source_file_name = source_file_name
        self.lat = lat
        self.long = long
        self.place_id = place_id
        self.prefix = prefix
        self.suffix = suffix
        self.bbox = bbox

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.twitter = tweepy.API(auth)

    def _get_current_line(self, index):
        with open(self.source_file_name) as source_fh:
            # read the desired line
            for i, status_str in enumerate(source_fh):
                if i == index:
                    break
            return status_str.strip()

    def _random_point_in(self, bbox):
        """Given a bounding box of (swlat, swlon, nelat, nelon),
         return random (lat, long)"""
        import random
        lat = random.uniform(bbox[0], bbox[2])
        long = random.uniform(bbox[1], bbox[3])
        return (lat, long)

    def post(self):
        index = postnumber
        status_str = self._get_current_line(index)
        if self.prefix:
            status_str = self.prefix + status_str
        if self.suffix:
            status_str = status_str + self.suffix
        if self.bbox:
            self.lat, self.long = self._random_point_in(self.bbox)

        self.twitter.update_status(status=status_str,
                                   lat=self.lat, long=self.long,
                                   place_id=self.place_id)


def _csv_to_float_list(csv):
    return list(map(float, csv.split(',')))


if __name__ == '__main__':
    def _get_comma_separated_args(option, opt, value, parser):
        setattr(parser.values, option.dest, _csv_to_float_list(value))

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('--lat', dest='lat',
                      help="The latitude for tweets")
    parser.add_option('--long', dest='long',
                      help="The longitude for tweets")
    parser.add_option('--bbox', dest='bbox',
                      type='string',
                      action='callback',
                      callback=_get_comma_separated_args,
                      help="Bounding box (swlat, swlon, nelat, nelon) "
                           "of random tweet location")
    (options, args) = parser.parse_args()

    bot = EverywordBot(consumer_key, consumer_secret,
                       access_token, access_token_secret,
                       source_file,
                       options.lat, options.long, place_id,
                       prefix,
                       suffix, 
                       options.bbox)

    bot.post()
