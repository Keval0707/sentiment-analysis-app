import React, { useState } from 'react';

function SentimentForm({ onAnalyze }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAnalyze(text);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text to analyze..."
        required
      />
      <button type="submit">Analyze Sentiment</button>
    </form>
  );
}

export default SentimentForm;