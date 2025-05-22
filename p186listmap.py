india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input("Enter the city name: ").strip().lower()

if city_name in india:
    print(f"{city_name.title()} belongs to India.")
elif city_name in pakistan:
    print(f"{city_name.title()} belongs to Pakistan.")
elif city_name in bangladesh:
    print(f"{city_name.title()} belongs to Bangladesh.")
else:
    print(f"{city_name.title()} is not in the list.")
