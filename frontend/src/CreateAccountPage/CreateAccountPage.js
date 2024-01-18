import React, { useState, useEffect } from 'react';
import Layout from '../LayoutTemplate/Layout';
import './CreateAccountPage.css';
import { useNavigate } from "react-router-dom";

const CreateAccountPage = () => {
  const navigate = useNavigate();
  const [information, setInformation] = useState('')
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    repeatPassword: '',
  });
  
  useEffect(() => {
    setInformation(formData.password === formData.repeatPassword ? '' : 'Passwords do not match')
  }, [formData.repeatPassword,formData.password]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    if(formData.password !== formData.repeatPassword){
      setInformation('Passwords do not match.')
      return;
    };

    try {
      const response = await fetch('/create_account', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Response:', data);
        navigate('/')
      } else if(response.status === 404){
        setInformation('Could not communicate with server');
      }
      else if(response.status === 400){
        const data = await response.json();
        setInformation(data.errorMessage);
      }
      else{
        setInformation('Unknown Error')
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <Layout>
        <div className="create-account-container">
          <h2>Account Registration</h2>
          <form className="create-account-form" onSubmit={handleSubmit}>
          <input className="form-input" type="text" name="username" placeholder="Username" required onChange={ (e) => setFormData({...formData,username:e.target.value})}></input>
          <input className="form-input" type="text" name="email" placeholder="Email" required onChange={ (e) => setFormData({...formData,email:e.target.value})}></input>
          <input className="form-input" type="password" name="password" placeholder="Password" required onChange={ (e) => setFormData({...formData,password:e.target.value})}></input>
          <input className="form-input" type="password" name="repeatPassword" placeholder="Repeat password" required onChange={(e) => setFormData({...formData,repeatPassword:e.target.value})}></input>
          {information === '' ? (<p></p>) : (<p>{information}</p>)}
          <button className="create-account-button" type="submit">Register Account</button>
          </form>
        </div>
    </Layout>
  );
};

export default CreateAccountPage;