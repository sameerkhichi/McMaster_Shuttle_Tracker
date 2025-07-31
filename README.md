# 🚌 McMaster Shuttle Bus Tracker

A real-time web app to track McMaster University's shuttle buses, providing accurate ETAs and stop prediction using GPS location data and smart logic to handle skipped or missed stops.

## 🔧 Tech Stack/Information

- **Python** (Flask) – Backend service to process GPS data and calculate ETAs
- **WGSI** – The Flask web app is hosted and run as a WGSI server using gunicorn in production
- **MySQL** – Stores location and status information
- **JavaScript/HTML/CSS** – Frontend for displaying shuttle info
- **OwnTracks** – GPS tracking from drivers devices
- **Render** - Currently the app is hosted on Render.
- **Custom Routing Logic** – Detects skipped stops, estimates speed-based arrival times, and corrects stop sequences when deviating from route schedule

## 💡 Features

- Detects skipped stops based on position and time
- Calculates live ETAs using GPS and distance logic
- Automatically corrects stop order inconsistencies
- Tracks whether buses are actively running for simplicity

Currently the repository is open for view