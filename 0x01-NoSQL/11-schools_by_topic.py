#!/usr/bin/env python3
""" Lets such the collection given an item in the collection """


def schools_by_topic(mongo_collection, topic):
    """ lets filter the collection by topic """
    filtered = mongo_collection.find({"topics": {"$in": [topic]}})
    return [doc for doc in filtered]
