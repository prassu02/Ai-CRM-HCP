import React, { useState } from "react";
import { sendInteraction } from "./api";

function App() {
  const [doctorName, setDoctorName] = useState("");
  const [notes, setNotes] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const data = {
        doctor_name: doctorName,
        notes: notes,
      };

      const res = await sendInteraction(data);
      setResult(res);
    } catch (err) {
      alert("Error connecting to backend");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h2>AI CRM System</h2>

      <input
        type="text"
        placeholder="Doctor Name"
        value={doctorName}
        onChange={(e) => setDoctorName(e.target.value)}
        style={{ display: "block", marginBottom: "10px", width: "300px" }}
      />

      <textarea
        placeholder="Notes"
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        style={{
          display: "block",
          marginBottom: "10px",
          width: "300px",
          height: "100px",
        }}
      />

      <button onClick={handleSubmit}>
        {loading ? "Processing..." : "Submit"}
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Summary:</h3>
          <p>{result.summary}</p>

          <h3>Next Actions:</h3>
          <ul>
            {result.next_action.map((action, index) => (
              <li key={index}>{action}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;