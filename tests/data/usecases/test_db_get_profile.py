import pytest

from app.data.usecases.index import DbGetProfile
from tests.data.mocks.index import GetAccountByIdRepositorySpy


def make_sut():
    get_account_by_id_repository_spy = GetAccountByIdRepositorySpy()
    sut = DbGetProfile(get_account_by_id_repository_spy)

    return sut, get_account_by_id_repository_spy


@pytest.mark.asyncio
async def test_should_call_Get_Account_By_Id_Repository_with_correct_values():
    sut, get_account_by_id_repository_spy = make_sut()
    await sut.get('any_id')
    assert get_account_by_id_repository_spy.account_id == 'any_id'


@pytest.mark.asyncio
async def test_should_return_None_if_Get_Account_By_Id_Repository_returns_None(mocker):
    sut, get_account_by_id_repository_spy = make_sut()
    mocker.patch.object(get_account_by_id_repository_spy, "get_by_id", return_value=None)
    account = await sut.get('any_id')
    assert account is None


@pytest.mark.asyncio
async def test_should_raise_if_Get_Account_By_Id_Repository_raises(mocker):
    sut, get_account_by_id_repository_spy = make_sut()
    mocker.patch.object(get_account_by_id_repository_spy, "get_by_id", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.get('any_id')


@pytest.mark.asyncio
async def test_should_return_an_account_on_success():
    sut, get_account_by_id_repository_spy = make_sut()
    account = await sut.get('any_id')
    assert get_account_by_id_repository_spy.result == account
