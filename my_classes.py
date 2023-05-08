from collections import UserDict

class AddressBook(UserDict):
    """A class representing an address book, which contains a collection of Record objects."""

    def add_record(self, record):
        """Add a record to the address book."""
        self.data[record.name.value] = record
        return "successfully added"

    def delete_record(self, record):
        """Delete a contact in the address book."""
        del self.data[record.name.value] 
        return "successfully removed"


class Record:
    """A class representing a record in an address book."""

    def __init__(self, name, phone, *_):
        self.name = name
        self.phones = [phone] + [i for i in _]

    def add_phone(self, phone):
        self.phones.append(phone)
        return "successfully added"

    def change_phone(self, phone):
        self.phones = [phone]
        return "successfully changed"

    def delete_phone(self, phone):
        for i in self.phones:
            if i.value==phone:
                self.phones.remove(i)
                return "successfully deleted"
        return "such phone number not found"


class Field:
    """A class representing a generic field."""

    def __init__(self, value):
        self.value = value


class Name(Field):
    """idk what's specific about the phone or name fields yet."""

    pass


class Phone(Field):
    """idk what's specific about the phone or name fields yet."""

    pass