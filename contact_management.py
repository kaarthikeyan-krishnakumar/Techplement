import json
import os
import re

CONTACTS_FILE = "contacts.json"

# Load existing contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Add new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number (10 digits): ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Must be exactly 10 digits.")
        return

    email = input("Enter email address: ").strip()
    if not is_valid_email(email):
        print("Invalid email format.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added successfully.")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}\n")
    else:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter the name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave field empty to keep existing value.")

    new_phone = input("Enter new phone number (10 digits): ").strip()
    if new_phone:
        if new_phone.isdigit() and len(new_phone) == 10:
            contacts[name]["phone"] = new_phone
        else:
            print("Invalid phone number. Skipping phone update.")

    new_email = input("Enter new email address: ").strip()
    if new_email:
        if is_valid_email(new_email):
            contacts[name]["email"] = new_email
        else:
            print("Invalid email format. Skipping email update.")

    print("Contact updated successfully.")

# Menu loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
