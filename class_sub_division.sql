CREATE TABLE [dbo].[class_sub_division]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [class_id] INT NOT NULL, 
    [division] NCHAR(10) NOT NULL, 
    CONSTRAINT [FK_class_sub_division_class] FOREIGN KEY ([class_id]) REFERENCES [class]([class_id])
)
