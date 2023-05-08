from source.database.mongoDatabase import MongoDatabase
from source.elasticSearch.elasticSearch import ElasticSeacrhForDatabase

from source.server.index import runServer


runServer(5000)



#database = MongoDatabase("mongodb://127.0.0.1:27066","Modsen")
#database.readCsvFile("./data/posts.csv", "Documents",currectionFunction)
#elasticSearch = ElasticSeacrhForDatabase()
#elasticSearch.createIndex("posts", database.createDatabaseGenerator("Documents"))
#result = elasticSearch.search("posts", "Конкурс на НОВЫЙ СКИН")
#hits = result["hits"]["hits"]
#print(hits)
#idArray = map(lambda document: document["_id"], hits)
#for row in database.findById("Documents", idArray):
#    print(row["created_date"])


