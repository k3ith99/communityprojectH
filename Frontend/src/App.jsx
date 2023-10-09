import React from 'react'
import { Routes, Route } from "react-router-dom"

import { Itinerary } from './components'

function App() {

  return (
    <>
      <h1>Welcome</h1>

      <Routes>
        <Route path="/" element={<Itinerary />} ></Route>
      </Routes>
    </>
  )
}

export default App
