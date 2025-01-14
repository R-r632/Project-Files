document.getElementById("upload-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const fileInput = document.getElementById("file-upload");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const resultElement = document.getElementById("result");
    resultElement.textContent = "Predicting...";

    try {
        const response = await fetch("/", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();
        resultElement.textContent = `Prediction: ${data.class_name}`;
    } catch (error) {
        resultElement.textContent = "Error: Could not predict the image.";
    }
});
