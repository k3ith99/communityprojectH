import React from "react";
import { NavLink, Outlet } from 'react-router-dom'

function Header(){ 

    return <>
        <h1>Header</h1>
        
        <div id='navbar'>
            <NavLink className='nav-link' to='index'>Home</NavLink>
            <NavLink className='nav-link' to='about'>About</NavLink>
            <NavLink className='nav-link' to=''>Destination</NavLink>
            <NavLink className='nav-link' to=''>Blogs</NavLink>
            <NavLink className='nav-link' to=''>Search</NavLink>
            <NavLink className='nav-link' to=''>Login</NavLink>
        </div>
        <Outlet />
    </>
}

export default Header;