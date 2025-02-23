import pytest
from datetime import datetime, timezone
from payload.payload import valid_create_payload, invalid_create_payload
from endpoints.create_obj import CreateObj
from endpoints.delete_obj import DeleteObj


@pytest.fixture
def create_obj():
    """Фикстура для создания объекта"""
    return CreateObj()


@pytest.fixture
def create_obj_with_data():
    """
    Фикстура для создания объекта
    с данными и его удаления после теста
    """
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    created_obj_id = new_obj.get_data()['id']
    yield created_obj_id
    delete_obj = DeleteObj()
    delete_obj.delete_obj(created_obj_id)


@pytest.fixture(params=[
    (valid_create_payload, True),
    (invalid_create_payload, False)
])
def test_data(request):
    """
    Фикстура для параметризации тестов
    """
    return request.param


@pytest.fixture
def get_current_time():
    """
    Фикстура для определения текущего времени в секундах
    """
    return datetime.now(timezone.utc).isoformat(timespec='seconds')
