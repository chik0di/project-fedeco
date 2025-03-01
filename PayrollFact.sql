CREATE TABLE [dbo].[PayrollFact]
(
	[staff_id] INT NOT NULL, 
    [school_id] NCHAR(10) NOT NULL,
	[level] INT,
	[salary] FLOAT
)