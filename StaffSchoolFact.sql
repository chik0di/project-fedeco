CREATE TABLE [dbo].[StaffSchoolFact]
(
	[staff_id] INT NOT NULL, 
    [school_id] NCHAR(10) NOT NULL,
	[employment_type_id] INT NOT NULL,
	[subject_id] INT NULL,
	[non_teaching_role_id] INT NULL,
	[hire_date] DATE NOT NULL,
    [until_date] DATE NULL,
	[created_at] DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
	CONSTRAINT [FK_subject_id] FOREIGN KEY ([subject_id]) REFERENCES [SubjectDim]([subject_id]),
	CONSTRAINT [FK_non_teaching_role_id] FOREIGN KEY ([non_teaching_role_id]) REFERENCES [NonTeachingDim]([id])
)
