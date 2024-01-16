import React, { useState, useEffect } from 'react';
import Layout from '../LayoutTemplate/Layout';
import './CreateAccountPage.css';

const CreateAccountPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    repeatPassword: '',
    passwordError: '',
  });

  useEffect(() => {
    setFormData((prevdata) => {
      return {
        ...prevdata,
        passwordError:prevdata.password === prevdata.repeatPassword ? '' : 'Passwords do not match'
      };
    });
  }, [formData.repeatPassword,formData.password]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    if(formData.password !== formData.repeatPassword){
      alert("Registration failed, passwords do not match");
      return;
    };

    try {
      const response = await fetch('/create_account', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }),
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Response:', data);
      } else {
        const errorData = await response.json();
        console.error('Error:', errorData);
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
          {formData.passwordError && <p>{formData.passwordError}</p>}
          <button className="create-account-button" type="submit">Register Account</button>
          </form>
        </div>
    </Layout>
  );
};

export default CreateAccountPage;