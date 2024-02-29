import csv
from app import db, Job, app

def update_requirements_from_file(filename, limit=3000):
    with app.app_context():
            processed_count = 0
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if processed_count >= limit:
                        break

                    job_skills = row['job_skills']

                    # Update the "requirements" column for all rows in the Job table
                    jobs = Job.query.all()
                    for job in jobs:
                        job.requirements = job_skills
                        processed_count += 1
                        if processed_count >= limit:
                            break

                # Commit the changes to the database
                db.session.commit()

# Usage: Call the function with the filename
update_requirements_from_file('job_skills.csv', limit=3000)