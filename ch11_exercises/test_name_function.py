#2/27/2024; another example from chapter 11
from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('sandy', 'cheeks')
    assert formatted_name == 'Sandy Cheeks'

def test_middle_name():
    formatted_name = get_formatted_name('eugene', 'krabs', 'harold')
    assert formatted_name == 'Eugene Harold Krabs'