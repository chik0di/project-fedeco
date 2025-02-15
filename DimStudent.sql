CREATE TABLE [dbo].[DimStudent]
(
	[student_id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [academic_year_of_admission] NCHAR(10) NOT NULL,
    [state_of_origin] NCHAR(90) NULL, 
    CONSTRAINT [FK_student_academic_year] FOREIGN KEY ([academic_year_of_admission]) REFERENCES [DimAcademicYear]([session])
)
