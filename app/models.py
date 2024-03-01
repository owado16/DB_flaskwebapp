# app/models.py

from app import db

class Industry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    jobs = db.relationship('Job', backref='industry', lazy=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'), nullable=False)
    level = db.Column(db.String(50), nullable=False)
