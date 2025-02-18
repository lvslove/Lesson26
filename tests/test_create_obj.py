from endpoints.create_obj import CreateObj
from payload.payload import valid_create_payload


def test_create_obj():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate(new_obj.get_data())
    print(new_obj.get_name())


