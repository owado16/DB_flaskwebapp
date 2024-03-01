# app/routes.py

from flask import render_template, request
from app import app
from app.models import Job

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def display_search():
    return render_template("search.html")

@app.route('/search_result', methods=['POST'])
def search():
    job_title = request.form.get('job_title')
    jobs = Job.query.filter(Job.title.ilike(f'%{job_title}%')).all()
    return render_template('search_results.html', jobs=jobs)
