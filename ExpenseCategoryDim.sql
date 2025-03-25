CREATE TABLE [dbo].[ExpenseCategoryDim]
(
	[expense_category_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [expense_category] NCHAR(90) NOT NULL UNIQUE
)