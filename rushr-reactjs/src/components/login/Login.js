import React, { useState } from 'react'
import './Login.css'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default function Login() {

    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const [error, setError] = useState(null)
    // const signInWithEmailAndPasswordHandler = (event, email, password) => {
    //     event.preventDefault()
    // }

    return (
        <div className={"login-wrapper"}>
            <Jumbotron>
                <h3 className={"bold"}>
                    Please log in.
                </h3>

                <Form>
                    <Form.Group controlId={"loginEmail"}>
                        <Form.Label> Email address </Form.Label>
                        <Form.Control type={"email"} placeholder={"Enter email"} onChange={e => setEmail(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId={"loginPassword"}>
                        <Form.Label> Password </Form.Label>
                        <Form.Control type={"password"} placeholder={"Password"} onChange={e => setPassword(e.target.value)} />
                    </Form.Group>

                    <Button variant={"primary"} type={"submit"} href={"/dashboard"}>
                        Login
                    </Button>
                </Form>
            </Jumbotron>
        </div>
    )
}