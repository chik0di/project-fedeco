CREATE TABLE [dbo].[school]
(
	[school_id] INT NOT NULL PRIMARY KEY, 
    [name] NCHAR(131) NOT NULL, 
    [school_code] VARCHAR(50) NOT NULL UNIQUE, 
    [address] NCHAR(121) NOT NULL,
    [zipcode] INT NOT NULL,
    [local_government_area_id] INT NOT NULL,
    [state_id] INT NOT NULL,
    [school_website] NCHAR(196) NULL UNIQUE,
    [email_address] NCHAR(127) NOT NULL UNIQUE,
    [year_established] INT NOT NULL,
    CONSTRAINT [FK_school_state] FOREIGN KEY ([state_id]) REFERENCES [state]([id]), 
    CONSTRAINT [CK_school_years_valid] CHECK (year_established >= 1963 AND year_established <= YEAR(GETDATE()))
)
