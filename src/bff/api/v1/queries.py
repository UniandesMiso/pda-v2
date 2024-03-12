from requests import get

from bff.utils import get_properties_url


def get_ground_query(_, info, input):
    request = info.context
    auth = request.headers.get("Authorization")
    
    url = get_properties_url()
    headers = {"Authorization": auth}
    response = get(f"{url}/grounds/{input.get("id")}", headers=headers)

    return response.json()
