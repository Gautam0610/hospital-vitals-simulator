import os
import time
import json
import random
from kafka import KafkaProducer
from faker import Faker
import threading

# Kafka configuration
KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "vitals")

# Patient simulation configuration
NUM_PATIENTS = int(os.environ.get("NUM_PATIENTS", "10"))
VITAL_SIGNS = ["heart_rate", "blood_pressure", "temperature", "oxygen_saturation"]

fake = Faker()


def generate_vitals():
    return {
        "heart_rate": random.randint(60, 100),
        "blood_pressure": f"{random.randint(110, 140)}/{random.randint(70, 90)}",
        "temperature": round(random.uniform(36.5, 37.5), 1),
        "oxygen_saturation": random.randint(95, 100),
    }


def patient_simulator(patient_id, producer):
    while True:
        vitals = generate_vitals()
        vitals["patient_id"] = patient_id
        vitals["name"] = fake.name()
        vitals["timestamp"] = time.time()
        message = json.dumps(vitals).encode("utf-8")
        try:
            producer.send(KAFKA_TOPIC, message)
            print(f"Patient {patient_id}: Sent vitals: {vitals}")
        except Exception as e:
            print(f"Patient {patient_id}: Error sending vitals: {e}")
        time.sleep(random.uniform(0.5, 2))


def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

    threads = []
    for i in range(NUM_PATIENTS):
        thread = threading.Thread(target=patient_simulator, args=(i + 1, producer))
        threads.append(thread)
        thread.start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
        for thread in threads:
            thread.join()
        producer.close()

if __name__ == "__main__":
    main()