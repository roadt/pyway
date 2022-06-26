from connect_mongodb import Mongodb

#connection_url = 'mongodb://venus:27017'
connection_url = 'mongodb://localhost:27017'
collection_name = 'test'

con=Mongodb() 
con.connection(connection_url, database_name='test')

#con.create_database(database_name)

print(con.available_database())

#con.create_collection(collection_name)
#con.drop_collection(self, collection_name)

#con.insert(collection_name, record)
con.find(collection_name)
#con.update(self, collection_name, present_record, new_record))
#con.delete(collection_name,query)


