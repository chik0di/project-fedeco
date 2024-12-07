CREATE TABLE [dbo].[student]
(
	[id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [date_of_enrolment] DATE NOT NULL, 
    [hostel_id] INT NOT NULL, 
    [guardian] VARCHAR(30) NOT NULL, 
    CONSTRAINT [FK_student_staff] FOREIGN KEY ([guardian]) REFERENCES [staff]([staff_id]), 
    CONSTRAINT [FK_student_hostel] FOREIGN KEY ([hostel_id]) REFERENCES [hostel]([id])
)
