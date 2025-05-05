CREATE TABLE [dbo].[SubjectDepartmentDim]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [name] VARCHAR(50) UNIQUE NOT NULL
)