import './App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import map from "./images/mcmaster-parking-map.pdf"


function App() {
  const [busLocations, setBusLocations] = useState([]);

  useEffect(() => {
      async function getData() {
          const data = await fetchBusLocations(); //get the bus locations as a json response
          setBusLocations(data);
      }

      getData();
      const interval = setInterval(getData, 30000); //refresh data every 30 seconds

      return () => clearInterval(interval); //clearing the interval to reset timer
  }, []);


  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">McMaster Parking Shuttle Buses</h1>

      <div className="mb-6">
        <img src={map} alt="Map" width="800" height="600" />
      </div>

      <div className="mb-4">
        <h2 className="text-xl font-semibold">Active Shuttles: {busLocations.length}</h2>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {busLocations.map((bus, index) => (
          <div key={index} className="rounded-xl shadow-md p-4 border">
            <h3 className="text-lg font-semibold mb-2">Bus ID: {bus.bus_id}</h3>
            {/*if the nearest_stop field is none or empty, its travelling to the next stop*/}
            <p><strong>Stop:</strong> {bus.nearest_stop ?? `En route to ${bus.next_stop}`}</p>
            <p><strong>Next Stop:</strong> {bus.next_stop}</p>
            <p><strong>ETA:</strong> {bus.eta} minute(s)</p>
            <p><strong>Last Updated:</strong> {new Date(bus.time_stamp).toLocaleTimeString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;