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
      await axios.post('/api/confirm', formData);
      setMessage(<span style={{ color: green[500] }}>Obrigado pela Confirmação!</span>);
      clearForm();
    } catch (error) {
      setMessage(<span style={{ color: red[500] }}>Erro ao enviar confirmação :(</span>);
    }

  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', color: 'white' }}>
      <TextField 
        label="Nome" 
        name="name" 
        variant='outlined'
        id = "name"
        value={formData.name} 
        onChange={handleChange} 
        fullWidth 
        margin="normal"
        InputLabel={{ style: { color: 'white' } }}
        InputProps={{ style: { color: 'white' } }}
      />
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
        InputLabel={{ style: { color: 'white' } }}
        InputProps={{ style: { color: 'white' } }}
      />
      <TextField 
        label="Celular" 
        name="phone" 
        variant='outlined'
        id="phone"
        value={formData.phone} 
        onChange={handleChange} 
        fullWidth 
        margin="normal"
        InputLabel={{ style: { color: 'white' } }}
        InputProps={{ style: { color: 'white' } }}
      />
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
      <Button type="submit" variant="contained" color="primary">
        Enviar
      </Button>
      {message && <p>{message}</p>}
    </form>
  );
};

export default ConfirmationForm;
