CREATE TABLE [warehouse].[SubjectDim]
(
	[subject_id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [name] VARCHAR(50) NOT NULL, 
    [subject_department_id] INT NOT NULL,
)
