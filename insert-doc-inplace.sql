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
name
)
VALUES
('Languages'), ('Sciences'), ('Commercial'),
('Arts'), ('Vocational'), ('Engineering');


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