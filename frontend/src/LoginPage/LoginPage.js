// Login.js
import React, { useState } from 'react';
import Layout from'../LayoutTemplate/Layout';


const LoginPage = () => {
  const [usernameOrEmail, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          usernameOrEmail: usernameOrEmail,
          password: password,
        }),
      });

      if (response.ok) {
        window.location.href = '/dashboard';
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
          <input className="form-input" type="text" name="usernameOrEmail" placeholder="Username or Email" required ></input>
          <input className="form-input" type="password" name="password" placeholder="Password" required></input>
          <button className="create-account-button" type="submit">Login</button>
          </form>
        </div>
    </Layout>
  );
};

export default LoginPage;