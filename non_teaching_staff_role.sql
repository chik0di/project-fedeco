CREATE TABLE [dbo].[non_teaching_staff_role]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [name] VARCHAR(50) UNIQUE NOT NULL
)
