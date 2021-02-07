import React from 'react';
import './Dashboard.css'
import ChartTable from "./ChartTable";
import Button from 'react-bootstrap/Button'
import Form from "react-bootstrap/Form";

const Dashboard = () => {
    return (
        <div className={"dash-page-wrapper"}>

            <div className={"banner"}>
                <div className={"welcome-text"} style={{"margin-top": "48px", "margin-left": "5%"}}>
                    Welcome to your dashboard.
                </div>
                <Button size="lg" variant={"danger"} type="submit" href={"/"} className={"sign-out-button"}>
                    Log out
                </Button>
            </div>


            <div>
                <ChartTable />
            </div>


        </div>
    )
}

export default Dashboard
