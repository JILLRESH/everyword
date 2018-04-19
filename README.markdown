This was the file from the aparrish code I edited for my bot. I deleted some irrelevant information. The rest is pretty helpful, but I think reading my comments in everywordbot.py and [this website](https://medium.com/science-friday-footnotes/how-to-make-a-twitter-bot-in-under-an-hour-259597558acf) will be more helpful.
    
DM me at [@jillresh](https://twitter.com/jillresh) if you have any trouble or questions. 

Best of luck!
-Jill



Everyword Bot
-------------

[![Build Status](https://travis-ci.org/aparrish/everywordbot.svg)](https://travis-ci.org/aparrish/everywordbot) [![Coverage Status](https://coveralls.io/repos/aparrish/everywordbot/badge.svg)](https://coveralls.io/r/aparrish/everywordbot)

This is a small Python script that implements an [`@everyword`](http://twitter.com/everyword)-like Twitter bot. Here's what you'll need to run it:

* Python 2.6+
* [Tweepy](http://www.tweepy.org/)
* a plain text file, with each of your desired tweets on one line

Instructions
------------



* `<ckey>` is your Twitter consumer key;
* `<csecret>` is your Twitter consumer secret;
* `<atoken>` is a valid Twitter access token;
* `<tokensecret>` is the access token secret for the token given above;
* `<source>` is the filename of a plain text file, with one tweet per line (defaults to `tweet_list.txt` in the current directory); and
* `<index>` is the name of a file where the script can store the current tweet index (i.e., which line in the file should be tweeted next). The script must be able to write to this file.



Production Notes
----------------

Twitter may return one of a variety of error messages in response to an attempt
to post a status update (invalid authorization credentials, rate limits, fail
whales, etc.). This script does not attempt to catch or differentiate between
these errors; however, it will *only* increment the index if the post succeeds.
(The idea is that 100% coverage of the source file is more important than 100%
uptime.)

As stated in the license, this software is provided under no warranty of any
kind. However, if the operation of this script is critical to your business,
grant application, art school thesis, or innovative government program, you may
want to monitor the results of the script by (e.g.) checking the return value
of the script and sending an e-mail message if it's non-zero.  Feel free to
update the script to handle errors in whatever method is appropriate for your
specific application.

Obtaining Twitter authorization credentials
-------------------------------------------

The easiest way to obtain the appropriate credentials is as follows:

* Create a new Twitter account. This is the account on whose behalf the script will post tweets.
* Go to the [Twitter Application Management page](https://apps.twitter.com/) and sign in with the account you just created. (You'll need to verify your account's e-mail address before Twitter will let you log in with your new account.)
* Click "Create a new application."
* Fill in the form. The "Callback URL" field is not important.
* You'll be taken to the overview page for your new application. Activate the "Settings" tab and change the "Application Type" from "Read only" to "Read and Write."
* Return to the "Details" tab. Select "Create my access token" at the bottom of the page.
* Congratulations! All the information that you need (consumer key, consumer secret, access token, access token secret) is now displayed on the "Details" tab.

In my experience, Twitter may prevent newly created accounts from posting
status updates, responding to such requests with invalid authorization errors.
This is likely an anti-spam measure. Wait a few minutes and try again before
freaking out.

Creating your Twitter API application while logged in to your Twitter bot user
account is the by far simplest method for obtaining credentials. 

(The above information above may become inaccurate if Twitter changes their
policies or the layout of their site.)

License
-------

Everyword Bot is provided under the MIT license. See `LICENSE.TXT` for more information.

