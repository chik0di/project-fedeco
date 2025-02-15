CREATE TABLE [dbo].[student_class]
(
	[student_id] VARCHAR(30) NOT NULL PRIMARY KEY, 
    [class_id] INT NOT NULL, 
    CONSTRAINT [FK_student_class_student] FOREIGN KEY ([student_id]) REFERENCES [student]([student_id]),
    CONSTRAINT [FK_student_class_class] FOREIGN KEY ([class_id]) REFERENCES [DimClass]([class_id])
)