class vehicle:
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service_date = service_date


    def get_full_car(self):
        return self.brand + " " + self.model


def list_all_vehicles(vehicles):
    for index, car in enumerate(vehicles):
        print "ID: " + str(index)  # index is an order number of the contact object in the contacts list
        print car.get_full_car()
        print car.kilometers
        print car.service_date
        print ""  # empty line

    if not vehicles:
        print "You don't have any contacts in your contact list."


def add_new_vehicle(vehicles):
    brand = raw_input("Please enter the vehicles brand: ")
    model = raw_input("Please enter the model: ")
    kilometers = raw_input("Please enter the kilometers the vehicle has done so far: ")
    date = raw_input("Please enter the next service date for the vehicle: ")

    new = vehicle(brand=brand, model=model, kilometers=kilometers, service_date=date)
    vehicles.append(new)

    print ""  # empty line
    print new.get_full_car() + " was successfully added to your vehicle list."


def edit_vehicle(vehicles):
    print "Select the number of the vehicle you'd like to edit:"

    for index, car in enumerate(vehicles):
        print str(index) + ") " + car.get_full_car()

    print ""  # empty line
    selected_id = raw_input("Which vehicle would you like to edit? (enter ID number): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_km = raw_input("Please enter a new kilometer count for %s: " % selected_vehicle.get_full_car())
    selected_vehicle.kilometers = new_km

    print ""  # empty line
    print "Kilometers updated."

    new_date = raw_input("Please enter a new service date for %s: " % selected_vehicle.get_full_car())
    selected_vehicle.service_date = new_date

    print ""  # empty line
    print "Service date updated."



    # ... you can do the same for other fields.



def main():
    print "Welcome to your Vehicle List"

    # let's add some contacts in our contact list so it's not empty
    merc = vehicle(brand="Mercedes", model="210", kilometers="30000", service_date="5.5.2017")
    peugeot = vehicle(brand="Peugeot", model="207", kilometers="70000", service_date="7.8.2017")
    vehicles = [merc, peugeot]

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit a vehicles kilometers and service date"
        print "d) store in txt file"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, or d): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_vehicles(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_vehicle(vehicles)
        elif selection.lower() == "d":
            print "Thank you for using Vehicle List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
     main()