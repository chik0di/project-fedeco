CREATE TABLE [dbo].[StaffDim]
(
	[record_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [staff_id] UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL UNIQUE,
    [first_name] VARCHAR(50) NOT NULL, 
    [middle_name] VARCHAR(50) NOT NULL,
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(1) NOT NULL, 
    [state_id] INT NULL,
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(70) UNIQUE NOT NULL
    CONSTRAINT [FK_StaffDim_DimState] FOREIGN KEY (state_id) REFERENCES [StateDim]([id])
)
