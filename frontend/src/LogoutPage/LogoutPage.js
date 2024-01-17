import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../LayoutTemplate/Layout';
import Spinner from '../GeneralComponents/Spinner';

const LogoutPage = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  const logoutWithRetry = async (retryCount = 3, delay = 1000) => {
    for (let i = 0; i < retryCount; i++) {
    try {
      const response = await fetch('/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log(loading)
      if (response.ok) {
        setLoading(false);
        navigate('/');
        return;
      }
    } catch (error) {
      console.error('Error during fetch:', error);
      alert('Failed to logout')
      navigate('/');
      setLoading(false);
    }
    await new Promise(resolve => setTimeout(resolve, delay));
  };
  setLoading(false);
  alert('Logging out failed')
  navigate('/')
  }
  React.useEffect(() => {
    logoutWithRetry();

  }, );

  return (
    <Layout>
      {loading ? (
        <Spinner>Logging out</Spinner>
      ) : (
        <p></p>
      )}
    </Layout>
  );
};

export default LogoutPage;