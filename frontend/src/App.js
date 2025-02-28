import React from 'react';
import { Container } from '@mui/material';
import ConfirmationForm from './components/ConfirmationForm';
import MapComponent from './components/MapComponent';
import Information from './components/Information';

function App() {

  return (
    <Container maxWidth="sm">
      <Information/>
      <ConfirmationForm />
      <MapComponent />

    </Container>
  );
}

export default App;
