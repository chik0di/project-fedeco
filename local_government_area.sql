CREATE TABLE [dbo].[local_government_area]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [local_government] NCHAR(90) NOT NULL, 
    [state] NCHAR(50) NOT NULL
)
