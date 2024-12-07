CREATE TABLE [dbo].[hostel]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [name] VARCHAR(50) NOT NULL, 
    [hostel_master] VARCHAR(30) NOT NULL, 
    CONSTRAINT [FK_hostel_staff] FOREIGN KEY ([hostel_master]) REFERENCES [staff]([staff_id])
)
