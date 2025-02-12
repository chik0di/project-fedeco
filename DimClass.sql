CREATE TABLE [dbo].[DimClass]
(
	[class_id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [class] NCHAR(5) UNIQUE NOT NULL
)
