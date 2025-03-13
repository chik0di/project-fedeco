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

def insert_dummy_staff(num_records):
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

    # Commit transaction
    conn.commit()
    print(f"Successfully inserted {num_records} staff records into StaffDimTable.")



# Insert 100 dummy records
insert_dummy_staff(10)

# Close connection
cursor.close()
conn.close()