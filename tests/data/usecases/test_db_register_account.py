import pytest

from app.data.usecases.index import DbRegisterAccount
from tests.data.mocks.index import CheckAccountByEmailRepositorySpy, HasherSpy, RegisterAccountRepositorySpy
from tests.domain.mocks.index import mock_register_account_input


def make_sut():
    check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
    hasher_spy = HasherSpy()
    register_account_repository_spy = RegisterAccountRepositorySpy()

    sut = DbRegisterAccount(
        check_account_by_email_repository_spy, hasher_spy, register_account_repository_spy
    )

    return sut, check_account_by_email_repository_spy, hasher_spy, register_account_repository_spy


@pytest.mark.asyncio
async def test_should_call_Check_Account_By_Email_Repository_with_correct_values():
    sut, check_account_by_email_repository_spy, _, _ = make_sut()
    register_account_input = mock_register_account_input()
    await sut.register(register_account_input)
    assert check_account_by_email_repository_spy.email == register_account_input.email


@pytest.mark.asyncio
async def test_should_return_None_if_Check_Account_By_Email_Repository_returns_False():
    sut, check_account_by_email_repository_spy, _, _ = make_sut()
    check_account_by_email_repository_spy.result = True
    account = await sut.register(mock_register_account_input())
    assert account is None


@pytest.mark.asyncio
async def test_should_raise_if_Check_Account_By_Email_Repository_raises(mocker):
    sut, check_account_by_email_repository_spy, _, _ = make_sut()
    mocker.patch.object(check_account_by_email_repository_spy, "check_by_email", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.register(mock_register_account_input())


@pytest.mark.asyncio
async def test_should_call_Hasher_with_correct_values():
    sut, _, hasher_spy, _ = make_sut()
    register_account_input = mock_register_account_input()
    await sut.register(register_account_input)
    assert hasher_spy.plaintext == register_account_input.password


@pytest.mark.asyncio
async def test_should_raise_if_Hasher_raises(mocker):
    sut, _, hasher_spy, _ = make_sut()
    mocker.patch.object(hasher_spy, "hash", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.register(mock_register_account_input())


@pytest.mark.asyncio
async def test_should_call_Register_Account_Repository_with_correct_values():
    sut, _, hasher_spy, register_account_repository_spy = make_sut()
    register_account_input = mock_register_account_input()
    await sut.register(register_account_input)
    register_account_input.password = hasher_spy.digest
    assert register_account_repository_spy.register_account_input == register_account_input


@pytest.mark.asyncio
async def test_should_raise_if_Register_Account_Repository_raises(mocker):
    sut, _, _, register_account_repository_spy = make_sut()
    mocker.patch.object(register_account_repository_spy, "register", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.register(mock_register_account_input())


@pytest.mark.asyncio
async def test_should_return_an_account_on_success():
    sut, _, _, register_account_repository_spy = make_sut()
    account = await sut.register(mock_register_account_input())
    assert register_account_repository_spy.result == account
