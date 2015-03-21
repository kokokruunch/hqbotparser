import feedparser
import praw
import getpass
import time

user_agent = 'haikyuu manga feed:v0.1 (by /u/kruunch)'
r = praw.Reddit(user_agent=user_agent)

user = 'hqbott'
print("Password for " + user_name + "?")
passwd = getpass.getpass()

r.login(user, passwd)


r.submit('test','HQ Bot Test', text='Test')

def nj_get():

	feed = feedparser.parse('http://nijimurashuuzo.tumblr.com/rss')

	#MANGA_NAME = 'haikyuu'
	MANGA_NAME = 'durarara'
	#KEYWORD   = 'translation'
	KEYWORD    = 'shizuo'

	for i in range(0, len(feed['entries'])):
		e = feed.entries[i]

		title = e.title
		cat = e.category

		lowercaseTitle = title.lower() #lower'd just in case

		if((MANGA_NAME in lowercaseTitle) 
			and (KEYWORD in lowercaseTitle)
			and ('drrr' in cat):
		
			link = e.link	
			#print (link)
