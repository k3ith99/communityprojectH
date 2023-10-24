import React, { useState } from "react";

function Itinerary(props){

    const [travelTo, setTravelTo] = useState('')
    const [travelFrom, setTravelFrom] = useState('')
    const [leaveDate, setLeaveDate] = useState('')
    const [returnDate, setReturnDate] = useState('')
    const [people, setPeople] = useState(1)
    const [toNote, setToNote] = useState('')

    async function submitItinerary(e){
        e.preventDefault();
        const data = { travelTo: travelTo, travelFrom: travelFrom, leaveDate: leaveDate, returnDate: returnDate, people: people, toNote: toNote }

        // console.log(data)

        await fetchSubmitItinerary(data)
    }

    async function fetchSubmitItinerary(data){
        try {
            // replace url with the launched server one
            const url = 'http://127.0.0.1:5000'

            return await fetch(`${url}/itinerary_form`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            }).then(resp => resp.json())
        } catch(err){
            console.log(err)
            return err
        }
    }

    return <>
        <h2>Itinerary</h2>

        <form onSubmit={submitItinerary}>
            <label htmlFor="travel-to">Choose a UK destination or random: </label>
            <input type="text" id="travel-to" name="travel-to" onChange={e => setTravelTo(e.target.value)} />
        
            <label htmlFor="travel-from">Traveling from: </label>
            <input type="text" id="travel-from" name="travel-from" onChange={e => setTravelFrom(e.target.value)} />

            <label htmlFor="leave-date">Leave Date: </label>
            <input type="date" id="leave-date" name="leave-date" onChange={e => setLeaveDate(e.target.value)} />

            <label htmlFor="return-date">Return Date: </label>
            <input type="date" id="return-date" name="return-date" onChange={e => setReturnDate(e.target.value)} />

            <label htmlFor="people">People: </label>
            <input type="number" id="people" name="people" value={people} onChange={e => setPeople(e.target.value)} />

            <label htmlFor="things-to-note">Important things to note: </label>
            <input type="text" id="things-to-note" name="things-to-note"
                placeholder="I love to visit cultural sites."
                onChange={e => setToNote(e.target.value)} />

            <button type="submit">Submit</button>
        </form>
    </>
}

export default Itinerary;