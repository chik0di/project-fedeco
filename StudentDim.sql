CREATE TABLE [dbo].[StudentDim]
(
	[student_id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL, 
    [state_of_origin] INT NULL
    CONSTRAINT [FK_DimStudent_DimState] FOREIGN KEY (state_of_origin) REFERENCES [StateDim]([id])

)
