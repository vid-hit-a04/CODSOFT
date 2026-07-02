# Contact Book Application

print("Welcome to Contact Book")

contacts = {}

while True:
    print("\n--- MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD CONTACT
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }

        print("Contact added successfully!")

    # VIEW CONTACTS
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, details in contacts.items():
                print("\nName:", name)
                print("Phone:", details["phone"])

    # SEARCH CONTACT
    elif choice == "3":
        search = input("Enter name or phone to search: ")
        found = False

        for name, details in contacts.items():
            if search == name or search == details["phone"]:
                print("\nContact Found:")
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("Address:", details["address"])
                found = True

        if not found:
            print("Contact not found.")

    # UPDATE CONTACT
    elif choice == "4":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }

            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # DELETE CONTACT
    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # EXIT
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")