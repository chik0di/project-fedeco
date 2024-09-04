CREATE TABLE [dbo].[non_academic_staff]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [staff_id] VARCHAR(50) NOT NULL, 
    [non_academic_staff_department_id] INT NOT NULL, 
    [date_started] DATE NOT NULL, 
    CONSTRAINT [FK_non_academic_staff_department_id] FOREIGN KEY ([non_academic_staff_department_id]) REFERENCES [non_academic_staff_department]([id])
)

GO
