document.addEventListener("DOMContentLoaded", function () {
    const themeSelect = document.getElementById("theme-select");
    const saveButton = document.getElementById("save-theme-btn");
    const message = document.getElementById("theme-message");

    if (themeSelect && saveButton) {
        themeSelect.value = localStorage.getItem("theme") || "light";
        document.body.setAttribute("data-theme", themeSelect.value);

        saveButton.addEventListener("click", () => {
            const theme = themeSelect.value;
            document.body.setAttribute("data-theme", theme);
            localStorage.setItem("theme", theme);

            message.style.display = "block";
            setTimeout(() => {
                message.style.display = "none";
            }, 2000);
        });
    }
});