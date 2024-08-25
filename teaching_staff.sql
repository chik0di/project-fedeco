CREATE TABLE [dbo].[teaching_staff]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [first_name] VARCHAR(50) NOT NULL, 
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(15) NOT NULL, 
    [subject_id] INT NOT NULL, 
    [date_started] DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(70) NOT NULL UNIQUE, 
    [additional_role] VARCHAR(70) NULL, 
    CONSTRAINT [FK_subject_id] FOREIGN KEY ([subject_id]) REFERENCES [subject]([id])
)
