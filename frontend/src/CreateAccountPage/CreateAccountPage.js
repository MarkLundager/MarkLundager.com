import React, { useState } from 'react';
import Layout from '../LayoutTemplate/Layout';
import './CreateAccountPage.css';

const CreateAccountPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
  };

  return (
    <Layout>
      <body>
        <div class ="create-account-container">
          <h2>Account Registration</h2>
          <form class="create-account-form">
          <input class="form-input" type="text" name="username" placeholder="Username" required></input>
          <input class="form-input" type="password" name="password" placeholder="Password" required></input>
          <button class="create-account-button" type="submit">Register Account</button>
          </form>
        </div>
      </body>
    </Layout>
  );
};

export default CreateAccountPage;