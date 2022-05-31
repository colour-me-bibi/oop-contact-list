
from dataclasses import dataclass, field

# TODO set for shared contacts
# TODO heap for contacts


@dataclass
class Contact:
    name: str
    number: str


@dataclass
class ContactList:
    name: str
    contacts: list[Contact] = field(default_factory=list)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.contacts.sort(key=lambda c: c["name"])

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c["name"] != name]

    def find_shared_contacts(self, other_list):
        others = set(contact["name"] for contact in other_list.contacts)
        return [contact for contact in self.contacts if contact["name"] in others]


def main():
    friends = [{"name": "Alice", "number": "867-5309"}, {"name": "Bob", "number": "555-5555"}]
    work_buddies = [{"name": "Alice", "number": "867-5309"}, {"name": "Carlos", "number": "555-5555"}]

    my_friends_list = ContactList("My Friends", friends)
    print(my_friends_list)

    my_work_buddies = ContactList("Work Buddies", work_buddies)
    print(my_work_buddies)

    friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
    # friends_i_work_with should be: [{"name":"Alice","number":"867-5309"}]

    print(friends_i_work_with)


if __name__ == "__main__":
    main()
