def gas_station(distance, tank_size, stations):
    result = []
    current_position = 0
    tank_level = tank_size

    for station in stations:
        while station - current_position > tank_level:
            return []
            result.append(current_position)
            tank_level = tank_size

        current_position = station

    result.append(current_position)
    return result


print(gas_station(390, 80, [70, 90, 140, 210, 240, 280, 350]))
