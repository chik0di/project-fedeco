CREATE TABLE [dbo].[StaffSchoolFact]
(
	[staff_id] INT NOT NULL PRIMARY KEY, 
    [school_id] NCHAR(10) NOT NULL,
	[date_started] DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    [date_left] DATE NULL
)
