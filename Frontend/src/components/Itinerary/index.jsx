import React from "react";

function Itinerary(props){

    function sendItinerary(){
        
    }

    return <>
        <h2>Itinerary</h2>

        <form>
            <label for="travel-to">Choose a UK destination or random: </label>
            <input type="text" id="travel-to" name="travel-to" />
        
            <label for="travel-from">Traveling from: </label>
            <label for="travel-from" id="travel-from" name="travel-from">Leaving Date: </label>

            <label for="start-date">End Date: </label>
            <input type="date" id="start-date" name="start-date" />

            <label for="end-date">End Date: </label>
            <input type="date" id="end-date" name="end-date" />

            <label for="people">People: </label>
            <input type="number" id="people" name="people" />

            <label for="things-to-note">Important things to note: </label>
            <input type="text" id="things-to-note" name="things-to-note" />
        </form>
    </>
}

export default Itinerary;