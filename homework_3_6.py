def gas_station(distance, tank_size, stations):
    result = []
    empty_tank = 0 + tank_size

    if tank_size > distance:
        return result

    for station_idx in range(0, len(stations) - 1):
        if empty_tank < stations[station_idx + 1]:
            result.append(stations[station_idx])
        
    result.append(stations[-1])
    return result

pass

print(gas_station(320, 90, [50, 80, 140, 180, 220, 290]))
