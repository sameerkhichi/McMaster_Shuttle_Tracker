# 🚌 McMaster Shuttle Bus Tracker

A real-time web app to track McMaster University's shuttle buses, providing accurate ETAs and stop prediction using GPS location data and smart logic to handle skipped or missed stops.

## 🔧 Tech Stack

- **Python** (Flask) – Backend service to process GPS data and calculate ETAs
- **MySQL** – Stores location and status information
- **JavaScript/HTML/CSS** – Frontend for displaying shuttle info
- **OwnTracks** – GPS tracking from drivers devices
- **Custom Routing Logic** – Detects skipped stops, estimates speed-based arrival times, and corrects stop sequences

## 💡 Features

- Detects skipped stops based on position and time
- Calculates live ETAs using GPS and distance logic
- Automatically corrects stop order inconsistencies
- Tracks whether buses are actively running for simplicity

Currently the repository is open for view