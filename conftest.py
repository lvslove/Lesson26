import pytest
from payload.payload import valid_create_payload, invalid_create_payload
from endpoints.create_obj import CreateObj


@pytest.fixture
def create_obj():
    """Фикстура для создания объекта"""
    return CreateObj()


@pytest.fixture(params=[
    (valid_create_payload, True),
    (invalid_create_payload, False)
])
def test_data(request):
    """Фикстура для параметризации тестов"""
    return request.param


