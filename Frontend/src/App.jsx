import React from 'react'
import { Routes, Route } from "react-router-dom"

// components
import { Header, Itinerary } from './components'

// pages
import { About, Home, Destinations, Blog, Login, Register } from './Pages/index'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<Header />} >
          <Route path='/about' element={<About />} ></Route>
          <Route path='/destinations' element={<Destinations />} ></Route>
          <Route path='/blog' element={<Blog />} ></Route>
          <Route path='/login' element={<Login />} ></Route>

          <Route path="/itinerary" element={<Itinerary />} ></Route>
          
          <Route path="*" element={<h1>404 Error</h1>} ></Route>
          <Route index element={<Home />} ></Route>
        </Route>
      </Routes>
    </>
  )
}

export default App
