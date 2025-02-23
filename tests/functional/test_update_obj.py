from endpoints.update_obj import UpdateObj
from payload.payload import update_payload


def test_update_obj(create_obj_with_data, get_current_time):
    # Cоздадим объект для теста
    object_id = create_obj_with_data

    # Отправим PUT запрос
    updated_obj = UpdateObj()
    updated_obj.update_obj(update_payload, object_id)
    update_time = get_current_time

    # Выполним проверки статуса запроса и валидации схемы
    updated_obj.check_response_is_200()
    updated_obj.validate(updated_obj.get_data())

    # Проверим содержимое полученного ответа
    assert updated_obj.get_updated_obj_id() == object_id, (
        f"Полученный ID от сервера {updated_obj.get_updated_obj_id()}",
        f"не соответствует ожидаемому {object_id}"
    )
    assert updated_obj.get_updated_obj_name() == update_payload['name'], (
        f"Полученное имя товара от сервера {updated_obj.get_updated_obj_name()}",
        f"не соответствует ожидаемому {update_payload['name']}"
    )
    assert updated_obj.get_updated_obj_data() == update_payload['data'], (
        f"Полученные данные товара от сервера {updated_obj.get_updated_obj_data()}",
        f"не соответствует ожидаемому {update_payload['data']}"
    )
    assert updated_obj.get_update_time() == update_time, (
        f"Ожидаемое время обновления товара: {update_time}, "
        f"не соответствует тому времени, что сервер вернул: {updated_obj.get_update_time()}"
    )
