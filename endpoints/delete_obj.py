import requests
from endpoints.base_endpoint import Endpoint


class DeleteObj(Endpoint):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"}
        },
        "required": ["message"]
    }

    def delete_obj(self, obj_id):
        self.response = requests.delete(url=f"{self.url}/objects/{obj_id}")
        self.response_json = self.response.json()

    def get_delete_message(self):
        return self.get_data()['message']
