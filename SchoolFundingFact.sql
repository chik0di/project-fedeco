CREATE TABLE [dbo].[SchoolFundingFact]
(
	[school_funding_id] INT NOT NULL PRIMARY KEY, 
    [school_id] NCHAR(10) NOT NULL, 
    [funding_title] NCHAR(90) NOT NULL,
    [funding_type] NCHAR(20) NOT NULL CHECK(funding_type IN('Government Funding', '')),
    [amount_allocated] DECIMAL NOT NULL, 
    [date_allocated] DATE NULL
)
