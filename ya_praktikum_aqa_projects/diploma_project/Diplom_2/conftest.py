import random

import pytest

from data import UserHelper, OrderHelper, IngredientsHash


@pytest.fixture
def create_user():
    user_data = UserHelper.reg_user()
    yield user_data
    UserHelper.delete_user(user_data["response_json"]["accessToken"])


@pytest.fixture
def delete_user():
    data = {}
    yield data
    UserHelper.delete_user(data["accessToken"])


@pytest.fixture
def gen_email():
    return UserHelper.generate_email()


@pytest.fixture
def gen_pass():
    return UserHelper.generate_password()


@pytest.fixture
def gen_name():
    return UserHelper.generate_name()


@pytest.fixture
def valid_hashes():
    random_valid_hashes = random.sample(IngredientsHash.VALID_INGREDIENTS_HASH, random.randint(1, 3))
    return tuple(random_valid_hashes)


@pytest.fixture
def invalid_hashes():
    return IngredientsHash.generate_invalid_hashes()
