import React from 'react'
import './Sidebar.css'
import rushrLogo from '../assets/images/rushrLogo.png'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import ncrBranding from '../assets/images/ncrBranding.png'

const Sidebar = () => {
    return(
        <div className={"sidebar-wrapper"}>
            <div className={"rushr-logo"}>
                <img src={rushrLogo}
                     alt={"rushr"}
                     style={{width: "50%", height: "50%"}} />
            </div>
            <div className={"credentials-form"} style={{"margin-top": "10%"}}>
                <Form>
                    <Form.Group controlId="formEmail">
                        <Form.Control size="lg" type="email" placeholder="Email" />
                    </Form.Group>
                    <Form.Group controlId="formPassword">
                        <Form.Control size="lg" type="password" placeholder="Password" style={{"margin-top": "25px"}} />
                    </Form.Group>
                    <div style={{"text-align": "right"}}>
                        <Form.Label style={{"font-size": "15px", "font-weight": "bold", color: "#66C15D"}}>
                            Forgot your password?
                        </Form.Label>
                    </div>
                    <br/>
                    <Button size="lg" variant="success" type="submit" style={{"width": "50%"}} href={"/dashboard"}>
                        Sign in
                    </Button>
                </Form>
            </div>
            <div className={"new-acct"}>
                New to rushr? <b style={{"color": "#66C15D"}}> Create an account </b>
            </div>
            <div style={{"text-align": "center"}}>
            <img src={ncrBranding}
                 alt={""}
                 style={{"width": "20%", "height": "auto", "margin-top": "10%"}}
                 />
            </div>
        </div>
    )
}

export default Sidebar