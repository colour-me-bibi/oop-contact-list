
from dataclasses import dataclass, field

# TODO set for shared contacts
# TODO heap for contacts


@dataclass(frozen=True)
class Contact:
    name: str
    number: str


@dataclass
class ContactList:
    name: str
    contacts: list[Contact] = field(default_factory=list)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.contacts.sort(key=lambda contact: contact["name"])

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"] != name]

    def find_shared_contacts(self, other_list):
        return ContactList(
            name=f"{self.name} & {other_list.name}",
            contacts=list(set(self.contacts) & set(other_list.contacts)),
        )


def main():
    friends = [{"name": "Alice", "number": "867-5309"}, {"name": "Bob", "number": "555-5555"}]
    work_buddies = [{"name": "Alice", "number": "867-5309"}, {"name": "Carlos", "number": "555-5555"}]

    my_friends_list = ContactList("My Friends", [Contact(**contact) for contact in friends])
    print(my_friends_list)

    my_work_buddies = ContactList("Work Buddies", [Contact(**contact) for contact in work_buddies])
    print(my_work_buddies)

    friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
    # friends_i_work_with should be: [{"name":"Alice","number":"867-5309"}]

    print(friends_i_work_with)

    """
    ContactList(
        name='My Friends',
        contacts=[Contact(name='Alice', number='867-5309'), Contact(name='Bob', number='555-5555')],
    )
    ContactList(
        name='Work Buddies',
        contacts=[Contact(name='Alice', number='867-5309'), Contact(name='Carlos', number='555-5555')],
    )
    ContactList(
        name='My Friends & Work Buddies',
        contacts=[Contact(name='Alice', number='867-5309')],
    )
    """


if __name__ == "__main__":
    main()
