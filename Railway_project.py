import random
import string

# -------------------------------
# Railway Ticket Reservation System
# -------------------------------

trains = {
    "12723": {
        "name": "Telangana Express",
        "source": "Hyderabad",
        "destination": "New Delhi",
        "seats": 50,
        "fare": 850
    },
    "12760": {
        "name": "Charminar Express",
        "source": "Hyderabad",
        "destination": "Chennai",
        "seats": 50,
        "fare": 650
    },
    "17015": {
        "name": "Visakha Express",
        "source": "Hyderabad",
        "destination": "Bhubaneswar",
        "seats": 50,
        "fare": 700
    },
    "12702": {
        "name": "Hussainsagar Express",
        "source": "Mumbai",
        "destination": "Hyderabad",
        "seats": 50,
        "fare": 600
    }
}

bookings = {}


# Generate PNR
def generate_pnr():
    while True:
        pnr = ''.join(random.choices(string.digits, k=10))
        if pnr not in bookings:
            return pnr


# Display all trains
def display_trains():
    print("\n========== AVAILABLE TRAINS ==========")

    for number, train in trains.items():
        print(f"\nTrain Number : {number}")
        print(f"Train Name   : {train['name']}")
        print(f"From         : {train['source']}")
        print(f"To           : {train['destination']}")
        print(f"Seats        : {train['seats']}")
        print(f"Fare         : ₹{train['fare']}")


# Search train
def search_train():
    source = input("\nEnter source station: ").strip().lower()
    destination = input("Enter destination station: ").strip().lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for number, train in trains.items():
        if (train["source"].lower() == source and
                train["destination"].lower() == destination):

            print(f"\nTrain Number : {number}")
            print(f"Train Name   : {train['name']}")
            print(f"Seats        : {train['seats']}")
            print(f"Fare         : ₹{train['fare']}")

            found = True

    if not found:
        print("\nNo trains found for the selected route.")


# Book ticket
def book_ticket():
    display_trains()

    train_number = input("\nEnter train number: ").strip()

    if train_number not in trains:
        print("Invalid train number.")
        return

    train = trains[train_number]

    if train["seats"] <= 0:
        print("Sorry! No seats available.")
        return

    name = input("Enter passenger name: ").strip()
    age = input("Enter passenger age: ").strip()
    gender = input("Enter gender: ").strip()

    try:
        age = int(age)
    except ValueError:
        print("Invalid age.")
        return

    pnr = generate_pnr()

    train["seats"] -= 1

    bookings[pnr] = {
        "name": name,
        "age": age,
        "gender": gender,
        "train_number": train_number,
        "train_name": train["name"],
        "source": train["source"],
        "destination": train["destination"],
        "fare": train["fare"],
        "status": "Confirmed"
    }

    print("\n========== TICKET BOOKED SUCCESSFULLY ==========")
    print(f"PNR Number    : {pnr}")
    print(f"Passenger     : {name}")
    print(f"Train         : {train['name']}")
    print(f"From          : {train['source']}")
    print(f"To            : {train['destination']}")
    print(f"Fare          : ₹{train['fare']}")
    print("Status        : Confirmed")


# View ticket
def view_ticket():
    pnr = input("\nEnter PNR number: ").strip()

    if pnr not in bookings:
        print("PNR not found.")
        return

    ticket = bookings[pnr]

    print("\n========== TICKET DETAILS ==========")
    print(f"PNR Number    : {pnr}")
    print(f"Passenger     : {ticket['name']}")
    print(f"Age           : {ticket['age']}")
    print(f"Gender        : {ticket['gender']}")
    print(f"Train Number  : {ticket['train_number']}")
    print(f"Train Name    : {ticket['train_name']}")
    print(f"From          : {ticket['source']}")
    print(f"To            : {ticket['destination']}")
    print(f"Fare          : ₹{ticket['fare']}")
    print(f"Status        : {ticket['status']}")


# Cancel ticket
def cancel_ticket():
    pnr = input("\nEnter PNR number to cancel: ").strip()

    if pnr not in bookings:
        print("PNR not found.")
        return

    ticket = bookings[pnr]

    if ticket["status"] == "Cancelled":
        print("Ticket is already cancelled.")
        return

    ticket["status"] = "Cancelled"

    train_number = ticket["train_number"]
    trains[train_number]["seats"] += 1

    print("\nTicket cancelled successfully.")
    print(f"PNR Number: {pnr}")


# Main menu
def main():
    while True:
        print("\n")
        print("==========================================")
        print("     RAILWAY TICKET RESERVATION SYSTEM")
        print("==========================================")
        print("1. Display All Trains")
        print("2. Search Train")
        print("3. Book Ticket")
        print("4. View Ticket")
        print("5. Cancel Ticket")
        print("6. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_trains()

        elif choice == "2":
            search_train()

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            view_ticket()

        elif choice == "5":
            cancel_ticket()

        elif choice == "6":
            print("\nThank you for using Railway Reservation System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()