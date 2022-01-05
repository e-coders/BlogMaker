import datetime

post_ad = "<div class=&quot;col-md-10 col-lg-8&quot;><div class=&quot;post-preview&quot;><a href=&quot;[link]&quot;><h2 class=&quot;post-title&quot;>[title]</h2><h3 class=&quot;post-subtitle&quot;>[content]</h3></a><p class=&quot;post-meta&quot;>Posted by&nbsp;<a href=&quot;#&quot;>Admin</a></p></div><hr></div>"
post_ad = post_ad.replace("&quot;",'"')

blog_post = "<div class=&quothero-blog-post&quot><h1>[post]</h1><h3>[little-desc]</h3></div><div class=&quothero-blog-post hero-text&quot>[desc]</div><button class=&quothero-blog-post btn btn-explore&quot onclick=&quotwindow.location = 'posts.html'&quot>See more blogs</button>"
blog_post = (blog_post.replace("&quot",'"')).replace("&quot;",'"')

def readFile(name):
	f = open(f"{name}","r")
	c = f.read()
	f.close()
	return c

def writeFile(name,content):
	f = open(f"{name}","w")
	f.write(f"{content}")
	f.close()

def readLines(name):
	global linesconfig
	f = open(f"{name}","r")
	c = f.readlines()
	f.close()
	linesconfig = c

def calcPostAdConfigID(value):
	return int(f"{value}") + 25

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

title = input("Post Title: ")
little_desc = input("Type a little Description: ")
desc = input("Type a Full Description:\n\nTip: Use <br> to add a line break!\n")
ID = input("Enter a ID, In which name this file will be refered. ")
blog_full = readFile("site/blog-post.html")
blog_full = blog_full.replace("[title]",title)
blog_full = blog_full.replace("[little-des]",little_desc)
blog_full = blog_full.replace("[content]",desc)
blog_full = blog_full.replace("[date]",generateToday())
writeFile("site/" + ID + ".html",blog_full)
print("Rendering file succeed.")


posts = readFile("site/index.html")    
post_ad = "<div class=&quot;col-md-10 col-lg-8&quot;><div class=&quot;post-preview&quot;><a href=&quot;[link]&quot;><h2 class=&quot;post-title&quot;>[title]</h2><h3 class=&quot;post-subtitle&quot;>[little-desc]</h3></a><p class=&quot;post-meta&quot;>Posted by&nbsp;<a href=&quot;#&quot;>Admin</a></p></div><hr></div><!--[ADS]-->"
post_ad = post_ad.replace("&quot;",'"')
post_ad = post_ad.replace("[link]",str(ID) + ".html")
post_ad = post_ad.replace("[title]",title)
post_ad = post_ad.replace("[little-desc]",little_desc)
posts = posts.replace("<!--[ADS]-->","\n\n" + str(post_ad) + "\n<!--[ADS]-->")
writeFile("site/index.html",posts)