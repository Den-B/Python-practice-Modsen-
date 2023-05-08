from source.database.mongoDatabase import MongoDatabase
from source.elasticSearch.elasticSearch import ElasticSeacrhForDatabase

from source.server.index import runServer

runServer(5000)


