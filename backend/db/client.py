from pymongo import MongoClient #type: ignore
import certifi #type: ignore

db_client = MongoClient().local

#ca = certifi.where()
#db_client = MongoClient("mongodb+srv://ansuzgs:<password>@cluster0.n8srebp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca).test