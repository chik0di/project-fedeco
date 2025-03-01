CREATE TABLE [dbo].[StaffSchoolFact]
(
	[staff_id] INT NOT NULL, 
    [school_id] NCHAR(10) NOT NULL,
	[employment_type_id] INT NOT NULL,
	[subject_id] INT NULL,
	[non_teaching_role_id] INT NULL,
	[date_started] DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    [until_date] DATE NULL,
	CONSTRAINT [FK_subject_id] FOREIGN KEY ([subject_id]) REFERENCES [SubjectDim]([subject_id]),
	CONSTRAINT [FK_non_teaching_role_id] FOREIGN KEY ([non_teaching_role_id]) REFERENCES [NonTeachingDim]([id])
)
