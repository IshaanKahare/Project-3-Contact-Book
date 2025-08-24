import os

class Contact:
    """A single node in the linked list representing a contact."""
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None

    def __str__(self):
        """String representation for easy printing."""
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    """Manages the linked list of contacts and file persistence."""
    def __init__(self, filename="contacts.txt"):
        self.head = None
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        """Loads contacts from the file and builds the linked list."""
        if not os.path.exists(self.filename):
            print("No contacts file found. Starting with an empty contact book.")
            return

        with open(self.filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                # Insert contacts to maintain alphabetical order
                self._insert_sorted(Contact(name, phone, email))
        print("Contacts loaded successfully.")

    def save_contacts(self):
        """Saves all contacts from the linked list to the file."""
        with open(self.filename, 'w') as file:
            current = self.head
            while current:
                file.write(f"{current.name},{current.phone},{current.email}\n")
                current = current.next
        print("Contacts saved successfully.")

    def _insert_sorted(self, new_contact):
        """
        Inserts a new contact node into the linked list while maintaining
        alphabetical order by name. This is a helper method.
        """
        # If the list is empty or the new contact should be the new head
        if not self.head or new_contact.name.lower() < self.head.name.lower():
            new_contact.next = self.head
            self.head = new_contact
            return

        # Find the correct position to insert the new contact
        current = self.head
        while current.next and current.next.name.lower() < new_contact.name.lower():
            current = current.next

        new_contact.next = current.next
        current.next = new_contact

    def add_contact(self, name, phone, email):
        """Creates and adds a new contact to the book."""
        new_contact = Contact(name, phone, email)
        self._insert_sorted(new_contact)
        print(f"Contact '{name}' added successfully.")
        self.save_contacts()

    def view_contacts(self):
        """Displays all contacts in the book."""
        if not self.head:
            print("Contact book is empty.")
            return

        print
