import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h2>AI‑First CRM – HCP Interaction Logger</h2>

      <textarea
        rows="5"
        cols="60"
        placeholder="Enter HCP interaction details..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br /><br />

      <button onClick={sendMessage}>
        Log Interaction
      </button>

      <h3>AI Response:</h3>
      <p>{response}</p>
    </div>
  );
}

export default App;
