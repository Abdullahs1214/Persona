import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
//import './LoginForm.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function LoginForm() {
    const [email, setEmail] = useState("");
    const [pwdattempt, setPwdattempt] = useState("");

    const handleChangeEmail = (event) => {
        event.preventDefault();
        setEmail(event.target.value);
    }

    const handleChangePassword = (event) => {
        event.preventDefault();
        setPwdattempt(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
    }
      
    return(
    <div className = "container">
        <div className = "row justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
            <div className = "col-sm-4">
                <div className='LoginInterface text-center' onSubmit={handleSubmit}>
                    <form>
                        <label className='Form'>
                            <input placeholder = "Email" name="emailform" type="email" value={email} onChange={handleChangeEmail} size={15}></input>
                        </label>

                        <label className='Form'>
                            <input placeholder = "Password" name="passwordform" type="password" value={pwdattempt} onChange={handleChangePassword} size={15}></input>
                        </label>
                    <div className = 'Form'>
                        <input type='submit' value="Login"/>
                    </div>
                    </form>
                </div>
            </div>
        </div>
    </div>);
}

export default LoginForm;
