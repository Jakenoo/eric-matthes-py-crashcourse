from employee import Employee; import pytest

@pytest.fixture
def some_person():
    """a person available to all test functions"""
    some_person = Employee("some", 'person', 70000)
    return some_person

def test_give_default_raise(some_person):
    """tests that default raise value in method is working as intended"""
    some_person.give_raise()
    assert some_person.salary == 75000

def test_give_custom_raise(some_person):
    """tests that custom raises works"""
    some_person.give_raise(10000)
    assert some_person.salary == 80000