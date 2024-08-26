CREATE TABLE [dbo].[non_teaching_staff]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [staff_id] VARCHAR(30) NOT NULL, 
    [role_id] INT NOT NULL, 
    [date_started] DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    CONSTRAINT [FK_non_teaching_staff_department_id] FOREIGN KEY ([role_id]) REFERENCES [non_teaching_staff_role]([id])
)
