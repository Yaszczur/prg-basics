def ms_to_kmh(ms):
    kmh = ms * 3.6
    return kmh

speed1_ms = 10
speed2_ms = 35

print(f"{speed1_ms} m/s = {ms_to_kmh(speed1_ms)} km/h")
print(f"{speed2_ms} m/s = {ms_to_kmh(speed2_ms)} km/h")