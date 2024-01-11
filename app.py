from flask import Flask, render_template, send_from_directory
import qrcode
import os
from random import randint

from config import BASEURL

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


def generate_qr_code(image, filename):
    url = f"{BASEURL}/{image}"
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qrcodes/{filename}")

    return f"qrcodes/{filename}"


images = os.listdir("images")
images = [f"images/{img}" for img in images]

app = Flask(__name__)


@app.route("/")
def index():
    image = images[randint(0, len(images) - 1)]
    qr_url = generate_qr_code(image, "qrcode.png")

    return render_template(
        "index.html", qr_url=qr_url, image_url=image, heading="Scan QR"
    )


@app.route("/images/<filename>")
def show_image(filename):
    return send_from_directory("images", filename)


@app.route("/qrcodes/<filename>")
def show_qrcode(filename):
    return send_from_directory("images", filename)


if __name__ == "__main__":
    app.run(debug=True)
