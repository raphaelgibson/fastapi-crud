import pytest

from app.data.usecases.index import DbDeleteAccount
from tests.data.mocks.index import DeleteAccountByIdRepositorySpy


def make_sut():
    delete_account_by_id_repository_spy = DeleteAccountByIdRepositorySpy()
    sut = DbDeleteAccount(delete_account_by_id_repository_spy)

    return sut, delete_account_by_id_repository_spy


@pytest.mark.asyncio
async def test_should_call_Delete_Account_By_Id_Repository_with_correct_values():
    sut, delete_account_by_id_repository_spy = make_sut()
    await sut.delete('any_id')
    assert delete_account_by_id_repository_spy.account_id == 'any_id'


@pytest.mark.asyncio
async def test_should_raise_if_Delete_Account_By_Id_Repository_raises(mocker):
    sut, delete_account_by_id_repository_spy = make_sut()
    mocker.patch.object(delete_account_by_id_repository_spy, "delete_by_id", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.delete('any_id')


@pytest.mark.asyncio
async def test_should_return_None_on_success():
    sut, delete_account_by_id_repository_spy = make_sut()
    result = await sut.delete('any_id')
    assert delete_account_by_id_repository_spy.result == result
