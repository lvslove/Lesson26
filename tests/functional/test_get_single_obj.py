from endpoints.get_single_obj import GetSingleObj
from payload.payload import valid_create_payload


def test_get_single_obj(create_obj_with_data):
    # Cоздадим объект для теста
    object_id = create_obj_with_data

    # Отправим GET запрос
    single_obj = GetSingleObj()
    single_obj.get_single_obj(object_id)

    # Выполним проверки статуса запроса и валидации схемы
    single_obj.check_response_is_200()
    single_obj.validate(single_obj.get_data())

    # Проверим содержимое полученного ответа
    assert single_obj.get_single_obj_id() == object_id, (
        f"Полученный ID от сервера {single_obj.get_single_obj_id()}",
        f"не соответствует ожидаемому {object_id}"
    )
    assert single_obj.get_single_obj_name() == valid_create_payload['name'], (
        f"Полученное ИМЯ товара от сервера {single_obj.get_single_obj_name()}",
        f"не соответствует ожидаемому {valid_create_payload['name']}"
    )
    assert single_obj.get_single_obj_data() == valid_create_payload['data'], (
        f"Полученные данные товара от сервера {single_obj.get_single_obj_data()}",
        f"не соответствует ожидаемому {valid_create_payload['data']}"
    )
