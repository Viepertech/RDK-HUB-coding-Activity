# RDK-HUB-coding-Activity
This is for an RDK-HUB coding activity, upon request it will be made private. the project was done using python3.

## Weather CLI App & Median Calculator

This repository contains two small Python applications developed for the GCS Academy Coding Assessment:

* **Weather CLI App**:  A menu-based program that retrieves real-time weather information using the OpenWeather API and allows managing up to three favourite cities.
* **Median Calculator**:   A program that implements a custom selection-sort algorithm and computes the median value of a list of numbers, following the provided pseudocode step-by-step.

## Requirements


* Python 3.8 or later
* Python requests library (for Weather CLI)

  ```bash
  pip install requests
  ```

* OpenWeather API Key (for Weather CLI)

  Obtain one at: https://openweathermap.org/api

  Set the API key as an environment variable named:

  OPENWEATHER_API_KEY

  ### Examples

   * Linux / macOS:

     
    ```bash
    export OPENWEATHER_API_KEY="your_api_key_here"
    ```

   * Windows PowerShell:

    ```powershell
    $env:OPENWEATHER_API_KEY = "your_api_key_here"
    ```

## Project Structure

```bash
RDB-HUB-coding-Activity/
├── weather_app.py         # Weather CLI application (Activity 1)
├── median_calculator.py   # Sorting + median calculator (Activity 2)
└── README.md              # This documentation
└── README.md              # Text file containing python library dependencies
```

## Weather CLI App

A command-line weather program that:
* Looks up the current weather for any city.
* Allows you to add up to 3 favourite cities.
* Lets you list favourites along with their current weather.
* Lets you remove or update favourites.
* Uses the OpenWeather Current Weather API.

### Features Implemented

* API integration with error handling (network errors, API errors, invalid JSON).
* Environment-based API key loading.
* Clean menu-driven interface.
* Readable output formatting (temperature, humidity, wind, description).
* Safe input handling for all user actions.
* All favourites stored in memory, as required.

### Running the Weather App

```python
python weather_app.py
```

You will see:

```bash
==== Weather CLI ====
1. Search weather for a city
2. Add a city to favourites (max 3)
3. List favourite cities with weather
4. Update favourites (remove/add)
5. Exit
```

Example Output: 

```
Enter city name: London
City: London
  Description : light rain
  Temperature : 12.4 °C (feels like 10.3 °C)
  Humidity    : 87%
  Wind Speed  : 5.2 m/s
```

## Median Calculator

A program that:
* Implements selection sort manually.
* Sorts the user-provided list in place.
* Computes the median using the required pseudocode:
    * Odd count → return middle value
    * Even count → average the two middle values
* Provides a simple and clear CLI.

### Features Implemented

* Custom sorting algorithm (selection sort).
* Safe handling of:
    * Empty input
    * Invalid input
    * Float or integer numbers
* Fully documented functions with explanations of the algorithm.

### Running the Median Calculator

```python
python median_calculator.py
```

Example Output:

```bash
Median Calculator (using a custom sorting function)
Type numbers separated by spaces, for example: 10 2 5 7 1
Numbers: 10 2 5 7 1
Sorted numbers: [1.0, 2.0, 5.0, 7.0, 10.0]
Median: 5.0
```

## Notes

* Both programs are self-contained and require no external files or databases.
* The code is intentionally written to be clear, readable, and beginner-friendly.
* All logic strictly follows the assessment’s specifications, including:
    * A manually implemented sorting algorithm.
    * A median function that matches pseudocode.
    * A menu-based weather application with favourite-city limits (using Canadian spelling just for fun)
