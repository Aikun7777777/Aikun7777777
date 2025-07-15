import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <h1>99乘法表</h1>
      <table style={{ borderCollapse: 'collapse', margin: '0 auto' }}>
        <tbody>
          {Array.from({ length: 9 }, (_, i) => (
            <tr key={i}>
              {Array.from({ length: i + 1 }, (_, j) => (
                <td
                  key={j}
                  style={{
                    border: '1px solid #ccc',
                    padding: '8px 12px',
                    textAlign: 'center',
                    background: '#f9f9f9',
                  }}
                >
                  {`${j + 1} × ${i + 1} = ${(j + 1) * (i + 1)}`}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
