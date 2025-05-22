india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter the first city name: ").strip().lower()
city2 = input("Enter the second city name: ").strip().lower()

if city1 in india and city2 in india:
    print(f"Both {city1.title()} and {city2.title()} are in India.")
elif city1 in pakistan and city2 in pakistan:
    print(f"Both {city1.title()} and {city2.title()} are in Pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"Both {city1.title()} and {city2.title()} are in Bangladesh.")
else:
    print(f"{city1.title()} and {city2.title()} are not in the same country.")
