import { useState } from 'react';
import { AiOutlineClose } from 'react-icons/ai';
import Login from './Login';
import SignUp from './SignUp';
import '../styles/AuthPage.css';

function AuthPage({ close }) {
  const [isSigningUp, setIsSigningUp] = useState(false);

  return (
    <div className='login-form'>
      <button onClick={close} className='close-button'>
        <AiOutlineClose color='black' />
      </button>
      <div className='select-login'>
        <div
          className={isSigningUp ? 'current' : ''}
          onClick={() => setIsSigningUp(true)}
        >
          Sign Up
        </div>
        <div
          className={!isSigningUp ? 'current' : ''}
          onClick={() => setIsSigningUp(false)}
        >
          Login
        </div>
      </div>
      {isSigningUp ? <SignUp close={close} /> : <Login close={close} />}
    </div>
  );
}

export default AuthPage;
