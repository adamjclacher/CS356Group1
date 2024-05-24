function helloWorld() {
    const options = {
        projectName: document.getElementById("projectName").value,
        radioOption: document.querySelector('input[name="radioOption"]:checked').value
    };

    alert(JSON.stringify(options));
}