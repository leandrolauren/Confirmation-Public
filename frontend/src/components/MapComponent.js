import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const MapComponent = () => {
  const address = "Rua Werner Habig, 831 - Chácaras Luzitana - Lote 13 Hortolandia-SP, 13187-020";
  const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(address)}`;

  const handleClick = () => {
    window.open(googleMapsUrl, "_blank");
  };

  return (
    <Card onClick={handleClick} style={{ cursor: 'pointer', marginTop: '20px', backgroundColor: '#E0FSF', opacity: 0.7 }}>
      <CardContent>
        <Typography variant="h5" align='center'>Clique aqui!</Typography>
        <Typography variant="body2">{address}</Typography>
      </CardContent>
    </Card>
  );
};

export default MapComponent;
