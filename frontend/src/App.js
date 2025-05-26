import './App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import map from "./images/mcmaster-parking-map.pdf"
import bus_icon from "./images/bus-icon.png"
import schedule from "./images/shuttle-schedule.png"

function App() {
  const [busLocations, setBusLocations] = useState([]);

  useEffect(() => {
    async function getData() {
      const data = await fetchBusLocations();
      setBusLocations(data);
    }

    getData();
    const interval = setInterval(getData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-white text-gray-900 font-sans">
      {/* Header */}
      <header className="bg-[#7A003C] text-white py-6 shadow-md">
        <h1 className="text-4xl font-bold text-center">McMaster Parking Shuttle Buses</h1>
      </header>

      <main className="p-6">
        {/* Map Image */}
        <div className="mb-8 flex justify-center">
          <img src={map} alt="McMaster Parking Map" width="800" height="600" className="rounded shadow-lg" />
        </div>

        {/* Shuttle Count */}
        <div className="mb-6 text-center">
          <h2 className="text-2xl font-semibold">
            Active Shuttles: {busLocations.filter(bus => bus.isRunning).length}
          </h2>
        </div>

        {/* Shuttle Cards */}
        <div className="flex gap-4 overflow-x-auto flex-nowrap scrollbar-hide snap-x snap-mandatory px-1 pb-4">
          {busLocations.map((bus, index) => (
            <div key={index} className="min-w-[300px] bg-white border border-gray-200 rounded-xl shadow-md p-4 shrink-0 snap-start">
              <img src={bus_icon} alt="Bus Icon" width="150" height="85" className="mx-auto mb-4" />
              <p><strong>Currently:</strong> {bus.nearest_stop ? `At ${bus.nearest_stop}` : `En route to ${bus.next_stop}`}</p>
              <p><strong>ETA:</strong> {bus.eta} minute(s) to {bus.next_stop}</p>
              <p><strong>Last Updated:</strong> {new Date(bus.time_stamp).toLocaleTimeString()}</p> {/*toLocaleTimeString converts the universal time to the local timezone */}
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;
