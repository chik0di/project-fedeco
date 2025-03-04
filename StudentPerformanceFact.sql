CREATE TABLE [dbo].[StudentPerformanceFact]
    (
	[id] INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
    [student_id] VARCHAR(30) NOT NULL, 
    [class_id] INT NOT NULL, 
    [term_id] INT NOT NULL, 
    [subject_id] INT NOT NULL, 
    [first_ca] INT NOT NULL, 
    [second_ca] INT NOT NULL, 
    [exam] INT NOT NULL
    -- CONSTRAINT [CK_student_performance_first_ca] CHECK (first_ca BETWEEN 0 AND 30), 
    -- CONSTRAINT [CK_student_performance_second_ca] CHECK (second_ca BETWEEN 0 AND 30), 
    -- CONSTRAINT [CK_student_performance_exam] CHECK (exam BETWEEN 0 AND 70), 
    CONSTRAINT [FK_student_performance_student] FOREIGN KEY ([student_id]) REFERENCES [StudentDim]([student_id]), 
    CONSTRAINT [FK_student_performance_term] FOREIGN KEY ([term_id]) REFERENCES [TermDim]([term_id]), 
    CONSTRAINT [FK_student_performance_class] FOREIGN KEY ([class_id]) REFERENCES [ClassDim]([class_id]), 
    CONSTRAINT [FK_student_performance_subject] FOREIGN KEY ([subject_id]) REFERENCES [SubjectDim]([subject_id])
    )