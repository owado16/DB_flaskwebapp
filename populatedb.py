import csv
from app import db, Job, Industry, app

def populate_database_from_csv(filename, limit=3000):
    processed_count = 0
    with app.app_context():
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if processed_count >= limit:
                    break

                job_title = row['job_title']
                company = row['company']
                location = row['job_location']
                level = row['job_level']
                requirements = "No requirements available"  # You may adjust this based on your requirements
                
                # Fetch the industry object based on the industry name
                industry_name = row.get('industry')  # Attempt to get industry name from CSV
                industry = None
                if industry_name:
                    industry = Industry.query.filter_by(name=industry_name).first()
                
                # If industry is not found or industry name is not provided, assign a default industry ID
                if not industry:
                    # You can set a default industry ID here or handle this case as per your requirement
                    industry_id = 1  # Default industry ID (Modify as needed)
                else:
                    industry_id = industry.id
                
                # Create a new Job instance with the fetched industry_id
                job = Job(title=job_title, company=company, location=location, 
                          industry_id=industry_id, level=level, requirements=requirements)
                db.session.add(job)
                processed_count += 1
                    
            # Commit the changes to the database
            db.session.commit()

def populate_industry_table():
    with app.app_context():
        # Example: List of industry names
        industry_names = ['Technology', 'Finance', 'Healthcare', 'Education', 'Manufacturing', 'Retail', 'Hospitality', 'Media']

        with db.session.begin_nested():
            for name in industry_names:
                # Create a new Industry instance and add it to the database
                industry = Industry(name=name)
                db.session.add(industry)

        # Commit the changes to the database
        db.session.commit()

# Usage: Call the function to populate the Industry table
populate_industry_table()

# Usage: Call the function with the filename and limit
populate_database_from_csv('linkedin_job_postings.csv', limit=3000)