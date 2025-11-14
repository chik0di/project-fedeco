CREATE TABLE [warehouse].[AcademicYearDim]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [session] NCHAR(10) UNIQUE NOT NULL, 
    [start_date] DATE NOT NULL, 
    [end_date] DATE NOT NULL
)
