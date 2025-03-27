IoT Environmental Data Collection and Visualization

This project demonstrates the development of an IoT system that simulates environmental sensor data, publishes it to ThingSpeak using MQTT, and visualizes the collected data. The system generates randomized values for temperature, humidity, and CO₂ levels, mimicking real-world environmental readings.

## Features

- **Sensor Data Simulation:** Generates realistic environmental data for temperature (°C), humidity (%), and CO₂ levels (ppm).
- **MQTT Publishing:** Transmits simulated sensor data to a ThingSpeak channel using the MQTT protocol.
- **Data Visualization:** Retrieves and plots the collected data from ThingSpeak for analysis.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `paho-mqtt`
  - `requests`
  - `pandas`
  - `matplotlib`

## Setup and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Required Libraries:**

   ```bash
   pip install paho-mqtt requests pandas matplotlib
   ```

3. **Configure ThingSpeak Credentials:**

   - Replace the placeholder values in the scripts with your actual ThingSpeak `CHANNEL_ID`, `MQTT_CLIENT_ID`, `MQTT_USERNAME`, and `MQTT_PASSWORD`.

4. **Simulate and Publish Sensor Data:**

   - Run the `publish_data.py` script to start generating and publishing sensor data to ThingSpeak.

     ```bash
     python publish_data.py
     ```

5. **Visualize the Data:**

   - Execute the `plot_data.py` script to retrieve and plot the data from ThingSpeak.

     ```bash
     python plot_data.py
     ```

## File Structure

- `publish_data.py`: Simulates sensor data and publishes it to ThingSpeak via MQTT.
- `plot_data.py`: Fetches data from ThingSpeak and plots it for visualization.

## Notes

- Ensure your ThingSpeak channel is properly set up to receive and display the data.
- Adjust the data publishing interval in `publish_data.py` as per your requirements and ThingSpeak's rate limits.
- Modify the time range in `plot_data.py` to focus on specific periods of interest.

## References

- [ThingSpeak MQTT Publishing](https://www.mathworks.com/help/thingspeak/publishtoachannelfeeds.html)
- [ThingSpeak Data Retrieval API](https://www.mathworks.com/help/thingspeak/readdata.html)

---

*This project serves as a foundational example for IoT data simulation, transmission, and visualization using Python and ThingSpeak.* # IoTAssignment3
IoT Assignment 3 
