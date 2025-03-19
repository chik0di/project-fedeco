import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine
import pyodbc
from name_provider import SurnameProvider, FirstNameByGender

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-DGGI0QJ\\SQLEXPRESS;"
    "DATABASE=fedeco;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

fake = Faker()
fake.add_provider(FirstNameByGender)
fake.add_provider(SurnameProvider)

def insert_staff(num_records):
    for _ in range(num_records):

        gender = random.choice(["M", "F"])
        if gender == "M":
            first_name = fake.male_name()
            middle_name = fake.first_name_male() 
        else:
            first_name = fake.female_name()
            middle_name = fake.first_name_female() 

        last_name = fake.surname()
        date_of_birth = fake.date_of_birth(minimum_age=27, maximum_age=60).strftime("%Y-%m-%d")
        
        ispc = ['080', '090', '081', '070', '091']
        phone_number = random.choice(ispc) + str(random.randint(10000000, 99999999))

        state_id = random.randint(1,37)

        domains = [ "gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com",
        "icloud.com", "protonmail.com", "zoho.com", "gmx.com", "mail.com",
        "yandex.com", "fastmail.com"
        ]
        email = first_name.lower() + last_name.lower() + str(random.randint(100,9999)) + "@" + random.choice(domains)

        # Insert data into StaffDim
        query = """
        INSERT INTO StaffDim (first_name, middle_name, last_name, date_of_birth, gender, state_id, phone_number, email_address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        cursor.execute(query, (first_name, middle_name, last_name, date_of_birth, gender, state_id, phone_number, email))

    conn.commit()
    print(f"Successfully inserted {num_records} staff records into StaffDimTable.")


def insert_staff_school():
    """
    What this function does:
    - Assigns Each Staff a School and Employment Type
    - Randomly Decides if They are Teaching or Non-Teaching (One, not both)
    - Generates a Random Start Date (Within the last 10 years)
    - 20% Chance of an until_date (Indicating they left)
    - 50% of Those Who Left Get Reassigned to a New School with a New Start Date
    """
    cursor.execute("SELECT staff_id FROM StaffDim")
    staff_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT school_id FROM SchoolDim")
    school_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT employment_type_id FROM EmploymentTypeDim")
    employment_type_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT subject_id FROM SubjectDim")
    subject_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT role_id FROM NonTeachingRoleDim")
    non_teaching_role_ids = [row[0] for row in cursor.fetchall()]

    staff_who_left = []
    data_to_insert = []

    for staff_id in staff_ids:
        school_id = random.choice(school_ids)
        employment_type_id = random.choice(employment_type_ids)

        if random.choice([True, False]):  # 50% chance
            subject_id = random.choice(subject_ids)
            non_teaching_role_id = None
        else:
            subject_id = None
            non_teaching_role_id = random.choice(non_teaching_role_ids)

        date_started = fake.date_between(start_date="-25y", end_date="today") # 25 because 25 years ago, mom debuted as math teacher in fggc umuahia

        # Randomly decide if the staff has an "until_date" (left the school)
        until_date = None
        if random.random() < 0.2:  # 20% chance the staff has left
            until_date = fake.date_between(start_date=date_started, end_date="today")
            staff_who_left.append(staff_id)

        data_to_insert.append((staff_id, school_id, employment_type_id, subject_id, non_teaching_role_id, date_started, until_date))

    cursor.executemany("""
        INSERT INTO StaffSchoolFact (staff_id, school_id, employment_type_id, subject_id, non_teaching_role_id, date_started, until_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data_to_insert)

    conn.commit()

    # Handle transfers (re-insert some staff who left into a new school)
    data_to_insert = []

    for staff_id in staff_who_left:
        if random.random() < 0.5:  # 50% chance of getting reassigned
            new_school_id = random.choice([s for s in school_ids if s != school_id])  # Ensure new school
            employment_type_id = random.choice(employment_type_ids)

            if random.choice([True, False]):
                subject_id = random.choice(subject_ids)
                non_teaching_role_id = None
            else:
                subject_id = None
                non_teaching_role_id = random.choice(non_teaching_role_ids)

            date_started = fake.date_between(start_date=until_date, end_date="today")
            until_date = None  # New employment doesn't have an end date

            data_to_insert.append((staff_id, new_school_id, employment_type_id, subject_id, non_teaching_role_id, date_started, until_date))

    # Insert transferred staff
    if data_to_insert:
        cursor.executemany("""
            INSERT INTO StaffSchoolFact (staff_id, school_id, employment_type_id, subject_id, non_teaching_role_id, date_started, until_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data_to_insert)

        conn.commit()


def insert_student(how_many):
    for _ in range(how_many):

        gender = random.choice(["M", "F"])
        if gender == "M":
            first_name = fake.male_name()
            middle_name = fake.first_name_male() 
        else:
            first_name = fake.female_name()
            middle_name = fake.first_name_female() 

        last_name = fake.surname()
        date_of_birth = fake.date_of_birth(minimum_age=9, maximum_age=16).strftime("%Y-%m-%d")

        state_id = random.randint(1,37)

        query = """
        INSERT INTO StudentDim (first_name, middle_name, last_name, date_of_birth, gender, state_id)
        VALUES (?,?,?,?,?,?)
        """
        cursor.execute(query, (first_name, middle_name, last_name, date_of_birth, gender, state_id))

    conn.commit()
    print(f"Successfully inserted {how_many} student records into StudentDim.")













insert_staff(10)
insert_staff_school()
insert_student(80)

# Close connection
cursor.close()
conn.close()