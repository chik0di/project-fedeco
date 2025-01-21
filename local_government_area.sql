CREATE TABLE [dbo].[local_government_area]
(
	[id] INT NOT NULL PRIMARY KEY, 
    [local_government] NCHAR(90) NOT NULL, 
    [state_id] INT NOT NULL
    CONSTRAINT [FK_local_government_area_state] FOREIGN KEY ([state_id]) REFERENCES [state]([id])
)
