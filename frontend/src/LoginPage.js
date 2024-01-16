// Login.js
import React, { useState } from 'react';
import Layout from'./Layout';


const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    // Implement authentication logic, e.g., make API request to the server
    try {
      const response = await fetch('sign_in', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        // Handle successful login, e.g., redirect to another page
        window.location.href = '/dashboard';
      } else {
        // Handle unsuccessful login, show error message
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };


  return (
    <Layout></Layout>
  );
};

export default Login;