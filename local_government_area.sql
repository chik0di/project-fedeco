CREATE TABLE [dbo].[local_government_area]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [local_government] NCHAR(90) NOT NULL, 
    [state] NCHAR(50) NOT NULL, 
    CONSTRAINT [FK_local_government_area_state] FOREIGN KEY ([state]) REFERENCES [state]([state])
)
