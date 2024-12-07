-----------------------------------------------
------INSERTING VALUES INTO THE TERM TABLE-----
-----------------------------------------------
INSERT INTO term (term)
VALUES  ('1st'), 
		('2nd'),
		('3rd');


-----------------------------------------------
-----INSERTING VALUES INTO THE CLASS TABLE-----
-----------------------------------------------
INSERT INTO class (class)
VALUES  ('JS1'), ('JS2'), ('JS3'),
		('SS1'), ('SS2'), ('SS3');


-------------------------------------------------------------------
---- INSERTING VALUES INTO THE [non_teaching_staff_role] TABLE ----
-------------------------------------------------------------------
INSERT INTO [non_teaching_staff_role] 
	( 
		[name]
		)
VALUES	
	('Librarian'), ('Registrar'), ('Laboratory Technician and Assistant'), ('Guidance Counselor'), 
	('ICT Support Staff'), ('Examination Officer'), ('Records Officer');


--------------------------------------------------------------
-----INSERTING VALUES INTO THE [subject_department] TABLE-----
--------------------------------------------------------------

INSERT INTO subject_department
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
[name], [subject_department_id]
)
VALUES  
	('English Language', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('Literature-in-English', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('French', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('Igbo', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('Yoruba', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('Hausa', (SELECT id FROM subject_department WHERE name = 'Languages')),
	('Further Mathematics', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Mathematics', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Physics', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Chemistry', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Biology', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Computer Science', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Agricultural Science', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Basic Science', (SELECT id FROM subject_department WHERE name = 'Sciences')),
	('Commerce', (SELECT id FROM subject_department WHERE name = 'Commercial')),
	('Financial Accounting', (SELECT id FROM subject_department WHERE name = 'Commercial')),
	('Economics', (SELECT id FROM subject_department WHERE name = 'Commercial')),
	('Business Studies', (SELECT id FROM subject_department WHERE name = 'Commercial')),
	('Civic Education', (SELECT id FROM subject_department WHERE name = 'Social Sciences')),
	('Religious Studies', (SELECT id FROM subject_department WHERE name = 'Social Sciences')),
	('Government', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Geography', (SELECT id FROM subject_department WHERE name = 'Social Sciences')),
	('Social Studies', (SELECT id FROM subject_department WHERE name = 'Social Sciences')),
	('History', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Theatre Arts/Drama', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Fine Arts/Visual Arts', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Music', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Creative Writing', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Cultural and Creative Arts (CCA)', (SELECT id FROM subject_department WHERE name = 'Arts')),
	('Food and Nutrition', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Home Economics', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Home Management', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Data Processing', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Clothing and Textiles', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Typing and Shorthand', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Carpentry and Woodwork', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Entrepreneurship Studies', (SELECT id FROM subject_department WHERE name = 'Vocational')),
	('Basic Technology', (SELECT id FROM subject_department WHERE name = 'Engneering')),
	('Technical Drawing', (SELECT id FROM subject_department WHERE name = 'Engneering'))
;

-------------------------------------------------------------------------
-----INSERTING VALUES INTO THE [non_academic_staff_department] TABLE-----
-------------------------------------------------------------------------

INSERT INTO non_academic_staff_department
(
name
)
VALUES
('Kitchen'), ('Security'), ('Utility'), ('PTA Member'),
('Cleaning'), ('Office Assistant'), ('Driver'), ('Electrician');


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