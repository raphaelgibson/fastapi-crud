import pytest

from app.presentation.controllers.index import RegisterAccountController
from app.presentation.helpers.index import ok, server_error
from test.presentation.mocks.index import RegisterAccountSpy


def mock_request() -> RegisterAccountController.Request:
    return RegisterAccountController.Request(email='any_email', name='any_name', password='any_password')


def make_sut():
    register_account_spy = RegisterAccountSpy()
    sut = RegisterAccountController(register_account_spy)

    return sut, register_account_spy


@pytest.mark.asyncio
async def test_should_call_Register_Account_with_correct_values():
    sut, register_account_spy = make_sut()
    request = mock_request()
    await sut.handle(request)
    assert register_account_spy.register_account_input == request


@pytest.mark.asyncio
async def test_should_return_500_if_Register_Account_raises(mocker):
    sut, register_account_spy = make_sut()
    mocker.patch.object(register_account_spy, "register", side_effect=Exception)
    http_response = await sut.handle(mock_request())
    assert http_response == server_error()


@pytest.mark.asyncio
async def test_should_return_200_on_success():
    sut, register_account_spy = make_sut()
    http_response = await sut.handle(mock_request())
    assert http_response == ok(register_account_spy.result)
