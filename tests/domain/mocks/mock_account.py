from app.domain.usecases.index import RegisterAccount


def mock_register_account_input() -> RegisterAccount.Input:
    return RegisterAccount.Input(name='any_name', email='any_email', password='any_password')