import pytest
from httpx import ASGITransport, AsyncClient
from pytest_mock import MockerFixture

from src.fastapi_example.fastapi_example import app

transport = ASGITransport(app=app)
base_url = "http://test"


@pytest.mark.asyncio
async def test_get_hello():
    async with AsyncClient(transport=transport, base_url=base_url) as client:
        response = await client.get("/hello")
        assert response.status_code == 200
        assert response.json() == {"hello": "how are you?"}


@pytest.mark.asyncio
async def test_get_time(mocker: MockerFixture):
    mock_time = mocker.patch("time.ctime")
    mock_time.return_value = "Tue Mar 11 08:16:16 2025"

    async with AsyncClient(transport=transport, base_url=base_url) as client:
        response = await client.get("/time")
        # mock_time.assert_has_calls()
        assert response.status_code == 200
        assert response.json() == {"time": "Tue Mar 11 08:16:16 2025"}
