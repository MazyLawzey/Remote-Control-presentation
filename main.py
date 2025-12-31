import os
from flask import Flask, send_from_directory, jsonify
from pynput.keyboard import Controller, Key


app = Flask(__name__, static_folder='static')
keyboard = Controller()


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/left', methods=['POST'])
def press_left():
    print('🔵 LEFT')
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    return jsonify({'status': 'ok', 'key': 'left'})


@app.route('/right', methods=['POST'])
def press_right():
    print('🔴 RIGHT')
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    return jsonify({'status': 'ok', 'key': 'right'})


if __name__ == '__main__':
	cert_file = os.path.join('certs', 'cert.pem')
	key_file = os.path.join('certs', 'key.pem')
	port = int(os.environ.get('PORT', 443))
	if not (os.path.exists(cert_file) and os.path.exists(key_file)):
		print("SSL cert/key not found. Generate them with ./generate_cert.sh")
		raise SystemExit("Missing SSL certificate and key. Run './generate_cert.sh' to create them.")
	context = (cert_file, key_file)
	app.run(host='0.0.0.0', port=port, ssl_context=context)

