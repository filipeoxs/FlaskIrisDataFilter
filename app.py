import io
import csv
from flask import Flask, render_template, request, Response, jsonify
from sklearn.datasets import load_iris

app = Flask(__name__)

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
feature_names = iris.feature_names

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        filtered_data = []
        for i in range(len(X)):
            if (
                X[i][0] >= sepal_length and
                X[i][1] >= sepal_width and
                X[i][2] >= petal_length and
                X[i][3] >= petal_width
            ):
                filtered_data.append(list(X[i]))

        return render_template('index.html', data=filtered_data, feature_names=feature_names)

    return render_template('index.html', data=X.tolist(), feature_names=feature_names)

@app.route('/export', methods=['POST'])
def export_data():
    if request.method == 'POST':
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_length')
        petal_width = request.form.get('petal_width')

        # Verifique se os campos estão presentes e não vazios
        if sepal_length and sepal_width and petal_length and petal_width:
            sepal_length = float(sepal_length)
            sepal_width = float(sepal_width)
            petal_length = float(petal_length)
            petal_width = float(petal_width)

            filtered_data = []
            for i in range(len(X)):
                if (
                    X[i][0] >= sepal_length and
                    X[i][1] >= sepal_width and
                    X[i][2] >= petal_length and
                    X[i][3] >= petal_width
                ):
                    filtered_data.append(list(X[i]))

            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(iris.feature_names)
            writer.writerows(filtered_data)
            output.seek(0)

            response = Response(output, mimetype='text/csv')
            response.headers['Content-Disposition'] = 'attachment; filename=filtered_data.csv'
            return response
        else:
            return "Preencha todos os campos do formulário antes de exportar os dados."
if __name__ == '__main__':
    app.run(debug=True)
