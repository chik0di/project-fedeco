CREATE TABLE [dbo].[non_teaching_staff]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [first_name] VARCHAR(50) NOT NULL, 
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(10) NOT NULL, 
    [non_teaching_staff_department_id] INT NOT NULL, 
    [date_started] DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(50) NOT NULL UNIQUE,
    [additional_role] VARCHAR(70) NULL, 
    CONSTRAINT [FK_non_teaching_staff_department_id] FOREIGN KEY ([non_teaching_staff_department_id]) REFERENCES [non_teaching_staff_department]([id])
)
