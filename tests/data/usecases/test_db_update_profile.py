import pytest

from app.data.usecases.index import DbUpdateProfile
from tests.data.mocks.index import UpdateAccountRepositorySpy


def make_sut():
    update_account_repository_spy = UpdateAccountRepositorySpy()
    sut = DbUpdateProfile(update_account_repository_spy)

    return sut, update_account_repository_spy


@pytest.mark.asyncio
async def test_should_call_Update_Account_Repository_with_correct_values():
    sut, update_account_repository_spy = make_sut()
    await sut.update('any_id', 'any_name')
    assert update_account_repository_spy.account_id == 'any_id'
    assert update_account_repository_spy.name == 'any_name'


@pytest.mark.asyncio
async def test_should_raise_if_Update_Account_Repository_raises(mocker):
    sut, update_account_repository_spy = make_sut()
    mocker.patch.object(update_account_repository_spy, "update", side_effect=Exception)

    with pytest.raises(Exception):
        await sut.update('any_id', 'any_name')


@pytest.mark.asyncio
async def test_should_return_an_account_on_success():
    sut, update_account_repository_spy = make_sut()
    account = await sut.update('any_id', 'any_name')
    assert update_account_repository_spy.result == account
