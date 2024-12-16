CREATE TABLE [dbo].[student]
(
	[student_id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [academic_year_of_admission] NCHAR(10) NOT NULL,
    [student_type_id] INT NOT NULL, 
    [hostel_id] INT NOT NULL, 
    [guardian] VARCHAR(30) NULL
    CONSTRAINT [FK_student_staff] FOREIGN KEY ([guardian]) REFERENCES [staff]([staff_id]), 
    CONSTRAINT [FK_student_hostel] FOREIGN KEY ([hostel_id]) REFERENCES [hostel]([id]), 
    CONSTRAINT [FK_student_student_type] FOREIGN KEY ([student_type_id]) REFERENCES [student_type]([id]), 
    CONSTRAINT [FK_student_academic_year] FOREIGN KEY ([academic_year_of_admission]) REFERENCES [academic_year]([session])
)
