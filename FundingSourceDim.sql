CREATE TABLE [dbo].[FundingSourceDim]
(
	[funding_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1),
	[funding_name] NCHAR(50) NOT NULL UNIQUE,
	[category] NCHAR(30) NOT NULL
)
