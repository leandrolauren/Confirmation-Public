import React, { useState } from 'react';
import { TextField, Button, Checkbox, FormControlLabel } from '@mui/material';
import axios from 'axios';
import { green, red } from '@mui/material/colors';

const ConfirmationForm = () => {

  const initialFormState = {
    name: '',
    email: '',
    phone: '',
    confirmation: true,
    qtt_adult: '',
    qtt_child: ''
  };

  const [formData, setFormData] = useState(initialFormState);
  const [message, setMessage] = useState('');
  
  const clearForm = () => {
    setFormData(initialFormState);
  };

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('https://confirmation-back.onrender.com/api/confirm', formData);
      setMessage(<span style={{ color: green[900] }}>Obrigado pela Confirmação!</span>);
      clearForm();
    } catch (error) {
      setMessage(<span style={{ color: red[500] }}>Erro ao enviar confirmação :(</span>);
    }

  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
      <div style={{ flex: '1 1 200px', minWidth: '200px' }}>
        <TextField 
          label="Nome" 
          name="name" 
          variant='outlined'
          id = "name"
          value={formData.name} 
          onChange={handleChange} 
          fullWidth 
          margin="normal"
          required
          maxlength="100"
          InputLabel={{ style: { color: 'white' } }}
          InputProps={{ style: { color: 'white' } }}
        />
      </div>
      <div style={{ flex: '1 1 200px', minWidth: '200px' }}>
        <TextField 
          label="Email" 
          name="email" 
          variant='outlined'
          id="email"
          type="email"
          value={formData.email} 
          onChange={handleChange} 
          fullWidth 
          margin="normal"
          maxlength="150"
          required
          InputLabel={{ style: { color: 'white' } }}
          InputProps={{ style: { color: 'white' } }}
        />
      </div>
      <div style={{ flex: '1 1 200px', minWidth: '200px' }}>
        <TextField 
          label="Celular" 
          name="phone" 
          variant='outlined'
          id="phone"
          value={formData.phone} 
          onChange={handleChange} 
          fullWidth 
          margin="normal"
          maxlength={10}
          InputLabel={{ style: { color: 'white' } }}
          InputProps={{ style: { color: 'white' } }}
        /> 
      </div>
      <div style={{ flex: '1 1 150px', minWidth: '150px' }}>
        <TextField
          type='number'
          label="Adultos"
          name="qtt_adult"
          variant="outlined"
          id="qtt_adult"
          value={formData.qtt_adult}
          onChange={handleChange}
          margin="normal"
          maxlength="10"
          required
          InputLabel={{ style: { color: 'white' } }}
          InputProps={{ style: { color: 'white' } }}
        />
      </div>
      <div style={{ flex: '1 1 150px', minWidth: '150px' }}> 
        <TextField
          type="number"
          label="Crianças"
          name="qtt_child"
          variant="outlined"
          id="qtt_child"
          value={formData.qtt_child}
          onChange={handleChange}
          margin="normal"
          maxlength="10"
          defaultValue="0"
          InputLabel={{ style: { color: 'white' } }}
          InputProps={{ style: { color: 'white' } }}
        />
      </div>
      <div style={{ flex: '0 1 auto', alignSelf: 'center' }}>
        <FormControlLabel
          control={
            <Checkbox
              name="confirmation"
              checked={formData.confirmation}
              onChange={(e) => setFormData(prev => ({ ...prev, confirmation: e.target.checked }))}
            />
          }
          label="Eu participarei da Festa!"
        />
      </div>
      <div style={{flex: '1 1 auto', alignSelf: 'center'}}>
        <Button type="submit" variant="contained" color="primary">
          Confirmar
        </Button>
      </div>
      {message && <p>{message}</p>}
    </form>
  );
};

export default ConfirmationForm;
