from uuid import uuid4
from requests import post

from bff.dispatchers import Dispatcher
from bff.utils import get_listings_url, time_millis


def create_ground_mutation(_, info, input):
    command = dict(id=str(uuid4()), ingestion=time_millis(), data=input)
    dispatcher = Dispatcher()
    dispatcher.send_message(command, "register-ground-command")
    return {"message": "Ground registered successfully!"}


def create_sale_mutation(_, info, input):
    command = dict(id=str(uuid4()), ingestion=time_millis(), data=input)
    dispatcher = Dispatcher()
    dispatcher.send_message(command, "register-sale-command")
    return {"message": "Sale registered successfully!"}


def process_listing_mutation(_, info, input):
    url = get_listings_url()
    response = post(f"{url}/information", json=input)
    return response.json()
