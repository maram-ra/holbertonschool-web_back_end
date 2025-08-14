#!/usr/bin/env python3
"""define a function update_topics"""


def update_topics(mongo_collection, name, topics):
    """update all documents"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    