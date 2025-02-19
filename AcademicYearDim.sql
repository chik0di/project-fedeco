CREATE TABLE [dbo].[AcademicYearDim]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [session] NCHAR(10) UNIQUE NOT NULL
)
