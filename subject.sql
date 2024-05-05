CREATE TABLE [dbo].[subject]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [name] VARCHAR(50) NOT NULL, 
    [subject_department_id] INT NOT NULL,
    CONSTRAINT [FK_subject_department_id] FOREIGN KEY ([subject_department_id]) REFERENCES [subject_department]([id])
)
