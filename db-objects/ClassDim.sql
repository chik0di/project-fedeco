CREATE TABLE [warehouse].[ClassDim]
(
	[class_id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
	[class_full] VARCHAR(50) UNIQUE NOT NULL,
    [class] NCHAR(5) UNIQUE NOT NULL
)