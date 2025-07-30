//this file serves as the api calls the front end will make to the backend

//the empty string forces the client to use the origin URL
const API_URL = ""; 

//getting the bus locations from flask
export async function fetchBusLocations(){
    try{
        const response = await fetch(`/update`, {
            method: "GET", //ensuring the right request type is being used
            headers: {
                "Content-Type": "application/json"
            }
        });
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return await response.json();
    }
    catch(error){
        console.error("Error fetching bus locations: ", error);
        return[];
    }
}
