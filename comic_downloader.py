import urllib
import os,math
import datetime
def getImageURL(content):
	startIndex=content.find("http://safr.kingfeatures.com/idn/cnfeed/")
	endIndex=content.find("content.php?file=")
	endIndex=endIndex+133
	return content[startIndex:endIndex]

proxies={'http':"http://172.30.0.12:3128/",'https':"https://172.30.0.12:3128/"}
#uncomment the below line if you are not behind a proxy
#proxies={}
comicWebsite="http://dennisthemenace.com/comics/"

day=datetime.datetime.now()

print "Enter from year:"
year=int(raw_input())

while day.year!=year and day.day!=1:
	day=day-datetime.timedelta(days=1)
	fileHandle=urllib.urlopen(comicWebsite+str(day.strftime("%B-%d-%Y").lower()),proxies=proxies)

	if fileHandle.getcode()==200:
		content=fileHandle.read()
		imageURL = getImageURL(content)
		saveImage=urllib.urlopen(imageURL,proxies=proxies)
		writeImage=open("Dennis/"+str(day.strftime("%B-%d-%Y").lower()),'wb')
		writeImage.write(saveImage.read())
		writeImage.close()
		print "Image saved!"
	else:
		print "Error 404: Image not found"

print "Dennis the menace comic strips have been downloaded!"
print "Enjoy reading the comics!"