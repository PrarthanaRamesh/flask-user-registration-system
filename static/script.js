document.addEventListener("DOMContentLoaded", function () {

   
    const phoneInput = document.querySelector('input[name="phone"]');
    phoneInput.addEventListener("input", function () {
        this.value = this.value.replace(/[^0-9]/g, "");
    });

    
    const dobInput = document.querySelector('input[name="dob"]');
    const today = new Date().toISOString().split("T")[0];
    dobInput.setAttribute("max", today);

   
    const countrySelect = document.getElementById("country");
    const stateSelect = document.getElementById("state");

    const countryStateMap = {
        India: [
            "Tamil Nadu",
            "Kerala",
            "Karnataka",
            "Maharashtra",
            "Other"
        ],
        USA: [
            "California",
            "Texas",
            "New York",
            "Florida",
            "Other"
        ],
        Other: ["Other"]
    };

    countrySelect.addEventListener("change", function () {
        stateSelect.innerHTML = '<option value="">-- Select State --</option>';

        if (countryStateMap[this.value]) {
            countryStateMap[this.value].forEach(function (state) {
                const option = document.createElement("option");
                option.value = state;
                option.textContent = state;
                stateSelect.appendChild(option);
            });
        }
    });

});
