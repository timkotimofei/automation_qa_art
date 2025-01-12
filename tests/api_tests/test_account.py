import requests


def test_authorized_status_code_is_200(authorized):
    assert authorized.status_code == 200