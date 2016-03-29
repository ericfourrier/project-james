#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""

Purpose : Gather helpers for auth and storing data to json and to mongodb

Notes : We will use tweepy api : https://github.com/tweepy/tweepy

"""

# Import Packages
import os
import json
import codecs
import tweepy


def get_consumer_tokens():
    """ Return a tuple of consumer_id, consumer_secret """
    return os.environ.get('TWITTER_CONSUMER_ID'), os.environ.get('TWITTER_CONSUMER_SECRET')


def get_access_tokens():
    """ Return a tuple of access_id, access_secret """
    return os.environ.get('TWITTER_ACCESS_ID'), os.environ.get('TWITTER_ACCESS_SECRET')

ci, cs = get_consumer_tokens()
aci, acs = get_access_tokens()


def authentify(consumer_id, consumer_secret, access_id, access_secret):
    auth = tweepy.OAuthHandler(consumer_id, consumer_secret)
    #auth.secure = True
    auth.set_access_token(access_id, access_secret)
    return auth


def authentify_app(consumer_id, consumer_secret):
    """ Identify only app increase rate limit to 450 for search"""
    return tweepy.AppAuthHandler(consumer_id, consumer_secret)

auth = authentify_app(ci,cs)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def write_to_json(data, file_path):
    """ write tweet by tweet to json """
    with codecs.open(file_path, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def write_to_json_line(data, file_path):
    """ Save one object to json (one object per line) """
    with codecs.open(file_path, 'a', encoding='utf-8') as f:
        f.write("{}\n".format(json.dumps(data)))


def read_from_json_line(file_path):
    """ Read json line file """
    data = []
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def read_from_json(file_path):
    """ Read full json file of tweets """
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

#
