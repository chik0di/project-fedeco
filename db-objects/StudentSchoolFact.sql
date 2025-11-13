CREATE TABLE [dbo].[StudentSchoolFact]
(
	[record_id] INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
    [student_id] UNIQUEIDENTIFIER NOT NULL,
    [school_id] INT NOT NULL,
    [enrolment_date] DATE NOT NULL,
	[academic_year_of_admission] INT NOT NULL,
    [status] NCHAR(14) NOT NULL CHECK(status IN('Active', 'Graduated', 'Transferred', 'Dropped')) DEFAULT 'Active',
    [class_admitted] INT NOT NULL,
    [student_type] VARCHAR(6) NOT NULL CHECK(student_type IN('Day', 'Boarder')),
    [created_at] DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
    [updated_at] DATETIME NULL
    CONSTRAINT [FK_DimStudentSchool_DimAcademic_year_start] FOREIGN KEY ([academic_year_of_admission]) REFERENCES [AcademicYearDim]([id]),
    CONSTRAINT [FK_DimStudentSchool_DimClass] FOREIGN KEY (class_admitted) REFERENCES [ClassDim]([class_id])
)
