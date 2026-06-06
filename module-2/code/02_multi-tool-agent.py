import json

def weather_tool(city):
    return f"The weather in {city} is 31°C."

def calculator_tool(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"

def internship_tool(domain):
    return f"Found 5 mock internships in {domain}."

def detect_intent(query):
    query = query.lower()

    if "weather" in query:
        return {
            "intent": "weather",
            "tool": "weather_tool",
            "arguments": {
                "city": "Trivandrum"
            }
        }

    elif "calculate" in query or "+" in query or "*" in query:
        return {
            "intent": "calculation",
            "tool": "calculator_tool",
            "arguments": {
                "expression": query.replace("calculate", "").strip()
            }
        }

    elif "internship" in query:
        return {
            "intent": "internship_search",
            "tool": "internship_tool",
            "arguments": {
                "domain": "AI/ML"
            }
        }

    else:
        return {
            "intent": "general",
            "tool": None,
            "arguments": {}
        }

def run_agent(query):
    print("\nTHOUGHT: Understanding user query...")

    plan = detect_intent(query)

    print("\nSTRUCTURED TOOL CALL:")
    print(json.dumps(plan, indent=4))

    if plan["tool"] == "weather_tool":
        result = weather_tool(plan["arguments"]["city"])

    elif plan["tool"] == "calculator_tool":
        result = calculator_tool(plan["arguments"]["expression"])

    elif plan["tool"] == "internship_tool":
        result = internship_tool(plan["arguments"]["domain"])

    else:
        result = "This can be answered directly without tools."

    print("\nOBSERVATION:")
    print(result)

    print("\nFINAL ANSWER:")
    print(result)

query = input("Ask the agent: ")
run_agent(query)
"""
these tools are functions but in real agent systems these functions 
would be connected to the api(weather ,internship scrapping) , here we see only a mock up of 
the real tools that would be used in real agents
Remember : A tool is a function with a purpose, description, and
permission to be used by an agent.
"""