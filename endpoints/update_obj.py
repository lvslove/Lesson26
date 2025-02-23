import requests
from dateutil.parser import isoparse
from endpoints.base_endpoint import Endpoint


class UpdateObj(Endpoint):
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
            },
            "updatedAt": {"type": "string"}
        },
        "required": ["id", "name", "data", "updatedAt"]
    }

    def update_obj(self, update_payload, object_id):
        self.response = requests.put(f'{self.url}/objects/{object_id}',
                                     json=update_payload)
        self.response_json = self.response.json()

    def get_updated_obj_id(self):
        return self.get_data()['id']

    def get_updated_obj_name(self):
        return self.get_data()['name']

    def get_updated_obj_data(self):
        return self.get_data()['data']

    def get_update_time(self):
        update_time = self.get_data()['updatedAt']
        dt = isoparse(update_time)
        return dt.replace(microsecond=0).isoformat()
