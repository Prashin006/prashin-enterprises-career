from flask import Flask, render_template, jsonify

JOBS =[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 7,50,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'New York, USA',
        'salary':'$ 120,000'
    },
    {
        'id':3,
        'title':'Software Developer',
        'location':'Mumbai, India',
        'salary':'Rs. 22,50,000'
    },
    {
        'id':4,
        'title':'Frontend Engineer',
        'location':'Florida, USA',
        'salary':'$ 105,000'
    }
]

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='Pushti Sanitaryware')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)