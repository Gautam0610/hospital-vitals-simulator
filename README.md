# Hospital Vitals Simulator

This project simulates hospital patient vitals and sends them to a Kafka broker. It includes a fault injector to simulate realistic scenarios like missing data, delays, and out-of-order timestamps.

## Functionality

-   **Vitals Generation:** Simulates vitals for multiple patients, including heart rate, blood pressure, temperature, and oxygen saturation.
-   **Kafka Integration:** Sends the generated vitals to a Kafka broker.
-   **Fault Injection:** Introduces realistic faults into the data stream, such as missing fields, delays, and out-of-order timestamps.

## Files

-   `main.py`: Main script for running the simulation and sending data to Kafka.
-   `fault_injector.py`: Implements the fault injection logic.
-   `Dockerfile`: Used for containerizing the application with Docker.
-   `requirements.txt`: Lists the Python dependencies.

## Usage

1.  **Prerequisites:**
    -   Kafka broker running and accessible.
    -   Python 3.6+

2.  **Installation:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    -   Set the `KAFKA_BROKER` and `KAFKA_TOPIC` environment variables to configure the Kafka connection.
    -   Set the `NUM_PATIENTS` environment variable to configure the number of patients to simulate.

4.  **Run the simulator:**
    ```bash
    python main.py
    ```

## Docker

A `Dockerfile` is included for easy containerization. To build and run the Docker image:

```bash
 docker build -t hospital-vitals-simulator .
 docker run -e KAFKA_BROKER=<kafka_broker_address> -e KAFKA_TOPIC=<kafka_topic> hospital-vitals-simulator
```