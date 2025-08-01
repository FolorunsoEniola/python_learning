missions = []
mission_details = {}

def add_mission(missions, mission_details, name, details):
    missions[mission_details] = {'name': name, 'details': details}
    pass

def update_mission(mission_details, name, key, value):
    mission_details = {'name': name, 'key': key, 'value': value}
    pass

def display_missions(missions, mission_details):
    print(display_missions())
    pass

def list_astronauts(mission_details):
    print(mission_details)
    pass

# Main menu loop
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        display_missions(missions, mission_details)

    elif choice == '4':
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# Space Math Module

def calculate_fuel(distance):
    # Calculate fuel needed for the journey
    # Formula: fuel = distance * 500
    return distance * 500
    pass

def time_to_destination(distance, speed):
    # Calculate time to reach the destination
    # Formula: time = distance / speed
    return distance / speed
    pass

def gravity_force(mass1, mass2, distance):
    # Calculate the gravitational force between two objects
    # Formula: force = (G * mass1 * mass2) / (distance ** 2)
    # Where G is the gravitational constant (G = 6.67430e-11)
    G = 6.67430e-11
    return G * mass1 * mass2 / distance ** 2
    pass
