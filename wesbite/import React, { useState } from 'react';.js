import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
//import './LoginForm.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function LoginForm(props) {
    const [email, setEmail] = useState("");
    const [pwdattempt, setPwdattempt] = useState("");
    const [message, setMessage] = useState("");
    const [debug, setDebug] = useState();

    const handleChangeEmail = (event) => {
        event.preventDefault();
        setEmail(event.target.value);
    }

    const handleChangePassword = (event) => {
        event.preventDefault();
        setPwdattempt(event.target.value);
    }

    async function asasaas() {
        const l = await getDocs(collection(firestore, "Users"));
        l.forEach((doc) => {
            setDebug(`${doc.id} => ${doc.data()}`);
        })
        return l;
    }

    const handleSubmit = (event) => { //call this when you hit the button
        event.preventDefault();


        //const UserRef = collection(firestore, "Users");
        const result = asasaas();
        
        //setDebug(result);
        
        
    }
      
    return(
    //<div className = "container">
      //  <div className = "row justify-content-center align-items-center" style={{ minHeight: '100vh' }}>
        //    <div className = "col-sm-4">
                <div className='LoginInterface text-center' onSubmit={handleSubmit}>
                    <form>
                        <label className='Form'>
                            <input placeholder = "Email" name="emailform" type="email" value={email} onChange={handleChangeEmail} size={15}></input>
                        </label>

            <label className='Form'>
                <input placeholder = "Password" name="passwordform" type="password" value={pwdattempt} onChange={handleChangePassword} size={15}></input>
            </label>

            <input type='submit' value="Login" />
        </form>
        <p>
            {message}
        </p>
    </div>);
}

export default LoginForm;
