# imports
import datetime

# Get author's name
uname = input('Enter the author\'s name: ')

# Home Post AD HTML
post_ad = f"<div class=&quot;col-md-10 col-lg-8&quot;><div class=&quot;post-preview&quot;><a href=&quot;[link]&quot;><h2 class=&quot;post-title&quot;>[title]</h2><h3 class=&quot;post-subtitle&quot;>[content]</h3></a><p class=&quot;post-meta&quot;>Posted by&nbsp;<a href=&quot;#&quot;>{uname}</a></p></div><hr></div>"
post_ad = post_ad.replace("&quot;",'"')

# Blog post HTML Code
blog_post = "<div class=&quothero-blog-post&quot><h1>[post]</h1><h3>[little-desc]</h3></div><div class=&quothero-blog-post hero-text&quot>[desc]</div><button class=&quothero-blog-post btn btn-explore&quot onclick=&quotwindow.location = 'posts.html'&quot>See more blogs</button>"
blog_post = (blog_post.replace("&quot",'"')).replace("&quot;",'"')

# Functions make everything easier.
# Read a file
def readFile(name):
	f = open(f"{name}","r")
	c = f.read()
	f.close()
	return c

# Write to a file
def writeFile(name,content):
	f = open(f"{name}","w")
	f.write(f"{content}")
	f.close()

# Read all lines of a file
def readLines(name):
	global linesconfig
	f = open(f"{name}","r")
	c = f.readlines()
	f.close()
	linesconfig = c

# Generate a readable date
def generateToday():
	time2 = datetime.datetime(2022,1,7)
	time2 = time2.today()
	day = time2.day
	year = time2.year
	if time2.month == 1:
		month = "January"
	elif time2.month == 2:
		month = "February"
	elif time2.month == 3:
		month = "March"
	elif time2.month == 4:
		month = "April"
	elif time2.month == 5:
		month = "May"
	elif time2.month == 6:
		month = "June"
	elif time2.month == 7:
		month = "July"
	elif time2.month == 8:
		month = "August"
	elif time2.month == 9:
		month = "September"
	elif time2.month == 10:
		month = "October"
	elif time2.month == 11:
		month = "November"
	elif time2.month == 12:
		month = "December"
	return str(day) + " " + str(month) + " " + str(year)

# Get post title
title = input("Post Title: ")
# Get post description
little_desc = input("Type a little Description: ")
# Blog content
desc = input("Type the content:\n\nTip: HTML supported! Use <BR> for line break, <p> for paragraph and <img> for images! ")
# ID is the name
ID = input("Enter the filename as the url will be refered: ")
# brand name is the org name shown on footer
brand = input("Type brand name, which is shown in the footer near the registered years. ")

# read and write the blog files.
blog_full = readFile("site/blog-post.html")
blog_full = blog_full.replace("[title]",title)
blog_full = blog_full.replace("[little-des]",little_desc)
blog_full = blog_full.replace("[content]",desc)
blog_full = blog_full.replace("[date]",generateToday())
blog_full = blog_full.replace("[author]",uname)
todayyear = datetime.datetime(2022,5,1)
todayyear = todayyear.today()
todayyear = todayyear.year
todayyear = str(todayyear) + "-" + str(todayyear + 1)
blog_full = blog_full.replace("[year]",todayyear)
blog_full = blog_full.replace("[brand]",brand)
writeFile("site/" + ID + ".html",blog_full)
blog_full = readFile("site/" + ID + ".html")
blog_full = blog_full.replace("[document-title]",title)
todaytime = datetime.datetime(2022,5,1)
todaytime = todaytime.today()
todaytime2 = str(todaytime.hour) + ":" + str(todaytime.minute)
if todaytime.hour >= 12:
	todaytime2 = todaytime2 + " PM"
elif todaytime.hour <= 12:
	todaytime2 = todaytime2 + " AM"
blog_full = blog_full.replace('[time]',todaytime2)
# with time attributes its latest version.
writeFile("site/" + ID + ".html",blog_full)
# Give the user a confirmation.
print("Rendering file succeed.")

# Add the link to a post here.
posts = readFile("site/index.html")    
post_ad = f"<div class=&quot;col-md-10 col-lg-8&quot;><div class=&quot;post-preview&quot;><a href=&quot;[link]&quot;><h2 class=&quot;post-title&quot;>[title]</h2><h3 class=&quot;post-subtitle&quot;>[little-desc]</h3></a><p class=&quot;post-meta&quot;>Posted by&nbsp;<a href=&quot;#&quot;>{uname}</a> On [date] at [time]</p></div><hr></div>"
post_ad = post_ad.replace("&quot;",'"')
post_ad = post_ad.replace("[link]",str(ID) + ".html")
post_ad = post_ad.replace("[date]",generateToday())
post_ad = post_ad.replace("[title]",title)
post_ad = post_ad.replace("[little-desc]",little_desc)
post_ad = post_ad.replace("[time]",todaytime2)
posts = posts.replace("<!--[ADS]-->","<!--[ADS]-->" + str(post_ad))
posts = posts.replace("<!--NO-->","\n")
# Write the file
writeFile("site/index.html",posts)