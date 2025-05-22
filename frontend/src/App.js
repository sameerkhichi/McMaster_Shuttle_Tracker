import './App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import map from "./images/mcmaster-parking-map.pdf"
import bus_icon from "./images/bus-icon.png"


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

      <div className="flex gap-4 overflow-x-auto flex-nowrap scrollbar-hide snap-x snap-mandatory px-1">
        {busLocations.map((bus, index) => (
          <div key={index} className="min-w-[300px] rounded-xl shadow-md p-4 border shrink-0 snap-start">
            <img src={bus_icon} alt="icon" width="150" height="85"/>
            {/*if the nearest_stop field is none or empty, its travelling to the next stop*/}
            <p><strong>Currently:</strong> {bus.nearest_stop ? `At ${bus.nearest_stop}` : `En route to ${bus.next_stop}`}</p>
            <p><strong>ETA:</strong> {bus.eta} minute(s) to {bus.next_stop}</p>
            <p><strong>Last Updated:</strong> {new Date(bus.time_stamp).toLocaleTimeString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;