baseurl = "https://app.loan2wheels.com/qrcode"

function viewimage() {
    document.getElementById("image-box").style.display = "block";
    document.getElementById("qr-box").style.display = "none";
    document.getElementById("heading").innerText = "You got:";
    document.getElementById("reset-btn").style.display = "inline";
    document.getElementById("view-btn").style.display = "none";
    document.getElementById("tagline").style.display = "block";
};

function reset() {

    fetch(baseurl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("display-image").src = data.image_url;
            document.getElementById("display-qr").src = data.qr_url;
            document.getElementById("tagline").innerText = data.tagline;

            document.getElementById("image-box").style.display = "none";
            document.getElementById("qr-box").style.display = "block";
            document.getElementById("tagline").style.display = "none";

            document.getElementById("heading").innerText = "Scan QR:";
            document.getElementById("reset-btn").style.display = "none";
            document.getElementById("view-btn").style.display = "inline";
        })
        .catch(error => console.error('Error:', error));
};

function display() {
    fetch(baseurl + "/" + "selected", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("display-image").src = data.image_url;
            document.getElementById("tagline").innerText = data.tagline;
        })
        .catch(error => console.error('Error:', error));
}

reset();