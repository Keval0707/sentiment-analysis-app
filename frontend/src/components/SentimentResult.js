import React from 'react';

function SentimentResult({ sentiment }) {
  return (
    <div>
      <h2>Result: {sentiment}</h2>
    </div>
  );
}

export default SentimentResult;