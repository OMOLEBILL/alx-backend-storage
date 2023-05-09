#!/usr/bin/env python3
""" We update the collection matching the given name
    with the list of topics
"""


def update_topics(mongo_collection, name, topics):
    """ Lets add some topics """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
