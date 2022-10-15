import pytest

from app.presentation.controllers.index import GetProfileController
from app.presentation.helpers.index import ok, server_error
from tests.presentation.mocks.index import GetProfileSpy


def mock_request() -> dict:
    return {'account_id': 'any_id'}


def make_sut():
    get_profile_spy = GetProfileSpy()
    sut = GetProfileController(get_profile_spy)

    return sut, get_profile_spy


@pytest.mark.asyncio
async def test_should_call_Get_Profile_with_correct_values():
    sut, get_profile_spy = make_sut()
    request = mock_request()
    await sut.handle(request)
    assert get_profile_spy.account_id == request['account_id']


@pytest.mark.asyncio
async def test_should_return_500_if_Get_Profile_raises(mocker):
    sut, get_profile_spy = make_sut()
    mocker.patch.object(get_profile_spy, "get", side_effect=Exception)
    http_response = await sut.handle(mock_request())
    assert http_response == server_error()


@pytest.mark.asyncio
async def test_should_return_200_on_success():
    sut, get_profile_spy = make_sut()
    http_response = await sut.handle(mock_request())
    assert http_response == ok(get_profile_spy.result)
