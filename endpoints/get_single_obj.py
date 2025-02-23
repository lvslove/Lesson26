import requests
from endpoints.base_endpoint import Endpoint


class GetSingleObj(Endpoint):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"}
                },
                "required": ["year", "price", "CPU model", "Hard disk size"]
            }
        },
        "required": ["id", "name", "data"]
    }

    def get_single_obj(self, obj_id):
        self.response = requests.get(url=f"{self.url}/objects/{obj_id}")
        self.response_json = self.response.json()

    def get_single_obj_id(self):
        return self.get_data()['id']

    def get_single_obj_name(self):
        return self.get_data()['name']

    def get_single_obj_data(self):
        return self.get_data()['data']
