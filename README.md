# Light Intensity Anomaly Detector(LIAD)

## Introduction
This project is designed to analyze intensity anomalies, integrate Twilio SMS notifications, and compute Z-factor values based on sensor data. The system is built using Python, with various modules handling anomaly detection, device configuration, and communication.

## Features
- **Intensity Anomaly Detection**: Identifies and analyzes deviations in intensity values.
- **Twilio SMS Alerts**: Sends real-time notifications using Twilio API.
- **Z-Factor Calculation**: Computes Z-factor values based on predefined formulae.
- **Device Configuration**: Customizable settings for the device parameters.
- **Component Management**: Tracks and lists all hardware components involved.

## Components Used
The system consists of the following key hardware and software components:

- Sensors for measuring intensity variations.
- Microcontroller for data processing.
- Communication modules for SMS alerts.
- Software algorithms for anomaly detection and factor calculations.

*(Refer to `List of Components used.png` for a detailed breakdown.)*

## Intensity Anomaly Detection
The script `intensity_anomaly.py` contains logic to monitor and analyze changes in intensity values, triggering alerts when anomalies are detected.

## Twilio SMS Integration
Twilio is used to send SMS notifications when specific conditions are met.

*(Refer to `Sms Twilio.jpeg` for configuration details.)*

## Z-Factor Calculation
The Z-factor calculation formulae are used to determine statistical values that help in data analysis.

*(Refer to `Z factor Calculation Formulae.png` for detailed mathematical equations.)*

## Configuration
The `conf.py` script contains configuration settings for the system, including thresholds, API keys, and device parameters.

## Installation and Usage
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `intensity_anomaly.py` to start monitoring.
4. Ensure Twilio API keys are configured in `conf.py` for SMS alerts.

## License
This project is licensed under [Your License].

## Contact
For any issues or contributions, feel free to reach out!
