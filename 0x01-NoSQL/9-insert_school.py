#!/usr/bin/env python3
""" Let get the id of the updated collection """


def insert_school(mongo_collection, **kwargs):
    """ we return the id of the updated collection """
    updatedcol = mongo_collection.insert_one(kwargs)
    return updatedcol.inserted_id
