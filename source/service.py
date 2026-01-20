import requests

GET_JSON_HTTPS_ADDR = r"https://jsonplaceholder.typicode.com/users"


database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users_json():
    response = requests.get(GET_JSON_HTTPS_ADDR)

    if response.status_code != 200:
        raise requests.HTTPError
    
    return response.json()
