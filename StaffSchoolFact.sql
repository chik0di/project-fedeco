CREATE TABLE [dbo].[StaffSchoolFact]
(
	[staff_id] INT NOT NULL, 
    [school_id] NCHAR(10) NOT NULL,
	[employment_type_id] INT NOT NULL,
	[date_started] DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    [date_left] DATE NULL
)
