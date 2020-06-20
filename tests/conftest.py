import pytest

from src.phonebook.phonebook import PhoneBook

@pytest.fixture
def phonebook(tmpdir):
    return PhoneBook(tmpdir)