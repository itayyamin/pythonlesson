def create_underground_stations(n):
    stations_dict = {}
    for _ in range(n):
        station_name = input("Enter the station's name: ")
        fare_zone = int(input("Enter the station's fare zone: "))
        stations_dict[station_name] = fare_zone
    return stations_dict


def calculate_trip_cost(station_zones, origin, destination):
    zone_diff = abs(station_zones[origin] - station_zones[destination])
    if zone_diff == 0:
        return 2.5
    elif zone_diff == 1:
        return 3.0
    elif zone_diff == 2:
        return 3.8
    else:
        return 5.0


def main():

    #    station_zones = {
    #     "Camden Town": 2,
    #     "Oxford Circus": 1,
    #     "Wembley Park": 4,
    #     "Baker Street": 1,
    #     "Stratford": 3,
    #     "Green Park": 1,
    #     "Canada Water": 2,
    # }
    #
    # # Step 2 & 3: Predefined trips
    # trips = [
    #     ("Camden Town", "Oxford Circus"),   # zone diff = 1 → £3.0
    #     ("Wembley Park", "Baker Street"),   # zone diff = 3 → £5.0
    #     ("Stratford", "Canada Water"),      # zone diff = 1 → £3.0
    #     ("Green Park", "Oxford Circus"),    # zone diff = 0 → £2.5
    #     ("Camden Town", "Wembley Park"),    # zone diff = 2 → £3.8
    # ]

    # Step 1: Create stations dictionary
    n = int(input("Enter the number of stations: "))
    station_zones = create_underground_stations(n)

    # Step 2 & 3: Trip fare calculations
    m = int(input("Enter the number of trips: "))
    total_cost = 0
    fare_counts = {}

    for _ in range(m):
        origin = input("Enter the origin station: ")
        destination = input("Enter the destination station: ")
        fare = calculate_trip_cost(station_zones, origin, destination)
        print(f"Origin: {origin}, Destination: {destination}, Fare: £{fare}")
        total_cost += fare
        if fare not in fare_counts:
            fare_counts[fare] = 0
        fare_counts[fare] += 1

    average_cost = total_cost / m

    print(f"\nTotal cost: £{total_cost}")
    print(f"Average cost: £{average_cost}")
    print("Trips per fare:")
    for fare, count in fare_counts.items():
        print(f"£{fare}: {count} trip(s)")


if __name__ == "__main__":
    main()
