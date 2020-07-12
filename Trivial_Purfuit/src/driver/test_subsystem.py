import pytest
from ..die.die import Die


# create test instance
die = Die()


@pytest.mark.die
def test_roll_return_type():
    assert type(die.roll()) == int


@pytest.mark.die
def test_roll_number_return_range():
    assert 1 <= die.roll() <= 6


