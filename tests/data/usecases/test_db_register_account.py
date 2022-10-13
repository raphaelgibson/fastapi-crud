import pytest

from app.data.usecases.index import DbRegisterAccount

from tests.data.mocks.index import RegisterAccountRepositorySpy
from tests.domain.mocks.index import mock_register_account_input


def make_sut():
    register_account_repository_spy = RegisterAccountRepositorySpy()
    sut = DbRegisterAccount(register_account_repository_spy)

    return sut, register_account_repository_spy


@pytest.mark.asyncio
async def test_should_call_Register_Account_Repository_with_correct_values():
    sut, register_account_repository_spy = make_sut()
    register_account_input = mock_register_account_input()
    await sut.register(register_account_input)
    assert register_account_repository_spy.register_account_input == register_account_input


@pytest.mark.asyncio
async def test_should_raise_if_Register_Account_Repository_raises(mocker):
    sut, register_account_repository_spy = make_sut()
    mocker.patch.object(register_account_repository_spy, "register", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.register(mock_register_account_input())


@pytest.mark.asyncio
async def test_should_return_an_account_on_success():
    sut, register_account_repository_spy = make_sut()
    account = await sut.register(mock_register_account_input())
    assert register_account_repository_spy.result == account
