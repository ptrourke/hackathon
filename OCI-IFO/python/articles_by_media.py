from pymongo import MongoClient

# connection to MongoDB on the IFO server
uri = "mongodb://hackathon_reader:To0305@www.oci-ifo.org:27017/scrapy?authMechanism=MONGODB-CR"
client = MongoClient(uri)
db = client.scrapy    
collection = db.articles

#uncomment to save output to file
#f = open('data.txt', 'w') 

#Query to MongoDB
#This query outputs a list of articles published by a media.
articles = collection.find({"media_url": "http://www.thestar.com/" }).limit( 1000 )
for x in articles:
    print x
#uncomment to save output to file
#    print  >>f, x 

