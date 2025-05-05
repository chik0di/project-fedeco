CREATE TABLE [dbo].[StudentDim]
(   
    [record_id] INT PRIMARY KEY IDENTITY(1,1),
	[student_id] UNIQUEIDENTIFIER DEFAULT NEWID() NOT NULL UNIQUE, 
    [first_name] NCHAR(90) NOT NULL, 
    [middle_name] NCHAR(70) NOT NULL, 
    [last_name] NCHAR(90) NOT NULL, 
    [date_of_birth] DATE NOT NULL,
    [gender] NCHAR(1) NOT NULL,
    [address] TEXT NOT NULL,
    [state_of_origin] INT NOT NULL,
    [sponsor_name] VARCHAR(50) NOT NULL,
    [sponsor_phone] VARCHAR(11) NOT NULL,
    [sponsor_address] TEXT,
    [sponsor_email_address] VARCHAR(30),
    [additional_notes] TEXT
    CONSTRAINT [FK_DimStudent_DimState] FOREIGN KEY (state_of_origin) REFERENCES [StateDim]([id])

)
