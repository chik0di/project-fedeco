CREATE TABLE [dbo].[StudentDim]
(   
    [record_id] INT PRIMARY KEY IDENTITY(1,1),
	[student_id] UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL UNIQUE, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL,
    [gender] NCHAR(1) NOT NULL,
    [state_of_origin] INT NULL
    CONSTRAINT [FK_DimStudent_DimState] FOREIGN KEY (state_of_origin) REFERENCES [StateDim]([id])

)
