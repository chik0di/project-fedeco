-- Adjust accordingly to remove all the rows from a table and reset index so Auto-Increment refreshes

  DELETE FROM [fedeco].[dbo].[AcademicYearDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[AcademicYearDim]', RESEED, 0);

---------------

  DELETE FROM [fedeco].[dbo].[ClassDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[ClassDim]', RESEED, 0);


--------------
  DELETE FROM [fedeco].[dbo].[EmploymentTypeDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[EmploymentTypeDim]', RESEED, 0);

---------------

  DELETE FROM [fedeco].[dbo].[ExpenseCategoryDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[ExpenseCategoryDim]', RESEED, 0);

----------------
  DELETE FROM [fedeco].[dbo].[StaffDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[StaffDim]', RESEED, 0);

----------------
  DELETE FROM [fedeco].[dbo].[SubjectDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[SubjectDim]', RESEED, 0);

  ----------------
  DELETE FROM [fedeco].[dbo].[SubjectDepartmentDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[SubjectDepartmentDim]', RESEED, 0);

  ----------------

  DELETE FROM [fedeco].[dbo].[TermDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[TermDim]', RESEED, 0);

  ----------------

  DELETE FROM [fedeco].[dbo].[StateDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[StateDim]', RESEED, 0);

  ----------------

  DELETE FROM [fedeco].[dbo].[TermDim];

  DBCC CHECKIDENT ('[fedeco].[dbo].[TermDim]', RESEED, 0);