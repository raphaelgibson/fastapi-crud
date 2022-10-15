import pytest

from app.presentation.controllers.index import UpdateProfileController
from app.presentation.errors.index import MissingParamError
from app.presentation.helpers.index import bad_request, ok, server_error
from tests.presentation.mocks.index import UpdateProfileSpy


def mock_request() -> dict:
    return {'account_id': 'any_id', 'name': 'any_name'}


def make_sut():
    update_profile_spy = UpdateProfileSpy()
    sut = UpdateProfileController(update_profile_spy)

    return sut, update_profile_spy


@pytest.mark.asyncio
async def test_should_call_Update_Profile_with_correct_values():
    sut, update_profile_spy = make_sut()
    request = mock_request()
    await sut.handle(request)
    assert update_profile_spy.account_id == request['account_id']
    assert update_profile_spy.name == request['name']


@pytest.mark.asyncio
async def test_should_return_400_if_name_is_not_provided():
    sut, _ = make_sut()
    http_response = await sut.handle({'account_id': 'any_id'})
    assert http_response == bad_request(MissingParamError('name'))


@pytest.mark.asyncio
async def test_should_return_500_if_Update_Profile_raises(mocker):
    sut, update_profile_spy = make_sut()
    mocker.patch.object(update_profile_spy, "update", side_effect=Exception)
    http_response = await sut.handle(mock_request())
    assert http_response == server_error()


@pytest.mark.asyncio
async def test_should_return_200_on_success():
    sut, update_profile_spy = make_sut()
    http_response = await sut.handle(mock_request())
    assert http_response == ok(update_profile_spy.result)
