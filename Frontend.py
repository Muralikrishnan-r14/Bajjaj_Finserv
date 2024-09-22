import React, { useState } from "react";
import axios from "axios";

function App() {
  const [jsonInput, setJsonInput] = useState("");
  const [response, setResponse] = useState(null);
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Validate JSON
      const parsedData = JSON.parse(jsonInput);

      // Make API call to your backend
      const res = await axios.post("http://127.0.0.1:5000/bfhl", {
        data: parsedData.data,
        file_b64: "" // Include this if you have a file to send
      });

      // Handle success
      setResponse(res.data);
      setError(null);
    } catch (err) {
      setError("Invalid JSON format or API error");
    }
  };

  const handleDropdownChange = (e) => {
    setSelectedOptions([...e.target.selectedOptions].map(o => o.value));
  };

  const renderResponse = () => {
    if (!response) return null;

    return (
      <div>
        {selectedOptions.includes("Alphabets") && (
          <div>Alphabets: {response.alphabets.join(", ")}</div>
        )}
        {selectedOptions.includes("Numbers") && (
          <div>Numbers: {response.numbers.join(", ")}</div>
        )}
        {selectedOptions.includes("Highest Lowercase Alphabet") && (
          <div>Highest Lowercase Alphabet: {response.highest_lowercase_alphabet}</div>
        )}
      </div>
    );
  };

  return (
    <div className="App">
      <h1>Enter JSON Input</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={jsonInput}
          onChange={(e) => setJsonInput(e.target.value)}
          placeholder='Enter JSON: { "data": ["A", "B", "1"] }'
        />
        <button type="submit">Submit</button>
      </form>
      {error && <div style={{ color: "red" }}>{error}</div>}
      {response && (
        <>
          <div>
            <label>Select Data to Display:</label>
            <select multiple={true} onChange={handleDropdownChange}>
              <option value="Alphabets">Alphabets</option>
              <option value="Numbers">Numbers</option>
              <option value="Highest Lowercase Alphabet">Highest Lowercase Alphabet</option>
            </select>
          </div>
          {renderResponse()}
        </>
      )}
    </div>
  );
}

export default App;
