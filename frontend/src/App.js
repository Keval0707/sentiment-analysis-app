import React, { useState } from 'react';
import SentimentForm from './components/SentimentForm';
import SentimentResult from './components/SentimentResult';
import './App.css';
//app.css

function App() {
  const [sentiment, setSentiment] = useState('');

  const handleAnalyze = async (text) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        const errorMessage = await response.text();  // Get detailed error message
        throw new Error(`Server error: ${response.status} - ${errorMessage}`);
      }

      const data = await response.json();
      setSentiment(data.sentiment);
    } catch (error) {
      console.error("Fetch error:", error.message);
      setSentiment("Error: Could not fetch sentiment. Check backend.");
    }
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis</h1>
      <SentimentForm onAnalyze={handleAnalyze} />
      <SentimentResult sentiment={sentiment} />
    </div>
  );
}

export default App;
