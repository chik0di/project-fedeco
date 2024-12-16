CREATE TABLE [dbo].[academic_year]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [session] NCHAR(10) UNIQUE NOT NULL
)
