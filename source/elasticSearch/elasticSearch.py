from datetime import datetime
from elasticsearch import Elasticsearch
import json 

class ElasticSeacrhForDatabase:

    def __init__(self):
        self.elasticSearch = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200, "scheme": "https"}], basic_auth=("superuser","superuser"), verify_certs=False)

    def createIndex(self, indexName, rowGenerator):
        for row in rowGenerator():
            self.elasticSearch.index(index=indexName, id=str(row["_id"]), document= json.dumps({"id": str(row["_id"]), "text": row["text"]}))

    def get(self, indexName, documentId):
        return self.elasticSearch.get(index=indexName, id=documentId)

    def delete(self, indexName, documentId):
        self.elasticSearch.delete(index=indexName, id=documentId)

    def search(self, indexName, text):
        return self.elasticSearch.search(index=indexName, size=20, query={
        "match": {
            "text": text
        }
    })
