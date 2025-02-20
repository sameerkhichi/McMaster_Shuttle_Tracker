//this file serves as the api calls the front end will make to the backend

//this is supposed to change when deploying to the actual url
const API_URL = "http://127.0.0.1:5000"; //USE HTTP NOT HTTPS OTHERWISE IT WILL LITERALLY EXPLODE

//getting the bus locations from flask
export async function fetchBusLocations(){
    try{
        const response = await fetch(`${API_URL}/bus-locations`, {
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
