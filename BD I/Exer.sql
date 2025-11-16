1
SELECT 
    B.street AS BranchStreet,
    B.city AS City,
    P.street AS PropertyStreet
FROM Branch AS B
LEFT JOIN PropertyForRent AS P
    ON B.city = P.city;

2
SELECT 
    B.street AS BranchStreet,
    B.city AS City,
    P.street AS PropertyStreet
FROM Branch AS B
INNER JOIN PropertyForRent AS P
    ON B.city = P.city;

3
SELECT
fName,
Positiion,
branchNO
From Staff
Where branchNO IN (SELECT(BranchNO FROM Branch Where city = 'london'))

ou

SELECT
  fName,
  position,
  S.branchNo
FROM Staff AS S
JOIN Branch AS B ON S.branchNo = B.branchNo
WHERE B.city = 'London';



4
SELECT
fName,
From Staff
Where branchNO IN (SELECT(BranchNO FROM Branch Where street = '163 Main St'))

ou

SELECT
  S.fName
FROM Staff AS S
JOIN Branch AS B ON S.branchNo = B.branchNo
WHERE B.street = '163 Main St';



5
SELECT
    B.Name,
    A.properyNo,
    A.comment
FROM Viewing as A
LEFT JOIN Client as B ON A.ClientNo = B.ClientNo


6
SELECT
    Count(prefType),
FROM Client
Where prefType = 'Flat'


7
SELECT
    sum(rent) as Faturamento
From PropertyForRent

8
SELECT
    fName
From Staff
Where salary > (Select avg(salary) from Staff)


9
SELECT
    A.fName
    B.city
From Staff as A
LEFT JOIN Branch as B ON (A.branchNO = B.branchNO)
Where salary = (SELECT min(salary) from STAFF)


10
SELECT
    A.branchNO,
    count(B.staffNo),
    max(B.salary)
FROM Branch as A
LEFT JOIN Staff as B on (A.branchNO = B.branchNO)
Group By A.branchNo


11
SELECT
    A.branchNO,
    count(B.staffNo),
    avg(B.salary)
FROM Branch as A
LEFT JOIN Staff as B on (A.branchNO = B.branchNO)
Group By A.branchNo
having count(B.staffNo) > 1;


12
SELECT
    fName
FROM STAFF
Where salary BETWEEN 20000 and 30000



13
SELECT
    B.Name
FROM PropertyForRent as A
LEFT JOIN PrivateOwner as B ON (A.OwnerNO = B.OwnerNO)
Where A.city = 'Glasgow'


14
SELECT
    A.Name
From Staff as A
Where A.salary > (SELECT min(B.salary) From STAFF as B Where B.BrancNO = 'B003')

15
SELECT
    A.BranchNO,
    A.City,
    B.fName,
    C.propertyNo
From Branch as A 
LEFT JOIN Staff as B ON (A.BranchNO = B.BranchNO)
LEFT JOIN PropertyForRnt as C ON (C.staffNo = B.staffNo)
Order by A.BranchNo ASC, B.fName ASC

16
SELECT
    A.Name
From Client as A
Where NOT EXISTS
    (
        Select B.propertyNo
        FROM PropertyForRent as B
        Where B.rooms = 3

        EXCEPT

        Select C.propertyNo 
        FROM Viewing as C
        Where C.ClientNo = A.ClientNo



    )


17
UPDATE STAFF 
SET salary = salary * 1.05
Where position = 'Mananger';


18
INSERT INTO STAFF (staffNo, fName, Iname, position, sex, DOB, salary, branchNo)
VALUES ('SL42', 'Luciano', 'Digiampietri', 'Supervisor', 'M', 1000, 'B0005')

19
REMOVE FROM Viewing
Where properyNo = 'PG4'
