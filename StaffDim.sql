CREATE TABLE [dbo].[StaffDim]
(
	[record_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [staff_id] UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL UNIQUE,
    [first_name] VARCHAR(50) NOT NULL, 
    [middle_name] VARCHAR(50) NOT NULL,
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(1) NOT NULL,
    [address] TEXT NOT NULL,
    [state_of_origin] INT NOT NULL,
    [phone_number] NCHAR(11) NOT NULL, 
    [email_address] VARCHAR(30) UNIQUE NOT NULL,
    [additional_notes] TEXT
    CONSTRAINT [FK_StaffDim_DimState] FOREIGN KEY (state_of_origin) REFERENCES [StateDim]([id])
)