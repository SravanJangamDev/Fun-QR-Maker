baseurl = "https://app.loan2wheels.com/qrcode"

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
display();