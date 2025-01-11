document.addEventListener("DOMContentLoaded", () => {
    const dropZone = document.getElementById("drop-zone");
    const fileInput = document.getElementById("file-input");

    dropZone.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZone.classList.add("drag-over");
    });

    dropZone.addEventListener("dragleave", () => {
        dropZone.classList.remove("drag-over");
    });

    dropZone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropZone.classList.remove("drag-over");
        const files = e.dataTransfer.files;
        updateFileInput(files);
    });

    fileInput.addEventListener("change", (e) => {
        const files = e.target.files;
        updateFileInput(files);
    });

    function updateFileInput(files) {
        fileInput.files = files;
        const fileLabel = dropZone.querySelector("label[for='file-input']");
        if (files.length === 1) {
            dropZone.querySelector("p").textContent = `1 file chosen`;
        } else {
            dropZone.querySelector("p").textContent = `${files.length} files chosen`;
        }
        fileLabel.style.display = "none"; 
    }
});
