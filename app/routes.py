# app/routes.py

from flask import flash, redirect, render_template, request, url_for
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

    # Check if job title is provided
    if not job_title:
        flash('Please enter a job title.')
        return redirect(url_for('index'))

    # Query the database for jobs matching the provided job title
    jobs = Job.query.filter(Job.title.ilike(f'%{job_title}%')).all()

    # Render the template with the search results
    return render_template('search_results.html', jobs=jobs)
