# Weather Application

This project is a simple weather application built using Python's Tkinter library for the GUI, along with various other libraries such as `geopy` for location services, `timezonefinder` and `pytz` for time zone management, and `requests` for fetching weather data from the OpenWeatherMap API.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Functions](#functions)
  - [get_weather_data(lat, lng)](#get_weather_datalat-lng)
  - [get_coordinates(location)](#get_coordinateslocation)
  - [get_local_time(latitude, longitude)](#get_local_timelatitude-longitude)
  - [show_data()](#show_data)
- [License](#license)

## Requirements

To run this project, you need the following Python libraries:

- `tkinter`
- `geopy`
- `requests`
- `timezonefinder`
- `pytz`

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment using the following command:

    ```bash
    python -m venv myenv
    ```

3. Activate the virtual environment:

    - On Windows:
    
        ```bash
        myenv\Scripts\activate
        ```

    - On macOS and Linux:
    
        ```bash
        source myenv/bin/activate
        ```

4. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install the required libraries individually:

    ```bash
    pip install geopy requests timezonefinder pytz
    ```

5. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'enter_api'` in the `weather_app.py` file with your API key.

## Usage

1. Place `logo.png` and `box.png` in the same directory as the `weather_app.py` script.
2. Run the `weather_app.py` script:

    ```bash
    python weather_app.py
    ```

3. Enter the desired location in the text box and click on "Results". The application will display the local time, temperature, humidity, precipitation probability, and wind speed for the entered location.

## File Structure

- `weather_app.py`: The main script containing the weather application logic.
- `logo.png`: An image file used as a logo in the application.
- `box.png`: An image file used as a background in the application.
- `requirements.txt`: A file listing the required Python libraries.
- `myenv/`: The virtual environment directory containing the installed dependencies.

## Functions

### `get_weather_data(lat, lng)`

This function fetches weather data from the OpenWeatherMap API using the provided latitude and longitude. It returns the temperature, humidity, precipitation probability, and wind speed.

### `get_coordinates(location)`

This function converts a location name into its corresponding latitude and longitude using the `geopy` library.

### `get_local_time(latitude, longitude)`

This function calculates the local time of the given latitude and longitude using the `timezonefinder` and `pytz` libraries.

### `show_data()`

This function retrieves the location from the user input, fetches the corresponding weather data and local time, and displays the results in the application.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
