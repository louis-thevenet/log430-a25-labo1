from daos.user_dao import UserDAO
from daos.user_dao_mongo import UserDAOMongo
from models.user import User
import pytest

dao = UserDAOMongo()


@pytest.fixture(scope="module", autouse=True)
def cleanup_after_tests():
    yield
    dao.delete_all()
    dao.close()


def test_user_insert():
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails


def test_user_update():
    user = User(None, 'Charles Babbage', 'babage@example.com')
    assigned_id = dao.insert(user)

    corrected_email = 'babbage@example.com'
    user.id = assigned_id
    user.email = corrected_email

    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails


def test_user_delete():
    user = User(None, 'Douglas Engelbart', 'engelbart@example.com')
    assigned_id = dao.insert(user)
    dao.delete(assigned_id)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails
