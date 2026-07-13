const analyseButton = document.getElementById("analyse-btn");
const result = document.getElementById("result");

analyseButton.addEventListener("click", async () => {
    const response = await fetch("/analyse", {
        method: "POST",
    });

    const data = await response.json();

    result.innerHTML = `
        <p>Status: ${data.status}</p>
        <p>Image: ${data.image}</p>
        <p>Brightness(0~255): ${data.scene.brightness.toFixed(1)}</p>
        <p>Dominant Color: ${data.scene.dominant_color}</p>
        <pre>${JSON.stringify(data.scene.observation, null, 2)}</pre>
    `;
});