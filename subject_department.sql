﻿CREATE TABLE [dbo].[subject_department]
(
	[id] INT NOT NULL PRIMARY KEY IDENTITY(1, 1), 
    [name] VARCHAR(50) UNIQUE NOT NULL
)