import React, { useState } from 'react';
import axios from 'axios';
import './Home.css'; // Import the Home.css file


function App() {
    const [tac, setTac] = useState('');
    const [prediction, setPrediction] = useState('');

    const handlePredict = async () => {
        try {
            const response = await axios.post('http://localhost:5000/predict', { tac });
            setPrediction(response.data.prediction);
        } catch (error) {
            console.error("There was an error making the prediction!", error);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>TAC Predictor</h1>
                <input
                    type="text"
                    value={tac}
                    onChange={(e) => setTac(e.target.value)}
                    placeholder="Enter TAC"
                />
                <button onClick={handlePredict}>Predict</button>
                {prediction && <p>Prediction: {prediction}</p>}
            </header>
        </div>
    );
}

export default App;


