import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import Layout from'../LayoutTemplate/Layout';


const LoginPage = () => {
  const [username_or_email, setUserNameOrEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          username_or_email: username_or_email,
          password: password,
        }),
      });

      if (response.ok) {
        navigate("/");
      } else {
        alert("Login Failed")
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };


  return (
    <Layout>
        <div className="create-account-container">
          <h2>Login</h2>
          <form className="create-account-form" onSubmit={handleSubmit}>
          <input className="form-input" type="text" name="username_or_email" placeholder="Username or Email" required onChange = {(e) =>{setUserNameOrEmail(e.target.value)}} ></input>
          <input className="form-input" type="password" name="password" placeholder="Password" required onChange = {(e) =>{setPassword(e.target.value)}}></input>
          <button className="create-account-button" type="submit">Login</button>
          </form>
        </div>
    </Layout>
  );
};

export default LoginPage;