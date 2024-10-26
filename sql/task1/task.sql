WITH RankedSalaries AS (
    SELECT 
        Department.name AS Department,
        Employee.name AS Employee,
        Employee.salary AS Salary,
        RANK() OVER (PARTITION BY Department.name ORDER BY Employee.salary DESC) AS SalaryRank
    FROM 
        Employee 
        INNER JOIN Department ON Employee.departmentId = Department.id
)
SELECT 
    Department,
    Employee,
    Salary
FROM 
    RankedSalaries
WHERE 
    SalaryRank = 1;