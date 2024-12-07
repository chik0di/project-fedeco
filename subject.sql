CREATE TABLE [dbo].[subject]
(
	[subject_id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [name] VARCHAR(50) NOT NULL, 
    [subject_department_id] INT NOT NULL,
    CONSTRAINT [FK_subject_department_id] FOREIGN KEY ([subject_department_id]) REFERENCES [subject_department]([id])
)
