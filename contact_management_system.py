import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"\n Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("\n No contacts found!\n")
        return
    print("\n Contact List:")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    print()

# Edit existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print("Leave blank to keep existing info.")
        phone = input(f"New Phone ({contacts[name]['phone']}): ").strip() or contacts[name]['phone']
        email = input(f"New Email ({contacts[name]['email']}): ").strip() or contacts[name]['email']
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print(f"\n Contact '{name}' updated successfully!\n")
    else:
        print("\n Contact not found!\n")

# Delete contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"\n Contact '{name}' deleted successfully!\n")
    else:
        print("\n Contact not found!\n")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("===== Contact Management System =====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\n Exiting... Goodbye!")
            break
        else:
          print("\n Invalid choice. Please try again!\n")

if __name__ == "__main__":
    main()

