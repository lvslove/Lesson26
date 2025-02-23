from endpoints.create_obj import CreateObj
from endpoints.get_single_obj import GetSingleObj
from endpoints.update_obj import UpdateObj
from endpoints.delete_obj import DeleteObj
from payload.payload import valid_create_payload, update_payload


def test_crud(get_current_time):
    # Cоздадим новый объект
    create_obj = CreateObj()

    # Отправим POST запрос
    create_obj.new_obj(valid_create_payload)

    # Выполним проверки статуса POST запроса и валидации схемы
    create_obj.check_response_is_200()
    create_obj.validate(create_obj.get_data())

    # Проверим содержимое полученного ответа для POST запроса
    assert create_obj.get_data()['data'] == valid_create_payload['data'], (
        f"Ответ API {create_obj.get_data()['data']} "
        f"не совпадает с ожидаемыми данными {valid_create_payload['data']}"
    )

    assert create_obj.get_name() == valid_create_payload['name'], (
        f"Имя полученное от сервера {create_obj.get_name()} != переданному имени"
        f" {valid_create_payload['name']}"
    )

    # Получим ID созданного товара
    obj_id = create_obj.get_id()

    # Отправим GET запрос для созданного товара
    get_obj = GetSingleObj()
    get_obj.get_single_obj(obj_id)

    # Выполним проверки статуса GET запроса и валидации схемы
    get_obj.check_response_is_200()
    get_obj.validate(get_obj.get_data())

    # Проверим содержимое полученного ответа для GET
    assert get_obj.get_single_obj_id() == obj_id, (
        f"Полученный ID от сервера {get_obj.get_single_obj_id()}",
        f"не соответствует ожидаемому {obj_id}"
    )
    assert get_obj.get_single_obj_name() == valid_create_payload['name'], (
        f"Полученное ИМЯ товара от сервера {get_obj.get_single_obj_name()}",
        f"не соответствует ожидаемому {valid_create_payload['name']}"
    )
    assert get_obj.get_single_obj_data() == valid_create_payload['data'], (
        f"Полученные данные товара от сервера {get_obj.get_single_obj_data()}",
        f"не соответствует ожидаемому {valid_create_payload['data']}"
    )

    # Отправим PUT запрос
    updated_obj = UpdateObj()
    updated_obj.update_obj(update_payload, obj_id)

    # Выполним проверки статуса PUT запроса и валидации схемы
    updated_obj.check_response_is_200()
    updated_obj.validate(updated_obj.get_data())

    # Проверим содержимое полученного ответа для PUT запроса
    assert updated_obj.get_updated_obj_id() == obj_id, (
        f"Полученный ID от сервера {updated_obj.get_updated_obj_id()}",
        f"не соответствует ожидаемому {obj_id}"
    )
    assert updated_obj.get_updated_obj_name() == update_payload['name'], (
        f"Полученное имя товара от сервера {updated_obj.get_updated_obj_name()}",
        f"не соответствует ожидаемому {update_payload['name']}"
    )
    assert updated_obj.get_updated_obj_data() == update_payload['data'], (
        f"Полученные данные товара от сервера {updated_obj.get_updated_obj_data()}",
        f"не соответствует ожидаемому {update_payload['data']}"
    )

    # Отправим DELETE запрос
    deleted_obj = DeleteObj()
    deleted_obj.delete_obj(obj_id)

    # Выполним проверки статуса DELETE запроса и валидации схемы
    deleted_obj.check_response_is_200()
    deleted_obj.validate(deleted_obj.get_data())

    # Проверим содержимое полученного сообщения об удалении
    assert deleted_obj.get_delete_message() == f"Object with id = {obj_id} has been deleted.", (
        f"Полученное сообщение от сервера об удалении {deleted_obj.get_delete_message()}",
        f"не соответствует ожидаемому"
    )

    # Попытаемся отправить GET запрос для уже удаленного товара
    get_obj.get_single_obj(obj_id)
    get_obj.check_response_is_404()
