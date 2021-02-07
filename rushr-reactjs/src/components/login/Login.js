import React, { useState } from 'react'
import './Login.css'
// import homeBgr from '../assets/homeBgr.jpg'
import Sidebar from './Sidebar'
import Left from './Left'

const Login = () => {
    return(
        <div className={"page-wrapper"}>
            <div className={"background-image"}>
                <Left />
                <Sidebar />
            </div>
        </div>
    )
}

export default Login;