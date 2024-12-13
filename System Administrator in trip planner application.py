def system_login():
    while True:
        with open("system.txt", "r") as file:
            staff_list = [line.strip().split(",") for line in file]

        staffname = input("Enter your name: ")
        password = input("Enter your password: ")
        while True:
            for staff in staff_list:
                if staff[0] == staffname and staff[1] == password and staff[2] == "staff":
                    import time
                    time.sleep(0.5)
                    print(f"\n'{staffname}' Login Successfully!")
                    return staffname
            print("Invalid staffname or password. Please try again.")
            break


def block_traveller():
    with open("traveller_list.txt", "r") as file:
        traveller_list = file.readlines()
        for line in traveller_list:
            print(line.strip())

    while True:
        traveller = input("\nEnter the traveller that you want to block:").capitalize()
        password = input("Enter the password:")
        if traveller == "Exit":
            print("Done!")
            break
        else:
            found_traveller = False
            for i in range(len(traveller_list)):
                line = traveller_list[i].strip()
                parts = line.split(",")
                if parts[0] == traveller and parts[1] == password:
                    found_traveller = True
                    while True:
                        confirm = input("Are you sure? (yes/no):").strip().lower()
                        if confirm == "yes":
                            if parts[2] == "unBlocked":
                                parts[2] = "Blocked"
                                traveller_list[i] = ",".join(parts) + "\n"
                                print(f"{traveller} has been blocked.")
                                with open("traveller_list.txt", "w") as file:
                                    file.writelines(traveller_list)
                            elif parts[2] == "Blocked":
                                print(f"{traveller} has already been blocked.")
                            break
                        elif confirm == "no":
                            import time
                            time.sleep(0.5)
                            print("Operation cancelled.")
                            break
                        else:
                            print("Invalid response. Please enter 'yes' or 'no'.")
                    break
            if not found_traveller:
                print("Traveller Account not found. Please try again.")

            for line in traveller_list:
                print(line.strip())


def unblock_traveller():
    with open("traveller_list.txt", "r") as file:
        traveller_list = file.readlines()
        for line in traveller_list:
            print(line.strip())

    while True:
        traveller = input("\nRemove the traveller from block:").capitalize()
        password = input("Enter the password:")
        if traveller == "Exit":
            print("Done!")
            break
        else:
            found_traveller = False
            for i in range(len(traveller_list)):
                line = traveller_list[i].strip()
                parts = line.split(",")
                if parts[0] == traveller and parts[1] == password:
                    found_traveller = True
                    while True:
                        confirm = input("Are you sure? (yes/no):").strip().lower()
                        if confirm == "yes":
                            if parts[2] == "Blocked":
                                parts[2] = "unBlocked"
                                traveller_list[i] = ",".join(parts) + "\n"
                                print(f"{traveller} has been unblocked.")
                                with open("traveller_list.txt", "w") as file:
                                    file.writelines(traveller_list)
                            elif parts[2] == "unBlocked":
                                print(f"{traveller} has already been unblocked.")
                            break
                        elif confirm == "no":
                            import time
                            time.sleep(0.5)
                            print("Operation cancelled.")
                            break
                        else:
                            print("Invalid response. Please enter 'yes' or 'no'.")
                    break
            if not found_traveller:
                print("Traveller Account not found. Please try again.")

            for line in traveller_list:
                print(line.strip())



def block_merchant():
    with open("merchant_list.txt", "r") as file:
        merchant_list = file.readlines()
        for line in merchant_list:
            print(line.strip())

    while True:
        merchant = input("\nEnter the merchant that you want to block:").strip()
        password = input("Enter the password:")
        if merchant == "exit" or password == "exit":
            print("Done!")
            break
        else:
            found_merchant = False
            for i in range(len(merchant_list)):
                line = merchant_list[i].strip()
                parts = line.split(",")
                if parts[0] == merchant and parts[1] == password:
                    found_merchant = True
                    while True:
                        confirm = input("Are you sure? (yes/no):").strip().lower()
                        if confirm == "yes":
                            if parts[2] == "unBlocked":
                                parts[2] = "Blocked"
                                merchant_list[i] = ",".join(parts) + "\n"
                                print(f"{merchant} has been blocked.")
                                with open("merchant_list.txt", "w") as file:
                                    file.writelines(merchant_list)
                            elif parts[2] == "Blocked":
                                print(f"{merchant} has already been blocked.")
                            break
                        elif confirm == "no":
                            import time
                            time.sleep(0.5)
                            print("Operation cancelled.")
                            break
                        else:
                            print("Invalid response. Please enter 'yes' or 'no'.")
                    break
            if not found_merchant:
                print("Merchant Account not found. Please try again.")

            for line in merchant_list:
                print(line.strip())



def unblock_merchant():
    with open("merchant_list.txt", "r") as file:
        merchant_list = file.readlines()
        for line in merchant_list:
            print(line.strip())

    while True:
        merchant = input("\nRemove the merchant from block:").strip()
        password = input("Enter the password:")
        if merchant == "exit" or password == "exit":
            print("Done!")
            break
        else:
            found_merchant = False
            for i in range(len(merchant_list)):
                line = merchant_list[i].strip()
                parts = line.split(",")
                if parts[0] == merchant and parts[1] == password:
                    found_merchant = True
                    while True:
                        confirm = input("Are you sure? (yes/no):").strip().lower()
                        if confirm == "yes":
                            if parts[2] == "Blocked":
                                parts[2] = "unBlocked"
                                merchant_list[i] = ",".join(parts) + "\n"
                                print(f"{merchant} has been unblocked.")
                                with open("merchant_list.txt", "w") as file:
                                    file.writelines(merchant_list)
                            elif parts[2] == "unBlocked":
                                print(f"{merchant} has already been unblocked.")
                            break
                        elif confirm == "no":
                            import time
                            time.sleep(0.5)
                            print("Operation cancelled.")
                            break
                        else:
                            print("Invalid response. Please enter 'yes' or 'no'.")
                    break
            if not found_merchant:
                print("Merchant Account not found. Please try again.")

            for line in merchant_list:
                print(line.strip())



def add_merchant():
    with open("merchant_list.txt", "r") as file:
        merchant_list = file.readlines()
        for line in merchant_list:
            print(line.strip())  # strip() - remove any leading and trailing whitespace (including newlines) from the line.

    while True:  # creates an infinite loop in Python
        merchant = input("\nAdd the merchant:").strip()  # First letter capitalized
        password = input("Enter the password:")
        if merchant == "exit" or password == "exit":
            print("Done!")
            break
        else:
            with open("merchant_list.txt", "r") as file:
                merchant_list = file.readlines()

            merchant_found = False  # Assume merchant is not found initially

            for i in range(len(merchant_list)):
                line = merchant_list[i].strip()
                parts = line.split(",")
                if parts[0] == merchant or parts[1] == password:
                    merchant_found = True  # Merchant found
                    print(f"{merchant} already exists.")
                    break

            if not merchant_found:
                with open("merchant_list.txt", "a") as file:  # Append mode
                    file.write(f"\n{merchant},{password},unBlocked")
                    print(f"{merchant} has been added with status unBlocked.")

    # Print the updated merchant list
    with open("merchant_list.txt", "r") as file:
        updated_list = file.readlines()
        print("\nFinal merchant list:")
        for line in updated_list:
            print(line.strip())



### delete merchant ###

def delete_merchant():
    # Load and display the initial merchant list
    with open("merchant_list.txt", "r") as file:
        merchant_list = file.readlines()

    print("Current merchant list:")
    for line in merchant_list:
        print(line.strip())

    while True:  # Creates an infinite loop in Python
        merchant = input("\nDelete the merchant:").strip()  # First letter capitalized
        password = input("Enter the password:").strip()
        if merchant.lower() == "exit" or password.lower() == "exit":
            print("Done!")
            break
        else:
            with open("merchant_list.txt", "r") as file:
                merchant_list = file.readlines()

            found_merchant = False  # Assume merchant is not found initially

            for i in range(len(merchant_list)):
                line = merchant_list[i].strip()
                parts = line.split(",")
                if parts[0] == merchant and parts[1] == password:
                    found_merchant = True  # Merchant found
                    del merchant_list[i]  # Delete the merchant
                    print(f"{merchant} has been deleted.")
                    break

            if not found_merchant:
                print("Merchant account not found. Please try again.")
            else:
                with open("merchant_list.txt", "w") as file:
                    file.writelines(merchant_list)

            # Print the updated merchant list
            print("\nUpdated merchant list:")
            for line in merchant_list:
                print(line.strip())



def system_menu():
    staffname = system_login()
    if staffname:
        while True:
            print("1. Block Traveller")
            print("2. Unblock Traveller")
            print("3. Block Merchant")
            print("4. Unblock Merchant")
            print("5. Add Merchant")
            print("6. Delete Merchant")
            print("7. Logout")
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer number.")
            if choice == 1:
                block_traveller()
            elif choice == 2:
                unblock_traveller()
            elif choice == 3:
                block_merchant()
            elif choice == 4:
                unblock_merchant()
            elif choice == 5:
                add_merchant()
            elif choice == 6:
                delete_merchant()
            elif choice == 7:
                print("Thank you for using!")
                break
            else:
                print("Invalid choice")
    else:
        print("Login failed")

system_menu()



## update the promotion ###
#
def view_promotions():
    with open("promotion.txt", "r") as file:
        promotions = file.readlines()
    print("\nCurrent promotions:")
    for promotion in promotions:
        print(promotion.strip())  # Display each promotion


def add_promotion():
    while True:
        promotion_id = input("\nEnter promotion ID: ")
        promotion_name = input("Enter promotion name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        discount_percentage = input("Enter discount percentage: ")
        with open("promotion.txt", "r+") as file:
            promotions = file.readlines()
            for i in range(0, len(promotions), 5):  # Each promotion occupies 5 lines
                if (f"promotion_id: {promotion_id}" in promotions[i] or
                    f"promotion_name: {promotion_name}" in promotions[i + 1] or
                    f"start_date: {start_date}" in promotions[i + 2] or
                    f"start_date: {end_date}" in promotions[i + 3]):
                    print("Promotion already exists.")
                    break
                else:
                    file.write(f"\n\npromotion_id: {promotion_id}\n")
                    file.write(f"promotion_name: {promotion_name}\n")
                    file.write(f"start_date: {start_date}\n")
                    file.write(f"end_date: {end_date}\n")
                    file.write(f"discount_percentage: {discount_percentage}\n")
                    print("Promotion added successfully!")
                return



def update_promotion():
    while True:
        promotion_id = input("\nEnter the promotion ID to update:")
        with open("promotion.txt", "r") as file:
            promotions = file.readlines()

        promotion_found = False
        for i in range(0, len(promotions), 6):  # Each promotion occupies 6 lines
            if f"promotion_id: {promotion_id}\n" in promotions[i]:
                promotion_found = True
                promotions[i + 1] = f"promotion_name: {input('Enter new promotion name: ')}\n"
                promotions[i + 2] = f"start_date: {input('Enter new start date (YYYY-MM-DD): ')}\n"
                promotions[i + 3] = f"end_date: {input('Enter new end date (YYYY-MM-DD): ')}\n"
                promotions[i + 4] = f"discount_percentage: {input('Enter new discount percentage: ')}\n"
                break
        if promotion_found:
            with open("promotion.txt", "w") as file:
                file.writelines(promotions)
            print("Promotion updated successfully!")
            return
        else:
            print("Promotion not found.")




# while True:
#     print("\n1. View Promotions\n2. Add Promotion\n3. Update Promotion\n4. Exit")
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         view_promotions()
#     elif choice == "2":
#         add_promotion()
#     elif choice == "3":
#         update_promotion()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option.")

#
#
def get_recommendation(day, provide_trip):
    day_str = f"Day {day}:"
    provide_trip_str = "".join(provide_trip)
    if day_str in provide_trip_str:
        start = provide_trip_str.index(day_str)
        end = provide_trip_str.find("Day", start + len(day_str))
        if end == -1:  # If it's the last day, take everything till the end
            end = len(provide_trip_str)
        recommendation = provide_trip_str[start:end].strip()
        return recommendation
    else:
        return "Day not found in the trip recommendation."

# def main():
#     with open("trip.txt", "r") as file:
#         provide_trip = file.readlines()
#     for trip in provide_trip:
#         print(trip.strip())
#
#     while True:
#         guest_input = input("\n\nEnter the day number (1-7) you want recommendations for (or 'exit' to quit):").strip()
#         if guest_input.lower() == "exit":
#             print("Thank you! Have a great trip!")
#             break
#         if guest_input.isdigit() and 1 <= int(guest_input) <= 7: #isdigit - checks whether all characters in a string are digits (0-9)
#             day = int(guest_input)
#             recommendation = get_recommendation(day, provide_trip)
#             print("\n" + recommendation + "\n")
#         else:
#             print("Invalid response. Please enter a number between 1 and 7, or 'exit' to quit.")
#
# main()




