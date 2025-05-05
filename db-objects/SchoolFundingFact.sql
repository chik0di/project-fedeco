CREATE TABLE [dbo].[SchoolFundingFact]
(
	[school_funding_id] INT NOT NULL PRIMARY KEY, 
    [school_id] NCHAR(10) NOT NULL, 
    [funding_source] NCHAR(90) NOT NULL, 
    [amount_allocated] DECIMAL NOT NULL, 
    [date_allocated] DATE NULL
)
