document.getElementById("recommendBtn").addEventListener("click", getRecommendations);

async function getRecommendations() {
  const idea = document.getElementById("ideaInput").value;
  if (!idea) {
    alert("⚠️ Please enter an idea first!");
    return;
  }

  document.getElementById("loading").style.display = "block";
  document.getElementById("result").innerHTML = "";

  try {
    const response = await fetch("/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea })
    });

    const data = await response.json();
    document.getElementById("loading").style.display = "none";

    if (data.error) {
      document.getElementById("result").innerHTML =
        `<p style="color:red;">❌ ${data.error}</p>`;
    } else {
      document.getElementById("result").innerHTML =
        `<h3>✅ Recommendations:</h3><p>${data.recommendations}</p>`;
    }

  } catch (err) {
    document.getElementById("loading").style.display = "none";
    document.getElementById("result").innerHTML =
      `<p style="color:red;">⚠️ Error: ${err.message}</p>`;
  }
}
