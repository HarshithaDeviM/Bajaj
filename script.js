function sendData() {
    const jsonInput = document.getElementById("jsonInput").value;

    fetch('https://bajaj-m5jh.onrender.com/bfhl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonInput
    })
    .then(response => response.json())
    .then(data => {
        displayResponse(data);
    })
    .catch(error => {
        document.getElementById("responseOutput").innerText = 'Error: ' + error.message;
    });
}

function displayResponse(data) {
    const selectedOptions = Array.from(document.querySelectorAll('#responseFilter input[type="checkbox"]:checked')).map(checkbox => checkbox.value);
    let output = {};

    if (selectedOptions.includes("numbers")) {
        output["Numbers"] = data.numbers;
    }
    if (selectedOptions.includes("alphabets")) {
        output["Alphabets"] = data.alphabets;
    }
    if (selectedOptions.includes("highestLowercaseAlphabet")) {
        output["Highest Lowercase Alphabet"] = data.highest_lowercase_alphabet;
    }

    document.getElementById("responseOutput").innerText = JSON.stringify(output, null, 2);
}
