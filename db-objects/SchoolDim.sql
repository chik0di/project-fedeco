﻿CREATE TABLE [dbo].[SchoolDim]
(
	[school_id] INT NOT NULL PRIMARY KEY, 
    [full_name] NCHAR(131) NOT NULL, 
    [school_display] VARCHAR(50) NOT NULL, 
    [state] NCHAR(50) NOT NULL,
    [school_website] NCHAR(196) NULL, 
    CONSTRAINT [FK_SchoolDim_State] FOREIGN KEY ([state]) REFERENCES [StateDim]([state])

)