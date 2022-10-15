import pytest

from app.presentation.controllers.index import DeleteAccountController
from app.presentation.helpers.index import ok, server_error
from tests.presentation.mocks.index import DeleteAccountSpy


def mock_request() -> dict:
    return {'account_id': 'any_id'}


def make_sut():
    delete_account_spy = DeleteAccountSpy()
    sut = DeleteAccountController(delete_account_spy)

    return sut, delete_account_spy


@pytest.mark.asyncio
async def test_should_call_Register_Account_with_correct_values():
    sut, delete_account_spy = make_sut()
    request = mock_request()
    await sut.handle(request)
    assert delete_account_spy.account_id == request['account_id']


@pytest.mark.asyncio
async def test_should_return_500_if_Register_Account_raises(mocker):
    sut, delete_account_spy = make_sut()
    mocker.patch.object(delete_account_spy, "delete", side_effect=Exception)
    http_response = await sut.handle(mock_request())
    assert http_response == server_error()


@pytest.mark.asyncio
async def test_should_return_200_on_success():
    sut, _ = make_sut()
    http_response = await sut.handle(mock_request())
    assert http_response == ok({'message': 'Account deleted'})
