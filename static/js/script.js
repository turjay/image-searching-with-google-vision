document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const resultSection = document.getElementById("result-section");
    const resultList = document.getElementById("result-list");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const fileInput = document.getElementById("file");
        const file = fileInput.files[0];

        if (!file) {
            alert("Lütfen bir görsel seçin!");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        fetch("/upload", {
            method: "POST",
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                resultSection.style.display = "block";
                resultList.innerHTML = "";
                data.labels.forEach(label => {
                    const li = document.createElement("li");
                    li.innerHTML = `<span>${label.description}</span> - <span>%${(label.score * 100).toFixed(2)}</span>`;
                    resultList.appendChild(li);
                });
            })
            .catch(error => console.error("Error:", error));
    });
});
