import os

class PhoneBook:
    def __init__(self, cache_directory):
        self._phonebook = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name, number):
        self._phonebook[name] = number

    def lookup(self, name):
        return self._phonebook[name]

    def is_consistent(self):
        for name1, number1 in self._phonebook.items():
            for name2, number2 in self._phonebook.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def get_numbers(self):
        pass

    def get_names(self):
        pass

    def names(self):
        return set(self._phonebook.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
