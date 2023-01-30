from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))


@app.route('/', methods=["GET", "POST"])
def index():  # put application's code here
    file_img = base_dir + "/static/files/"
    file_list = os.listdir(file_img)
    if request.method == "GET":
        return render_template("index.html", file_list=file_list)
    else:
        try:
            f = request.files.get('file')
            file_name = secure_filename(f.filename)

            random_num = random.randint(0, 100)
            file_name = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + file_name.rsplit(".")[
                1]
            file_path = base_dir + "/static/files/" + file_name
            # print(file_path)
            f.save(file_path)
            # 配置对应的外网访问链接
            my_host = '127.0.0.1:5000/'
            new_path_file = my_host + '/static/files/' + file_name
            data = {"msg": "success", "url": new_path_file}

            payload = jsonify(data)
            # print(payload.data)

            return render_template('index.html', file_name=file_name, f=f,payload=payload)
        except:
            return render_template('index.html', file_list=file_list)


if __name__ == '__main__':
    app.run()
