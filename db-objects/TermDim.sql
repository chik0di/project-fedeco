CREATE TABLE [dbo].[TermDim]
(
	[term_id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [term] NCHAR(10) UNIQUE NOT NULL
)
