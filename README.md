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
.
├── weather_app.py         # Weather CLI application (Activity 1)
├── median_calculator.py   # Sorting + median calculator (Activity 2)
└── README.md              # This documentation
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


