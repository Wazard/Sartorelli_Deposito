const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("fileInput");

// Drag & drop events
dropZone.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropZone.classList.add("dragover");
});
dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("dragover");
});
dropZone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropZone.classList.remove("dragover");
  const file = e.dataTransfer.files[0];
  handleFile(file);
});

// Browse button
fileInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  handleFile(file);
});

async function handleFile(file) {
  if (file && file.name.endsWith(".csv")) {
    // Read file contents in JS
    const text = await file.text();
    // Send to Python via Eel
    eel.load_csv(text)();
  } else {
    alert("Please select a CSV file.");
  }
}