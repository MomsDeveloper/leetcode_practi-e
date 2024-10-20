# 184. Department Highest Salary

**Difficulty:** Medium  
**Topics:** SQL, Pandas

## Table: Employee

| Column Name  | Type    |
|--------------|---------|
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |

- `id` is the primary key (a column with unique values) for this table.
- `departmentId` is a foreign key (reference column) that links to the `id` in the Department table.
- Each row of this table indicates the `id`, `name`, and `salary` of an employee. It also contains the `departmentId` for their department.

## Table: Department

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |

- `id` is the primary key (a column with unique values) for this table. 
- It is guaranteed that the department `name` is not NULL.
- Each row of this table indicates the `id` of a department and its `name`.

## Problem Statement

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

### Example

#### Input: 

**Employee table:**

| id | name  | salary | departmentId |
|----|-------|--------|--------------|
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |

**Department table:**

| id  | name  |
|-----|-------|
| 1   | IT    |
| 2   | Sales |

#### Output: 

| Department | Employee | Salary |
|------------|----------|--------|
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |

#### Explanation: 
- Max and Jim both have the highest salary in the IT department.
- Henry has the highest salary in the Sales department.
