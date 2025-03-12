CREATE TABLE [dbo].[StudentSchoolFact]
(
	[record_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [student_id] UNIQUEIDENTIFIER NOT NULL,
    [school_id] INT NOT NULL,
	[academic_year_of_admission] INT NOT NULL,
    [academic_year_finished] INT NULL,
    [class_admitted] INT NOT NULL,
    [student_type] VARCHAR(15) NOT NULL
    CONSTRAINT [FK_DimStudentSchool_DimAcademic_year_start] FOREIGN KEY ([academic_year_of_admission]) REFERENCES [AcademicYearDim]([id]),
    CONSTRAINT [FK_DimStudentSchool_DimAcademic_year_finish] FOREIGN KEY ([academic_year_of_admission]) REFERENCES [AcademicYearDim]([id]),
    CONSTRAINT [FK_DimStudentSchool_DimClass] FOREIGN KEY (class_admitted) REFERENCES [ClassDim]([class_id])
)
