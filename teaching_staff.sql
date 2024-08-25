CREATE TABLE [dbo].[teaching_staff]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [staff_id] VARCHAR(30) NOT NULL, 
    [subject_id] INT NOT NULL, 
    [date_started] DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    CONSTRAINT [FK_subject_id] FOREIGN KEY ([subject_id]) REFERENCES [subject]([id])    
)