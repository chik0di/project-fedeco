-----------------------------------------------
------INSERTING VALUES INTO THE TermDim TABLE-----
-----------------------------------------------
INSERT INTO TermDim (term)
VALUES  ('First'), ('Second'), ('Third');


-----------------------------------------------
-----INSERTING VALUES INTO THE ClassDim TABLE-----
-----------------------------------------------
INSERT INTO ClassDim (class_full, class)
VALUES  ('Junior Secondary School 1','JSS1'), ('Junior Secondary School 2','JSS2'), ('Junior Secondary School 3', 'JSS3'),
        ('Senior Secondary School 1', 'SSS1'), ('Senior Secondary School 2', 'SSS2'), ('Senior Secondary School 3', 'SSS3');


-------------------------------------------------------------------
---- INSERTING VALUES INTO THE [NonTeachingDim] TABLE ----
-------------------------------------------------------------------
INSERT INTO [NonTeachingDim]  
	( 
		[name]
		)
VALUES	
	('Librarian'), ('Registrar'), ('Laboratory Technician and Assistant'), ('Guidance Counselor'), ('ICT Support Staff'), ('Examination Officer'), 
  ('Records Officer'), ('Kitchen'), ('Security'), ('Utility'), ('Cleaning'), ('Office Assistant'), ('Driver'), ('Electrician');


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

INSERT INTO [subject]
(
[name], [SubjectDepartmentDim_id]
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

-------------------------------------------------------------------------
------- INSERTING VALUES INTO THE [administrative_roles] TABLE ----------
-------------------------------------------------------------------------

INSERT INTO [administrative_roles]
	(
		[name]
		)
VALUES 
	('Principal'),
	('Vice Principal (Administration)'),
	('Vice Principal (Academics)'),
	('Vice Principal (Special Duties)'),
	('PTA Executive'),
	('Head of Department');