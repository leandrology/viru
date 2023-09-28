import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ruby_admin.settings")

import pymongo
from django.core.exceptions import ObjectDoesNotExist

import django
django.setup()

from convo.models import Response
# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rasa-ruby"]
collection = db["rasamodels"]

# Retrieve data from MongoDB
mongo_data = collection.find()

# Map and save data to Django model
for entry in mongo_data:
    try:
        response_instance = Response.objects.get(intent=entry['domain']['intent'])
        print(response_instance)
    except ObjectDoesNotExist:
        response_instance = Response(
            intent=entry['domain']['intent'],
            message=entry['nlu']['examples'][0],
            response=entry['domain']['response']['text'][0],
            createdate=entry['createdAt'],
            status="Waiting for Approval"
        )
    response_instance.save()