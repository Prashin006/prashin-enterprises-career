from flask import Flask, render_template, jsonify
from datetime import datetime

now = datetime.now()
openings = [
        {
            "id": 1,
            "title": "Content Creator Intern",
            "location": "Remote",
            "description": "Create engaging and informative content for financial and technical courses. Responsible for research, writing, and content development.",
        },
        {
            "id": 2,
            "title": "Video Editing Intern",
            "location": "Remote",
            "description": "Edit video lectures and tutorials for financial and technical courses. Ensure high-quality production and engaging visual content.",
        },
        {
            "id": 3,
            "title": "Marketing Specialist Intern",
            "location": "Remote",
            "description": "Develop and execute marketing strategies to promote financial and technical courses. Focus on increasing reach and engagement.",
        },
        {
            "id": 4,
            "title": "Social Media Handler Intern",
            "location": "Remote",
            "description": "Manage social media accounts, create and schedule posts, and engage with the audience to build a strong online presence for our courses.",
        },
    ]

app = Flask(__name__)


@app.context_processor
def inject_global_variable():
    jobs = openings
    current_year = str(now.year)
    company_name = "Prashin Enterprises"
    description = f"{company_name} is a pioneering company dedicated to providing accessible and high-quality educational resources. Our mission is to empower individuals by offering free courses in various domains, ensuring that education is within everyone's reach."

    return dict(company_name=company_name, description=description, jobs=jobs, current_year=current_year)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",active_page='home')


@app.route("/jobs")
def jobs():
    return render_template("jobs.html",active_page='jobs')


@app.route("/about-us")
def about():
    return render_template("about.html",active_page='about')


@app.route("/courses")
def courses():
    return render_template("courses.html",active_page='courses')


@app.route("/contact-us")
def contact():
    return render_template("contact.html",active_page='contact')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(openings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
