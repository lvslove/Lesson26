from endpoints.delete_obj import DeleteObj


def test_delete_obj(create_obj_with_data):
    # Cоздадим объект для теста
    object_id = create_obj_with_data

    # Отправим DELETE запрос
    deleted_obj = DeleteObj()
    deleted_obj.delete_obj(object_id)

    # Выполним проверки статуса запроса и валидации схемы
    deleted_obj.check_response_is_200()
    deleted_obj.validate(deleted_obj.get_data())

    # Проверим содержимое полученного сообщения об удалении
    assert deleted_obj.get_delete_message() == f"Object with id = {object_id} has been deleted.", (
        f"Полученное сообщение от сервера об удалении {deleted_obj.get_delete_message()}",
        f"не соответствует ожидаемому"
    )

    # Попытаемся снова удалить уже удаленный товар
    deleted_obj.delete_obj(object_id)
    deleted_obj.check_response_is_404()
