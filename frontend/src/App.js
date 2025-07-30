import './css/App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import { Routes,Route,Link,useLocation } from 'react-router-dom'
import logo from './images/mcmaster-logo.png'
import Home from './pages/Home'
import BusStopETAList from './pages/BusStopETAList';

function App() {
  const [busLocations, setBusLocations] = useState([]);
  const location = useLocation();
  const isHome = location.pathname === "/";

  useEffect(() => {
    async function getData() {
      const data = await fetchBusLocations();
      console.log("Fetched bus locations:", data); // Temp
      setBusLocations(data);
    }

    getData();
    const interval = setInterval(getData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-white text-gray-900 font-sans pb-16">
      {/* Header */}
      <header className="bg-[#7A003C] text-white py-6 shadow-md px-5">
        <div className="flex items-center gap-10 relative">
          <img 
            src={logo} 
            alt="McMaster Logo"
            className="w-20 pb-4"
          />
          <h1 className="text-2xl font-bold sm:absolute sm:top-1/2 sm:left-1/2 sm:-translate-x-1/2 sm:-translate-y-1/2">McMaster Parking Shuttle Buses</h1>
        </div>
      </header>

      <Routes>
        <Route path="/" element={<Home busLocations={busLocations} />} />
        <Route path="/times" element={<BusStopETAList busLocations={busLocations}/>} />
      </Routes>

      <nav className="bg-white fixed bottom-0 left-0 right-0 border-t border-gray-300 flex h-16 z-50 font-semibold">
        <Link to="/" className="w-1/2 flex items-center justify-center border-r" style={{ backgroundColor: isHome ? "#7A003C" : "white", color: isHome ? "white" : "black"}} >Home</Link>
        <Link to="/times" className="w-1/2 flex items-center justify-center border-l" style={{ backgroundColor: isHome ? "white" : "#7A003C", color: isHome ? "black" : "white"}}>Times</Link>
      </nav>
    </div>
  );
}

export default App;
