CREATE TABLE [warehouse].[StateDim]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [state] NCHAR(50) NOT NULL UNIQUE, 
    [capital] NCHAR(50) NOT NULL,
    [geo_political_zone] VARCHAR(20) NOT NULL
)