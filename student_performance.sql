CREATE TABLE [dbo].[student_performance]
    (
	[id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
    [student_id] VARCHAR(30) NOT NULL, 
    [class_division_id] INT NOT NULL, 
    [term_id] INT NOT NULL, 
    [subject_id] INT NOT NULL, 
    [first_ca] INT NOT NULL, 
    [second_ca] INT NOT NULL, 
    [exam] INT NOT NULL
    CONSTRAINT [CK_student_performance_first_ca] CHECK (first_ca BETWEEN 0 AND 30), 
    CONSTRAINT [CK_student_performance_second_ca] CHECK (second_ca BETWEEN 0 AND 30), 
    CONSTRAINT [CK_student_performance_exam] CHECK (exam BETWEEN 0 AND 70), 
    CONSTRAINT [FK_student_performance_student] FOREIGN KEY ([student_id]) REFERENCES [student]([student_id]), 
    CONSTRAINT [FK_student_performance_term] FOREIGN KEY ([term_id]) REFERENCES [term]([term_id]), 
    CONSTRAINT [FK_student_performance_class_division] FOREIGN KEY ([class_division_id]) REFERENCES [class_sub_division]([id]), 
    CONSTRAINT [FK_student_performance_subject] FOREIGN KEY ([subject_id]) REFERENCES [subject]([subject_id])
    )