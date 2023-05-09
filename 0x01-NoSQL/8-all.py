#!/usr/bin/env python3
""" We return a list of all documents """


if __name__ == "__main__":
    def list_all(mongo_collection):
        """ Mongo_collection is the collection we 
        need to return the list of document"""
        alldoc = mongo_collection.find()
        return [doc for doc in alldoc]
