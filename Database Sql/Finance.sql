CREATE DATABASE NamalFinance;
USE NamalFinance;
CREATE TABLE Users(u_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, u_name VARCHAR(80),u_password VARCHAR(40),u_class VARCHAR(20));
CREATE TABLE Staff(stf_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, stf_name VARCHAR(255) , stf_email VARCHAR(255), stf_designation VARCHAR(255), stf_salary INT,u_id INT, FOREIGN KEY(u_id) REFERENCES Users(u_id));
CREATE TABLE Faculty( emp_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,emp_name VARCHAR(255), emp_email VARCHAR(255), emp_designation VARCHAR(255), emp_salary INT,u_id INT, FOREIGN KEY(u_id) REFERENCES Users(u_id));
CREATE TABLE Expenses(Electricity_Expense INT, EOBI INT, Umrah_Fund INT, House_Rent INT, Mess_Charge INT, Lp_charger INT, income_tax INT, Care_Rent INT);  
CREATE TABLE Student(std_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, std_name VARCHAR(255) , std_email VARCHAR(255), std_department VARCHAR(255), std_gender VARCHAR(10),std_hostel_flag BOOL,std_fee_waiver FLOAT,std_previos_fee INT, u_id INT, FOREIGN KEY(u_id) REFERENCES Users(u_id));
CREATE TABLE Fees(tuition_fee INT,hostel_fee INT, lab_exam_fee INT);
CREATE TABLE Posts(p_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, p_title VARCHAR(255),p_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, p_status VARCHAR(255) DEFAULT 'Unknown' ,p_data TEXT);
CREATE TABLE Employee(e_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,e_name VARCHAR(255),e_role VARCHAR(255),u_id INT, FOREIGN KEY(u_id) REFERENCES Users(u_id));
INSERT INTO Users (u_name,u_password,u_class) VALUES('Khadija','khadija123','Student'),('Bilal', 'bilal123', 'Staff'),('Sana', 'sana123', 'Faculty'), ('Sania', 'sania123', 'Employee'), ('Sadia', 'sadia123', 'Employee');
SELECT * FROM Users;
INSERT INTO Staff (stf_name,stf_email,stf_designation,stf_salary,u_id) VALUES('Muhammad Bilal', 'bilal@namal.edu.pk', 'Manager', '500000', '2');
SELECT * FROM Staff;
INSERT INTO Faculty (emp_name, emp_email, emp_designation ,emp_salary, u_id) VALUES('Sana', 'sana@namal.edu.pk', 'Professor', '100000', '3');
SELECT * FROM Faculty;
INSERT INTO Student (std_name,std_email,std_department,std_gender,std_hostel_flag,std_fee_waiver,std_previos_fee,u_id ) VALUES('Khadija', 'khadija@namal.edu.pk','CS', 'F', TRUE , 1.0, 0, 1);
SELECT * FROM Student;
INSERT INTO Fees (tuition_fee,hostel_fee,lab_exam_fee) VALUES (60000,5500, 2500);
SELECT * FROM Fees;
INSERT INTO Employee (e_name,e_role,u_id) VALUES ('Sania','Reviewer', 4), ('Sadia','Approver',5);
SELECT * FROM Employee;
INSERT INTO Expenses (Electricity_Expense,EOBI,Umrah_Fund , House_Rent,Mess_Charge,Lp_charger, income_tax,Care_Rent) VALUES(4000,600,2300,2455, 6000,7000,2200,300);
SELECT * FROM Expenses;


CREATE TABLE Test (t_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,t_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, t_status VARCHAR(10));
SELECT* FROM Test;
