import './App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import map from "./images/mcmaster-parking-map.pdf"
import schedule from "./images/shuttle-schedule.png"
import ShuttleCard from './components/ShuttleCard';

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
          {busLocations.map((bus) => (
            bus.isRunning && (
              <ShuttleCard bus={bus} key={bus.bus_id} />
            )
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;
