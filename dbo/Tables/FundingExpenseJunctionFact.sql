CREATE TABLE [dbo].[FundingExpenseJunctionFact]
(
	[Id] INT NOT NULL PRIMARY KEY, 
    [school_funding_id] INT NOT NULL,
	[expense_category_id] INT NOT NULL, 
    [amount_spent] DECIMAL NOT NULL, 
)