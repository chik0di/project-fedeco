CREATE TABLE [dbo].[StateDim]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [state] NCHAR(50) NOT NULL, 
    [capital] NCHAR(50) NOT NULL
)