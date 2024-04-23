import pytest
from src.masks import masks_card, masks_account


@pytest.fixture
def coll():
    return "7000792289606361"


def test_process_info(coll):
    assert masks_card(coll) == "7000 79** **** 6361"
