from pymongo.mongo_client import MongoClient
import yaml
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_mongo_client(host=None):
    if not host:
        host = 'default'
    with open(os.path.join(__location__, 'credentials.yaml')) as f:
        creds = yaml.load(f)
    creds = creds.get(host)
    if not creds:
        raise ValueError('There is no host:', host)
    return MongoClient(
        'mongodb://{user}:{password}@{host}'.format(
            user = creds['user'],
            password = creds['password'],
            host = creds['host']))
