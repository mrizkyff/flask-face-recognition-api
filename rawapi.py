from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import face_recognition

app =Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
	if request.method == 'GET':
		return jsonify({
			"response":"Get Request Called!"
		})
	elif request.method == 'POST':
		req_Json = request.json
		name = req_Json['name']
		return jsonify({
			"response":'hi ' + name
		})	


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		resp = {
			'response':''
		}
		

		if request.files['img']:
			f = request.files['img']
			f.save(secure_filename(f.filename))
			return perhitungan_face_recognition()
		else:
			return jsonify("file kosong boy!")
		

	elif request.method == 'GET':
		return jsonify('halo am get!')

def perhitungan_face_recognition():
	face_found = False
	identified = False
	diff = 0.0

	# image yang dikenali
	known_image = face_recognition.load_image_file('profile.png')
	known_image_encoding = face_recognition.face_encodings(known_image)[0]

	# image yang akan diuji
	unknown_image = face_recognition.load_image_file('img.jpg')
	unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

	if len(unknown_image_encoding) > 0:
		face_found = True
		# cek kecocokan
		match_result = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)
		# hitung jarak / perbedaan
		diff = face_recognition.face_distance([known_image_encoding], unknown_image_encoding)

		if match_result[0]:
			identified = True

	# return as json
	result = {
		"face_found_in_image": face_found,
		"is_identified": identified,
		"similarity": float(diff)
	}
	return jsonify(result)


if __name__ == '__main__':
	app.run(host="192.168.8.104",debug=True)