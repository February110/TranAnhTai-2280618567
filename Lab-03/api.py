from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['POST'])
def rsa_generate_keys():
    try:
        rsa_cipher.generate_keys()
        return jsonify({'message': 'Keys generated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    try:
        data = request.json
        message = data['message']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()
        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({'error': 'Invalid key type, must be "public" or "private".'}), 400
        encrypted_message = rsa_cipher.encrypt(message, key)
        encrypted_hex = encrypted_message.hex()
        return jsonify({'encrypted_message': encrypted_hex})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    try:
        data = request.json
        ciphertext_hex = data['ciphertext']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()
        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({'error': 'Invalid key type, must be "public" or "private".'}), 400
        ciphertext = bytes.fromhex(ciphertext_hex)
        decrypted_message = rsa_cipher.decrypt(ciphertext, key)
        return jsonify({'decrypted_message': decrypted_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    try:
        data = request.json
        message = data['message']
        private_key, _ = rsa_cipher.load_keys()
        signature = rsa_cipher.sign(message, private_key)
        signature_hex = signature.hex()
        return jsonify({'signature': signature_hex})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    try:
        data = request.json
        message = data['message']
        signature_hex = data['signature']
        _, public_key = rsa_cipher.load_keys()
        signature = bytes.fromhex(signature_hex)
        verified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({'verified': verified})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
