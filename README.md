What Is This?
-------------

This script uses the [requests](http://www.python-requests.org/en/latest/)
library as well as the
[webrowser](https://docs.python.org/3/library/webbrowser.html) module
to make a respectful get http request to reddit's
[random](http://reddit.com/r/random) page.

The script asks for a user input on how many random subreddit links to gather.
It only retrieves successful redirects, and opens them simultaneously
once they've been gathered.

How To Use The Script
-----------------------

Assuming you have Python 3.+, all you need to do from your terminal is execute
the following line:   
``python random_reddit_grabber.py``

The interface will take you the rest of the way.

Installation
-----------------------

1. Installation is twofold. Make sure you have Python 3.+ and
2. From your command line, download the Requests module   
``pip install requests``

License
--------------------------

No license. Try this script out at your leisure.

TODO
--------------------------

HTML/txt exporting, alternate ways to view finished, gathered links. E.g. avoid
opening 10+ tabs at once.
