#!/usr/bin/env python

"""Tests for `ugy_inventory_client` package."""

import pytest

from ugy_inventory_client.lib.auth import Auth, Credential
from ugy_inventory_client.lib.exceptions import AuthenticationError


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_bad_server_url():

    cred = Credential("", "")

    with pytest.raises(ValueError):
        Auth("", cred)


def test_auth_server_login_set_correctly():

    server = "http://localhost:5000"
    cred = Credential("", "")
    auth = Auth(server, cred)
    assert auth.login_url == f"{server}/auth/login"


def test_auth_bad_credential():

    server = "http://localhost:5000"
    cred = Credential("", "")
    auth = Auth(server, cred)

    with pytest.raises(AuthenticationError):
        auth.authenticate()


def test_auth_bad_password():

    server = "http://localhost:5000"
    cred = Credential("admin", "")
    auth = Auth(server, cred)

    with pytest.raises(AuthenticationError):
        auth.authenticate()


def test_auth_bad_username():

    server = "http://localhost:5000"
    cred = Credential("", "lfjdsl")
    auth = Auth(server, cred)

    with pytest.raises(AuthenticationError):
        auth.authenticate()


def test_auth_successful_login():

    server = "http://localhost:5000"
    cred = Credential("admin", "1234")
    auth = Auth(server, cred)

    auth.authenticate()
    assert auth.token
