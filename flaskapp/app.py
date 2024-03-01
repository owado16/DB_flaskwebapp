# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skillsearch.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Industry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     jobs = db.relationship('Job', backref='industry', lazy=True)

# class Job(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     company=db.Column(db.String(100), nullable=False)
#     location=db.Column(db.String(100), nullable=False)
#     requirements = db.Column(db.Text, nullable=False)
#     industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'), nullable=False)
#     level = db.Column(db.String(50), nullable=False)


# @app.route('/')
# def index():
#     return render_template('index.html')
# @app.route('/search')
# def displaysearch():
#     return render_template("search.html")

# @app.route('/search_result', methods=['POST'])
# def search():
#     job_title = request.form.get('job_title')
#     # Query the database for jobs matching the provided job title
#     jobs = Job.query.filter(Job.title.ilike(f'%{job_title}%')).all()
#     return render_template('search_results.html', jobs=jobs)

# if __name__ == '__main__':
#     app.run(debug=True)
