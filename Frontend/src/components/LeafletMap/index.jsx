import React from "react";
// import { Map, TileLayer, Marker, Popup } from 'react-leaflet';

function LeafletMap() {
    // const position = [this.state.location.lat, this.state.location.lng];
    
    // state = {
    //     lat: 51.505,
    //     lng: -0.09,
    //     zoom: 13,
    // }

    return (<>
    <h1>Map</h1>
        {/* <Map className="map" center={position} zoom={this.state.zoom}>
        <TileLayer
            attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors and Chat location by Iconika from the Noun Project"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Marker position={[position]}>
              <Popup>
                Test pop up
              </Popup>
            </Marker>
        </Map> */}
        
    </>)
}

export default LeafletMap;