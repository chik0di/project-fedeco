CREATE TABLE [dbo].[StaffDim]
(
	[staff_id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [first_name] VARCHAR(50) NOT NULL, 
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(15) NOT NULL, 
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(70) UNIQUE NOT NULL
)
