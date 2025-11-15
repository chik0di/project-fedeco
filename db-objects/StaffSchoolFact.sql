CREATE TABLE [warehouse].[StaffSchoolFact]
(
	[record_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1),
	[staff_id] INT NOT NULL, 
    [school_id] NCHAR(10) NOT NULL,
	[employment_type_id] INT NOT NULL,
	[subject_id] INT NULL,
	[non_teaching_role_id] INT NULL,
	[hire_date] DATE NOT NULL,
    [until_date] DATE NULL,
	[created_at] DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	[updated_at] DATETIME NULL
	)
