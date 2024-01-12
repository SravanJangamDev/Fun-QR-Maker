from flask import Flask, render_template, send_from_directory
import qrcode
import os
from random import randint
import json

from config import BASEURL, FRONTEND_PATH, FRONTEND_BASE_URL

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


def generate_qr_code(image):
    qr.add_data(image)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{FRONTEND_PATH}/qrcode.png")


tasks = [
    {
        "taskid": "1",
        "image": "smiley.png",
        "tagline": "Share the best memory you have with your manager.",
    },
    {
        "taskid": "2",
        "image": "smiley.png",
        "tagline": "Share a funny or interesting fact about yourself that most people don't know.",
    },
    {
        "taskid": "3",
        "image": "smiley.png",
        "tagline": "What positive feelings you have about HR, and describe them.",
    },
]

images = os.listdir(f"{FRONTEND_PATH}/images")
app = Flask(__name__)

generate_qr_code(f"{FRONTEND_BASE_URL}/display.html")
selected_task: dict = {}


@app.route("/qrcode", methods=["GET"])
def generate_qr():
    global selected_task
    task = tasks[randint(0, len(tasks) - 1)]
    image = task.get("image", "")
    tagline = task.get("tagline", "")
    selected_task = task
    response = app.response_class(
        response=json.dumps(
            {
                "image_url": f"{FRONTEND_BASE_URL}/images/{image}",
                "qr_url": f"{FRONTEND_BASE_URL}/qrcode.png",
                "tagline": tagline,
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


@app.route("/qrcode/selected", methods=["GET"])
def get_selected():
    global selected_task
    image = selected_task.get("image", "")
    tagline = selected_task.get("tagline", "")

    response = app.response_class(
        response=json.dumps(
            {
                "image_url": f"{FRONTEND_BASE_URL}/images/{image}",
                "tagline": tagline,
            }
        ),
        status=200,
        mimetype="application/json",
    )
    return response


# @app.route("/qrcode/images/<filename>")
# def show_image(filename):
#     return send_from_directory("images", filename)


# @app.route("/qrcode/qrcodes/<filename>")
# def show_qrcode(filename):
#     return send_from_directory("images", filename)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8600)
