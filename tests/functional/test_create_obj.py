def test_create_obj(create_obj, test_data, get_current_time):
    payload, is_valid = test_data

    create_obj.new_obj(payload)
    create_time = get_current_time

    if is_valid:
        create_obj.check_response_is_200()
        create_obj.validate(create_obj.get_data())

        assert create_obj.get_data()['data'] == payload['data'], (
            f"Ответ API {create_obj.get_data()['data']} "
            f"не совпадает с ожидаемыми данными {payload['data']}"
        )

        assert create_obj.get_name() == payload['name'], (
            f"Имя полученное от сервера {create_obj.get_name()} != переданному имени"
            f" {payload['name']}"
        )
        assert create_obj.get_create_time() == create_time, (
            f"Ожидаемое время обновления товара: {create_time}, "
            f"не соответствует тому времени, что сервер вернул: {create_obj.get_create_time()}"
        )
    else:
        print(create_obj.get_data())
