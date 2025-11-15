"""
Command-line weather app using the OpenWeather API.

What this program does:
- Lets you look up the current weather for any city.
- Lets you save up to 3 favourite cities.
- Lets you view and update your favourite cities.

Before running:
- You need Python 3.8 or higher.
- Install the 'requests' library: pip install requests
- Get an API key from OpenWeather: https://openweathermap.org/api
- Set it as an environment variable named: OPENWEATHER_API_KEY
"""

import os
import sys
import requests

# URL for the OpenWeather "current weather" endpoint
API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
# Name of the environment variable where we expect the API key
API_KEY_ENV_VAR = "OPENWEATHER_API_KEY" #I do not have an API key, but if I did I put it here.


class WeatherApp:
    def __init__(self):
        """
        Set up the app by reading the API key and creating the favourites list.
        """
        # Read the API key from the environment
        self.api_key = os.getenv(API_KEY_ENV_VAR)
        if not self.api_key:
            print(f"ERROR: Please set your OpenWeather API key in the "
                  f"{API_KEY_ENV_VAR} environment variable.")
            sys.exit(1)

        # Favourite cities are only kept in memory (not saved to a file or database)
        self.favourites = []  # list of city names (strings), maximum of 3 cities

    # ---------- Core API integration ----------

    def get_weather_for_city(self, city_name: str):
        """
        Ask the OpenWeather API for the current weather for the given city.

        Returns:
        - A dictionary with the weather data if the request works.
        - None if something goes wrong (network error, bad city name, etc.).
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric",  # get temperatures in Celsius
        }

        try:
            response = requests.get(API_BASE_URL, params=params, timeout=10)
        except requests.RequestException as exc:
            # This happens if there is a network problem (no internet, timeout, etc.)
            print(f"Network error while calling OpenWeather: {exc}")
            return None

        # If the API did not return a "success" status code
        if response.status_code != 200:
            # Try to show a helpful error message from the API response
            try:
                data = response.json()
                message = data.get("message", "Unknown error")
            except ValueError:
                message = "Unknown error"
            print(f"API error ({response.status_code}): {message}")
            return None

        # Try to turn the API response into a Python dictionary
        try:
            return response.json()
        except ValueError:
            print("Failed to parse JSON from OpenWeather response.")
            return None

    # ---------- Presentation helpers ----------

    @staticmethod
    def format_weather(weather_data: dict) -> str:
        """
        Turn raw weather data into a nice, readable text block.
        """
        # Use default values if some fields are missing
        name = weather_data.get("name", "Unknown city")
        main = weather_data.get("main", {})
        weather_list = weather_data.get("weather", [])
        wind = weather_data.get("wind", {})

        # Weather description like "clear sky", "light rain", etc.
        description = weather_list[0]["description"] if weather_list else "N/A"
        temp = main.get("temp", "N/A")
        feels_like = main.get("feels_like", "N/A")
        humidity = main.get("humidity", "N/A")
        wind_speed = wind.get("speed", "N/A")

        return (
            f"City: {name}\n"
            f"  Description : {description}\n"
            f"  Temperature : {temp} °C (feels like {feels_like} °C)\n"
            f"  Humidity    : {humidity}%\n"
            f"  Wind Speed  : {wind_speed} m/s\n"
        )

    # ---------- Favourites management ----------

    def add_favourite(self, city_name: str):
        """
        Add a city to the favourites list, if:
        - The name is not empty
        - It is not already in the list
        - The list has fewer than 3 cities
        """
        city_name = city_name.strip()
        if not city_name:
            print("City name cannot be empty.")
            return

        if city_name in self.favourites:
            print(f"{city_name} is already in favourites.")
            return

        if len(self.favourites) >= 3:
            print("Favourites list is full (max 3 cities).")
            print("Use option 4 to update favourites (remove and add).")
            return

        self.favourites.append(city_name)
        print(f"Added '{city_name}' to favourites.")

    def list_favourites_with_weather(self):
        """
        Show each favourite city and its current weather.
        """
        if not self.favourites:
            print("No favourite cities yet.")
            return

        print("\nFavourite Cities:\n-----------------")
        for city in self.favourites:
            # Print the name of the city
            print(f"-> {city}")
            # Look up the weather for this city
            data = self.get_weather_for_city(city)
            if data:
                print(self.format_weather(data))
            else:
                print("  (Could not fetch weather data.)\n")

    def update_favourites(self):
        """
        Let the user:
        - Remove one city from the favourites list
        - Optionally add a new city after removing (still max 3 total)
        """
        if not self.favourites:
            print("No favourites to update yet.")
            return

        # Show current favourite cities with numbers so the user can pick one
        print("\nCurrent favourites:")
        for idx, city in enumerate(self.favourites, start=1):
            print(f"{idx}. {city}")

        # Ask which city number to remove
        try:
            to_remove = int(input("Enter the number of the city to remove (or 0 to cancel): "))
        except ValueError:
            print("Invalid input.")
            return

        # If the user changes their mind
        if to_remove == 0:
            print("Update cancelled.")
            return

        # Check that the chosen number is valid
        if not (1 <= to_remove <= len(self.favourites)):
            print("Invalid choice.")
            return

        # Remove the selected city (list is 0-based, menu is 1-based)
        removed_city = self.favourites.pop(to_remove - 1)
        print(f"Removed '{removed_city}' from favourites.")

        # If there is space, ask if the user wants to add a new city
        if len(self.favourites) < 3:
            add_new = input("Do you want to add a new city? (y/n): ").strip().lower()
            if add_new == "y":
                new_city = input("Enter the name of the new city: ")
                self.add_favourite(new_city)

    # ---------- Menu / CLI ----------

    def search_and_display_weather(self):
        """
        Ask the user for a city name and show its current weather.
        """
        city_name = input("Enter city name: ").strip()
        if not city_name:
            print("City name cannot be empty.")
            return

        data = self.get_weather_for_city(city_name)
        if data:
            print(self.format_weather(data))

    def print_menu(self):
        """
        Show the main menu options to the user.
        """
        print("\n==== Weather CLI ====")
        print("1. Search weather for a city")
        print("2. Add a city to favourites (max 3)")
        print("3. List favourite cities with weather")
        print("4. Update favourites (remove/add)")
        print("5. Exit")

    def run(self):
        """
        Main loop of the program.

        Repeatedly:
        - Show the menu
        - Read the user's choice
        - Call the matching function
        - Exit when the user chooses option 5
        """
        while True:
            self.print_menu()
            choice = input("Select an option (1-5): ").strip()

            if choice == "1":
                self.search_and_display_weather()
            elif choice == "2":
                city = input("Enter city to add to favourites: ")
                self.add_favourite(city)
            elif choice == "3":
                self.list_favourites_with_weather()
            elif choice == "4":
                self.update_favourites()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    # Create the app and start the menu loop
    app = WeatherApp()
    app.run()
