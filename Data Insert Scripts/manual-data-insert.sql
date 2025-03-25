-----------------------------------------------
------INSERTING VALUES INTO THE AcademicYearDim TABLE-----
-----------------------------------------------
DECLARE @startYear INT = 1980;
DECLARE @endYear INT = 2025;

WHILE @startYear < @endYear
BEGIN
    INSERT INTO AcademicYearDim (session, start_date, end_date)
    VALUES (
        CAST(@startYear AS VARCHAR) + '/' + CAST(@startYear + 1 AS VARCHAR), 
        CAST(@startYear AS VARCHAR) + '-09-01', 
        CAST(@startYear + 1 AS VARCHAR) + '-07-31' 
    );

    SET @startYear = @startYear + 1;
END;


-----------------------------------------------
-----INSERTING VALUES INTO THE ClassDim TABLE-----
-----------------------------------------------
INSERT INTO ClassDim (class_full, class)
VALUES  ('Junior Secondary School, One','JSS1'), ('Junior Secondary School, Two','JSS2'), ('Junior Secondary School, Three', 'JSS3'),
        ('Senior Secondary School, One', 'SSS1'), ('Senior Secondary School, Two', 'SSS2'), ('Senior Secondary School, Three', 'SSS3');



-------------------------------------------------------------------------
------- INSERTING VALUES INTO THE [EmploymentTypeDim] TABLE ----------
-------------------------------------------------------------------------

INSERT INTO [EmploymentTypeDim]
	(
		[id], [employment_type]
		)
VALUES 
	(1, 'Federal Worker'),
	(2, 'School Employee'),
	(3, 'PTA Staff');


-------------------------------------------------------------------------
------- INSERTING VALUES INTO THE [ExpenseCategoryDim] TABLE ----------
-------------------------------------------------------------------------

INSERT INTO [ExpenseCategoryDim]
	(
		[expense_category]
		)
VALUES 
	('Infrastructure'),
	('Salary'),
	('Research'),
  ('Maintenance'),
  ('Equipment');



-------------------------------------------------------------------------
------- INSERTING VALUES INTO THE [FundingSourceDim] TABLE ----------
-------------------------------------------------------------------------

INSERT INTO FundingSourceDim (funding_id, funding_name, category) VALUES
(1, 'Federal Budget Allocation', 'Government Funding'),
(2, 'State/Regional Government Grants', 'Government Funding'),
(3, 'Local Government Funding', 'Government Funding'),
(4, 'Education Trust Funds', 'Government Funding'),
(5, 'Subsidies & Tax Rebates', 'Government Funding'),

(6, 'Private Donations', 'Private & Corporate Funding'),
(7, 'Corporate Sponsorships', 'Private & Corporate Funding'),
(8, 'Endowments & Trusts', 'Private & Corporate Funding'),
(9, 'Alumni Contributions', 'Private & Corporate Funding'),
(10, 'Religious Organization Support', 'Private & Corporate Funding'),
(11, 'School-Based Enterprises', 'Private & Corporate Funding'),
(12, 'Parent-Teacher Association (PTA) Contributions', 'Private & Corporate Funding'),

(13, 'National Research Grants', 'Research & Grants'),
(14, 'International Education Grants', 'Research & Grants'),
(15, 'NGO & Nonprofit Grants', 'Research & Grants'),
(16, 'Tech & Innovation Grants', 'Research & Grants'),

(17, 'Tuition & Fees', 'Internally Generated Revenue (IGR)'),
(18, 'Facility Rentals', 'Internally Generated Revenue (IGR)'),
(19, 'Boarding & Accommodation Fees', 'Internally Generated Revenue (IGR)'),
(20, 'Textbook & Learning Material Sales', 'Internally Generated Revenue (IGR)'),
(21, 'Training & Certification Courses', 'Internally Generated Revenue (IGR)'),
(22, 'Consultancy Services', 'Internally Generated Revenue (IGR)'),

(23, 'Bilateral Education Aid', 'International & Foreign Aid'),
(24, 'UN & Global Education Initiatives', 'International & Foreign Aid'),
(25, 'World Bank & IMF Education Loans', 'International & Foreign Aid'),
(26, 'Scholarship & Exchange Programs', 'International & Foreign Aid'),

(27, 'Disaster Recovery Funds', 'Special Purpose Funds'),
(28, 'Sports & Cultural Grants', 'Special Purpose Funds'),
(29, 'Special Needs Education Funds', 'Special Purpose Funds'),
(30, 'Technology Infrastructure Grants', 'Special Purpose Funds');




-------------------------------------------------------------------
---- INSERTING VALUES INTO THE [NonTeachingDim] TABLE ----
-------------------------------------------------------------------
INSERT INTO [NonTeachingDim]
	( 
		[name]
		)
VALUES	
	('Librarian'), ('Registrar'), ('Laboratory Technician and Assistant'), ('Guidance Counselor'), ('ICT Support Staff'), ('Examination Officer'), 
  ('Records Officer'), ('Kitchen Staff'), ('Security Staff'), ('Utility'), ('Cleaning Staff'), ('Office Assistant'), ('Driver'), ('Electrician'), ('Vice Principal (Administration)'), 
  ('Vice Principal (Academics)'),	('Vice Principal (Special Duties)'), ('Principal');


--------------------------------------------------------------
-----INSERTING VALUES INTO THE [SubjectDepartmentDim] TABLE-----
--------------------------------------------------------------

INSERT INTO SubjectDepartmentDim
(
[name]
)
VALUES
('Languages'), ('Sciences'), ('Commercial'), ('Social Sciences'),
('Arts'), ('Vocational'), ('Engineering');


--------------------------------------------------------------
-----INSERTING VALUES INTO THE [subject] TABLE-----
--------------------------------------------------------------

INSERT INTO [SubjectDim]
(
[name], [subject_department_id]
)
VALUES  
	('English Language', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('Literature-in-English', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('French', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('Igbo', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('Yoruba', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('Hausa', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Languages')),
	('Further Mathematics', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Mathematics', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Physics', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Chemistry', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Biology', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Computer Science', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Agricultural Science', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Basic Science', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Sciences')),
	('Commerce', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Commercial')),
	('Financial Accounting', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Commercial')),
	('Economics', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Commercial')),
	('Business Studies', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Commercial')),
	('Civic Education', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Social Sciences')),
	('Religious Studies', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Social Sciences')),
	('Government', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Geography', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Social Sciences')),
	('Social Studies', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Social Sciences')),
	('History', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Theatre Arts/Drama', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Fine Arts/Visual Arts', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Music', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Creative Writing', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Cultural and Creative Arts (CCA)', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Arts')),
	('Food and Nutrition', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Home Economics', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Home Management', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Data Processing', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Clothing and Textiles', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Typing and Shorthand', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Carpentry and Woodwork', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Entrepreneurship Studies', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Vocational')),
	('Basic Technology', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Engneering')),
	('Technical Drawing', (SELECT id FROM SubjectDepartmentDim WHERE name = 'Engneering'))
;


---------------------------------------------------
------INSERTING VALUES INTO THE TermDim TABLE-----
---------------------------------------------------
INSERT INTO TermDim (term)
VALUES  ('First'), ('Second'), ('Third');
