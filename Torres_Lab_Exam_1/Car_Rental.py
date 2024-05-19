def create_car(id, make, model, year):
    return {
        'id': id,
        'model': model,
        'year': year,
        'is_rented': False
    }

def add_car(fleet, car):
    return fleet + [car]

def list_cars(fleet):
    print("\nAvailable Cars:")
    for car in fleet:
        if not car['is_rented']:
            print(f"{car['year']} {car['model']} (ID: {car['id']}) - Available")
    
    print("\nRented Cars:")
    for car in fleet:
        if car['is_rented']:
            print(f"{car['year']} {car['model']} (ID: {car['id']}) - Rented")

def rent_car(fleet, id):
    updated_fleet = []
    car_found = False
    for car in fleet:
        if car['id'] == id and not car['is_rented']:
            updated_fleet.append({**car, 'is_rented': True})
            car_found = True
        else:
            updated_fleet.append(car)
    
    if car_found:
        print(f"Car with ID {id} has been rented.")
    else:
        print(f"No available car with ID {id} found.")
    return updated_fleet

def return_car(fleet, id):
    updated_fleet = []
    car_found = False
    for car in fleet:
        if car['id'] == id and car['is_rented']:
            updated_fleet.append({**car, 'is_rented': False})
            car_found = True
        else:
            updated_fleet.append(car)
    
    if car_found:
        print(f"Car with ID {id} has been returned.")
    else:
        print(f"No rented car with ID {id} found.")
    return updated_fleet

def main():
    fleet = []
    while True:
        print("\n--- Car Rental Service ---")
        print("1. Add new car")
        print("2. List cars")
        print("3. Rent a car")
        print("4. Return a car")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter car ID: ")
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            new_car = create_car(id, model, year)
            fleet = add_car(fleet, new_car)
            print(f"Car {new_car['year']} {new_car['model']} added to the fleet.")
        elif choice == "2":
            list_cars(fleet)
        elif choice == "3":
            id = input("Enter car ID to rent: ")
            fleet = rent_car(fleet, id)
        elif choice == "4":
            id = input("Enter car ID to return: ")
            fleet = return_car(fleet, id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()