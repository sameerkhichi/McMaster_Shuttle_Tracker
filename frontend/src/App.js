import './css/App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import { Routes,Route,Link } from 'react-router-dom'
import Home from './pages/Home'
import BusStopETAList from './pages/BusStopETAList';

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
    <div className="min-h-screen bg-white text-gray-900 font-sans pb-16">
      {/* Header */}
      <header className="bg-[#7A003C] text-white py-6 shadow-md">
        <h1 className="text-4xl font-bold text-center">McMaster Parking Shuttle Buses</h1>
      </header>

      <Routes>
        <Route path="/" element={<Home busLocations={busLocations} />} />
        <Route path="/times" element={<BusStopETAList />} />
      </Routes>

      <nav className="bg-white fixed bottom-0 left-0 right-0 border-t border-gray-300 shadow-md flex h-16 z-50">
        <Link to="/" className="w-1/2 flex items-center justify-center border-r">Home</Link>
        <Link to="/times" className="w-1/2 flex items-center justify-center border-l">Times</Link>
      </nav>
    </div>
  );
}

export default App;
