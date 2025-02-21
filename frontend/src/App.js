import './App.css';
import React, {useEffect, useState} from "react";
import { fetchBusLocations } from './api';

function App(){
  const [busLocations, setBusLocations] = useState([]);

  useEffect(() => {
      async function getData(){
          const data = await fetchBusLocations();
          setBusLocations(data);
      }
      getData();
  }, []);

  //this will return bus locations if there are any in the database - otherwise no locations available
  //does this with an advanced if-else statement basically
  return (
      <div>
          <h1>Bus Locations</h1>
          {busLocations.length > 0 ? (
              <ul>
                  {busLocations.map((bus, index) => (
                      <li key={index}>
                          <strong>Bus {bus.bus_id}:</strong> {bus.lat}, {bus.lon} (Updated: {bus.time_stamp})
                      </li>
                  ))}
              </ul>
          ) : (
              <p>No bus location data available.</p>
          )}
      </div>
  );
}

export default App;
