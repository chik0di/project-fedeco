CREATE TABLE [dbo].[non_academic_staff_member] (
    [id]                               INT          NOT NULL,
    [staff_id]                         VARCHAR (50) NOT NULL,
    [non_academic_staff_department_id] INT          NOT NULL,
    [date_started]                     DATE         NOT NULL,
    PRIMARY KEY CLUSTERED ([id] ASC),
    CONSTRAINT [FK_non_academic_staff_department_id] FOREIGN KEY ([non_academic_staff_department_id]) REFERENCES [dbo].[non_academic_staff_department] ([id])
);