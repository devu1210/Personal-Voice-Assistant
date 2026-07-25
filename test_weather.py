from weather import get_weather

city = input("Enter City: ")

weather = get_weather(city)

if weather:
    print("\n" + "=" * 45)
    print("        🌤 CURRENT WEATHER REPORT")
    print("=" * 45)
    print(f"📍 Location     : {weather['city']}, {weather['country']}")
    print(f"🌡 Temperature  : {weather['temperature']} °C")
    print(f"🤗 Feels Like   : {weather['feels_like']} °C")
    print(f"💧 Humidity     : {weather['humidity']} %")
    print(f"🌬 Wind Speed   : {weather['wind']} m/s")
    print(f"☁ Condition     : {weather['description']}")
    print("=" * 45)
else:
    print("❌ Unable to fetch weather.")