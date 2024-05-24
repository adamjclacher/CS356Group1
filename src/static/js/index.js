/**
 * displayPageOptions
 * Used for debugging purposes at the moment
 */
function displayPageOptions() {
    const options = {
        projectName: document.getElementById("projectName").value,
        radioOption: document.querySelector('input[name="radioOption"]:checked').value
    };

    alert(JSON.stringify(options));
}