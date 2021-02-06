import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Dashboard from "../dashboard/Dashboard";
import Preferences from "../preferences/Preferences"
import Login from "../login/Login";


function App() {
    // const {token, setToken} = useState();

    // // if user has not logged in
    // if (!token) {
    //     return (
    //         <div className={"wrapper"}>
    //             <h1>rushr</h1>
    //             <h3>app made for UGAHacks 6</h3>
    //             <Login setToken={setToken} />
    //         </div>
    //     )
    // }

    // if user has logged in
    return (
        <div className={"wrapper"}>

            <BrowserRouter>
                <Switch>

                    <Route path={"/"} exact component={Login} />
                    <Route path={"/dashboard"} exact component={Dashboard} />
                    <Route path={"/preferences"} exact component={Preferences} />

                </Switch>
            </BrowserRouter>


        </div>
  );
}

export default App;
