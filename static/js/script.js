// ==============================
// House Price Prediction Script
// ==============================

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("predictionForm");
    const button = document.getElementById("predictBtn");

    if (!form || !button) return;

    form.addEventListener("submit", function (e) {

        const area = document.querySelector("input[name='area']");
        const bedrooms = document.querySelector("input[name='bedrooms']");
        const bathrooms = document.querySelector("input[name='bathrooms']");

        // Validation
        if (
            area.value.trim() === "" ||
            bedrooms.value.trim() === "" ||
            bathrooms.value.trim() === ""
        ) {
            e.preventDefault();
            alert("Please fill in all fields.");
            return;
        }

        if (Number(area.value) <= 0) {
            e.preventDefault();
            alert("Area must be greater than 0.");
            area.focus();
            return;
        }

        if (Number(bedrooms.value) <= 0) {
            e.preventDefault();
            alert("Bedrooms must be at least 1.");
            bedrooms.focus();
            return;
        }

        if (Number(bathrooms.value) <= 0) {
            e.preventDefault();
            alert("Bathrooms must be at least 1.");
            bathrooms.focus();
            return;
        }

        // Loading Button
        button.disabled = true;
        button.innerHTML = "Predicting...";

    });

});