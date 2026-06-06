def weather_tool():
    return "Mock weather: 31°C"

def calculator_tool():
    return 10 + 20

query = input("Ask something: ").lower()

if "weather" in query:
    print("Tool selected: weather_tool")
    print(weather_tool())

elif "calculate" in query or "add" in query:
    print("Tool selected: calculator_tool")
    print(calculator_tool())

else:
    print("No tool needed. Giving direct response.")
#here we can see tool selection is done based on user query
