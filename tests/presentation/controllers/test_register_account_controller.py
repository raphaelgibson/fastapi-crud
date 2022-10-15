import pytest

from app.presentation.controllers.index import RegisterAccountController
from app.presentation.errors.index import EmailAlreadyExistsError, MissingParamError
from app.presentation.helpers.index import bad_request, conflict, created, server_error
from tests.presentation.mocks.index import RegisterAccountSpy


def mock_request() -> dict:
    return {'name': 'any_name', 'email': 'any_email', 'password': 'any_password'}


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
async def test_should_return_400_if_name_is_not_provided():
    sut, _ = make_sut()
    http_response = await sut.handle({'email': 'any_email', 'password': 'any_password'})
    assert http_response == bad_request(MissingParamError('name'))


@pytest.mark.asyncio
async def test_should_return_400_if_email_is_not_provided():
    sut, _ = make_sut()
    http_response = await sut.handle({'name': 'any_name', 'password': 'any_password'})
    assert http_response == bad_request(MissingParamError('email'))


@pytest.mark.asyncio
async def test_should_return_400_if_password_is_not_provided():
    sut, _ = make_sut()
    http_response = await sut.handle({'name': 'any_name', 'email': 'any_email'})
    assert http_response == bad_request(MissingParamError('password'))


@pytest.mark.asyncio
async def test_should_return_409_if_Register_Account_returns_None(mocker):
    sut, register_account_spy = make_sut()
    mocker.patch.object(register_account_spy, "register", return_value=None)
    http_response = await sut.handle(mock_request())
    assert http_response == conflict(EmailAlreadyExistsError())


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
    assert http_response == created(register_account_spy.result)
