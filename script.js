async function checkInteraction() {
  const medicine = document.getElementById("medicineInput").value.trim();
  const resultDiv = document.getElementById("result");

  if (!medicine) {
    resultDiv.innerHTML = "<p>Please enter a medicine name.</p>";
    return;
  }

  resultDiv.innerHTML = "<p>Checking dietary interactions...</p>";

  try {
    const response = await fetch("YOUR_BACKEND_API_URL", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        medicine: medicine
      })
    });

    const data = await response.json();
    resultDiv.innerHTML = `<p><strong>Results for ${medicine}:</strong><br>${data.result}</p>`;
  } catch (error) {
    console.error(error);
    resultDiv.innerHTML = "<p>Failed to fetch interaction data.</p>";
  }
}
