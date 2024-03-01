# tests.py

import unittest
from app import app, db
from app.models import Job, Industry

class FlaskTest(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():  # Set up application context
            db.create_all()

            # Create sample industry
            industry = Industry(name='Technology')
            db.session.add(industry)
            db.session.commit()

            # Insert sample data into the test database
            job1 = Job(title='Software Engineer', company='Tech Corp', location='California', requirements='Python, Java', industry_id=industry.id, level='Senior')
            job2 = Job(title='Data Scientist', company='Data Inc', location='New York', requirements='Python, R', industry_id=industry.id, level='Mid-Level')
            db.session.add(job1)
            db.session.add(job2)
            db.session.commit()

    def tearDown(self):
        with app.app_context():  # Set up application context
            db.session.remove()
            db.drop_all()

    def test_index(self):
        with app.app_context():  # Set up application context
            response = self.app.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Welcome to Our Job Search App', response.data)

    def test_search(self):
        with app.app_context():  # Set up application context
            response = self.app.post('/search_result', data=dict(job_title='Engineer'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Software Engineer', response.data)
            self.assertNotIn(b'Data Scientist', response.data)

if __name__ == '__main__':
    unittest.main()
