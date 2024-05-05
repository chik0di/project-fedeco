CREATE TABLE [dbo].[teaching_staff]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [first_name] VARCHAR(50) NOT NULL, 
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(10) NOT NULL, 
    [subject_id] INT NOT NULL, 
    [date_started] DATE NOT NULL, 
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(50) NOT NULL UNIQUE, 
    CONSTRAINT [FK_subject_id] FOREIGN KEY ([subject_id]) REFERENCES [subject]([id]) 
)
