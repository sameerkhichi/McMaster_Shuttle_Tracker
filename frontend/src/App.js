import './App.css';
import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/bus-locations")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching data:", error));  
  }, []);

  return (
    <div>
      <h1>Parking Services Shuttle Tracker</h1>
      <h2>Bus Locations</h2>
      <ul>
        {data.map((bus, index) =>(
          <li key={index}>
            Bus {bus.bus_id}: {bus.lat}, {bus.lon} at {bus.timestamp}
          </li>
        ))}  
      </ul>
    </div>
  );
}

export default App;
