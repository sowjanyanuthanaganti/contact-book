contacts=[]
def add_contact(name,phone,email,address):
    contacts.append({"name":name,"phone":phone,"email":email,"address":address})
    print("contavt added successfully")
def view_contacts():
    if contacts:
        for contact in contacts:
            print(f"Name:{contact["name"]},phone:{contact ["phone"]}")
    else:
        print("no contacts available")
def search_contact(keyword):
    found=False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print(f"Name:{contact["name"]},phone:{contact["phone"]}")
            found=True
    if not found:
        print("contact not found")
def update_contact(name,phone,email,address):
    for contact in contacts:
        if contact["name"]==name:
            contact.update({"phone":phone,"email":email,"address":address})
            print("contact uploaded successfully")
            return
    print("contact not found")
def delete_contact(name):
    for contact in contacts:
        if contact["name"]==name:
            contacts.remove(contact)
            print("contacts deleted successfully")
            return
    print("contact not found")
while True:
    print("\nMenu:")
    print("1.Add Contact")
    print("2.View Contact List")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        name=input("Enter name:")
        phone=input("Enter phone number:")
        email=input("Enter email:")
        address=input("Enter address:")
        add_contact(name,phone,email,address)
    elif choice=="2":
        print("Contact List:")
        view_contacts()
    elif choice=="3":
        keyword=input("Enter name or phone number to search")
        search_contact(keyword)
    elif choice=="4":
        name=input("Enter name of contact to update")
        email=input("Enter new mail:")
        address=input("Enter new address:")
        update_contact(name,phone,email,address)
    elif choice=="5":
        name=input("Enter name of contact to delete")
        delete_contact(name)
    elif choice=="6":
        print("Exiting")
        break
    else:
        print("invalid choice,enter number between 1 and 6:")
         
        
