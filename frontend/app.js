const analyseButton = document.getElementById("analyse-btn");
const result = document.getElementById("result");

analyseButton.addEventListener("click", async () => {
    const response = await fetch("/analyse", {
        method: "POST",
    });

    const data = await response.json();

    result.innerHTML = `
        <p>Status: ${data.status}</p>
        <p>Brightness: ${data.scene.brightness}</p>
        <p>Dominant Color: ${data.scene.dominant_color}</p>
    `;
});