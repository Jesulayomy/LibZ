import { useState, useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';
import axios from 'axios';

function ProfileDetails({ user }) {
  const { login } = useContext(AuthContext);
  const [editing, setEditing] = useState(false);
  const [updatedData, setUpdatedData] = useState({
    first_name: user.first_name,
    last_name: user.last_name,
    display_name: user.display_name || user.first_name + ' ' + user.last_name,
    phone: user.phone,
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUpdatedData((prevUpdatedData) => ({
      ...prevUpdatedData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    const formData = new FormData();
    for (const key in updatedData) {
      if (updatedData[key]) formData.append(key, updatedData[key]);
    }
    try {
      const res = await axios.put(
        `http://localhost:5000/api/users/${user.id}`,
        formData
      );
      const updatedUser = res.data;
      login(updatedUser);
      setEditing(false);
    } catch (error) {
      console.log(error);
    }
  };

  const calculateAge = (dob) => {
    const diff_ms = Date.now() - dob.getTime();
    const age_dt = new Date(diff_ms);
    return Math.abs(age_dt.getUTCFullYear() - 1970);
  };
  const age = calculateAge(new Date(user.date_of_birth));

  return (
    <div className='profile'>
      <div className='profile-image'>
        <img src='https://picsum.photos/200/300' alt='Profile' />
      </div>
      <div className='profile-details'>
        <div className='detail'>
          <div className='head'>Display Name</div>
          {editing ? (
            <input
              type='text'
              name='display_name'
              value={updatedData.display_name}
              onChange={handleChange}
              className='value-input'
            />
          ) : (
            <div className='value'>
              {user.display_name || user.first_name + ' ' + user.last_name}
            </div>
          )}
        </div>
        <div className='detail'>
          <div className='head'>First Name</div>
          {editing ? (
            <input
              type='text'
              name='first_name'
              value={updatedData.first_name}
              onChange={handleChange}
              className='value-input'
            />
          ) : (
            <div className='value'>{user.first_name}</div>
          )}
        </div>
        <div className='detail'>
          <div className='head'>Last Name</div>
          {editing ? (
            <input
              type='text'
              name='last_name'
              value={updatedData.last_name}
              onChange={handleChange}
              className='value-input'
            />
          ) : (
            <div className='value'>{user.last_name}</div>
          )}
        </div>
        {!editing && (
          <>
            <div className='detail'>
              <div className='head'>Email</div>
              <div className='value'>{user.email}</div>
            </div>
            <div className='detail'>
              <div className='head'>Gender</div>
              <div className='value'>{user.gender}</div>
            </div>
            <div className='detail'>
              <div className='head'>Age</div>
              <div className='value'>{age} years</div>
            </div>
          </>
        )}
        <div className='detail'>
          <div className='head'>Phone</div>
          {editing ? (
            <input
              type='tel'
              name='phone'
              value={updatedData.phone}
              onChange={handleChange}
              className='value-input'
            />
          ) : (
            <div className='value'>{user.phone}</div>
          )}
        </div>
        {editing ? (
          <div className='button'>
            <button onClick={handleSubmit} className='save'>
              Save changes
            </button>
            <button onClick={() => setEditing(false)} className='cancel'>
              Cancel
            </button>
          </div>
        ) : (
          <button onClick={() => setEditing(true)} className='button edit'>
            Edit profile
          </button>
        )}
      </div>
    </div>
  );
}

export default ProfileDetails;
