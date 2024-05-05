CREATE TABLE [dbo].[non_academic_staff_member]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [first_name] VARCHAR(50) NOT NULL, 
    [last_name] VARCHAR(50) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [gender] NCHAR(10) NOT NULL, 
    [non_academic_staff_department_id] INT NOT NULL, 
    [date_started] DATE NOT NULL, 
    [phone_number] INT NOT NULL, 
    [email_address] VARCHAR(50) NOT NULL UNIQUE, 
    CONSTRAINT [FK_non_academic_staff_department_id] FOREIGN KEY ([non_academic_staff_department_id]) REFERENCES [non_academic_staff_department]([id])
)

GO
EXEC sp_addextendedproperty @name = N'MS_Description',
    @value = N'non academic staff email address',
    @level0type = N'SCHEMA',
    @level0name = N'dbo',
    @level1type = N'TABLE',
    @level1name = N'non_academic_staff_member',
    @level2type = N'COLUMN',
    @level2name = N'email_address'