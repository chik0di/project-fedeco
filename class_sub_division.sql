CREATE TABLE [dbo].[class_sub_division]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [class_id] INT NOT NULL, 
    [division] NCHAR(10) NOT NULL
)
