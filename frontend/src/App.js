import './App.css';
import React, { useEffect, useState } from "react";
import { fetchBusLocations } from './api';
import map from "./images/mcmaster-parking-map.pdf"


function App() {
  const [busLocations, setBusLocations] = useState([]);
  const [eta, setEta] = useState("Loading...");
  const [activeBusses, setAmount] = useState("Loading...");

  useEffect(() => {
      async function getData() {
          const data = await fetchBusLocations(); //get the bus locations as a json response
          setBusLocations(data);
          calculateETA(data);
          findRunningBusses(data);
      }

      getData();
      const interval = setInterval(getData, 15000); //refresh data every 15 seconds

      return () => clearInterval(interval);//clearing the interval to reset timer
  }, []);


function calculateETA(){
    //implement eta logic here
} 

function findRunningBusses(){
    //get the amount of busses that are running here
}


  return (
    <div>
        <h1>McMaster Parking Shuttle Busses</h1>

        <div>
            <img src={map} alt="Map" width="800" height="600"/>

        </div>

        <div>
            <p>Currently Active Shuttles: </p>

        </div>

        
        <div>
            <h2>ETA</h2>
        
        </div>


    </div>
  );
}

export default App;
