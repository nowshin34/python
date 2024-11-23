import requests  # To make API requests

# Function to get weather data
def get_weather(city, api_key):
    # API URL with the city name and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send a request to the API
        response = requests.get(url)
        data = response.json()  # Convert response to JSON format

        # Check if the city is found
        if response.status_code == 200:
            # Extract weather details
            city_name = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Print weather details
            print("\nWeather Information:")
            print("-------------------")
            print(f"City: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Weather: {description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print("-------------------")
        else:
            # If the city is not found, print an error message
            print(f"Error: {data['message'].capitalize()}")
    except Exception as e:
        # Handle other unexpected errors
        print("An error occurred:", e)

# Main function to run the program
def main():
    print("Welcome to the Simple Weather App!")
    print("----------------------------------")
    
    
    api_key = "c70e2f0c3349d0ccae4e167a3ba96ebf"
    
    # Ask the user for input
    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == 'exit':
            # Exit the program if the user types 'exit'
            print("Thank you for using the Weather App. Goodbye!")
            break
        elif city:
            # Call the weather function if the city is valid
            get_weather(city, api_key)
        else:
            print("Please enter a valid city name.")

# Run the program
if __name__ == "__main__":
    main()
