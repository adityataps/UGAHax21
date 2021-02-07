import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Dashboard from "../dashboard/Dashboard";
import Preferences from "../preferences/Preferences"
import Login from "../login/Login";


function App() {

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
