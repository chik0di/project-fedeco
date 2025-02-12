CREATE TABLE [dbo].[DimAcademicYear]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [session] NCHAR(10) UNIQUE NOT NULL
)
