from models.pollutant import Pollutant
from storage.file_handler import save
from utils.validators import validate

def add_record():
    time = input("Enter timestamp: ")
    pm25 = validate(input("PM2.5: "))
    pm10 = validate(input("PM10: "))

    if pm25 is None or pm10 is None:
        return

    p = Pollutant(time, pm25, pm10)

    aqi = p.calculate_aqi()
    category = p.get_category()

    print(f"AQI: {aqi} ({category})")

    save([time, pm25, pm10, aqi, category])