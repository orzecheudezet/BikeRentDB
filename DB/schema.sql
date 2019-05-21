CREATE DATABASE BikeRents;

USE BikeRents

CREATE TABLE Bikes (
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Color varchar(50) NOT NULL,
Size int NOT NULL,
Brand varchar(50) NOT NULL);

CREATE TABLE Users (
PESEL char(11) NOT NULL PRIMARY KEY,
FirstName varchar(32) NOT NULL,
LastName varchar (32) NOT NULL);

CREATE TABLE Rents (
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Person char(11) NOT NULL FOREIGN KEY REFERENCES Users(PESEL),
Bike int NOT NULL FOREIGN KEY REFERENCES Bikes(Id),
DateFrom date NOT NULL,
DateTo date NOT NULL,
Price money NOT NULL,
[Status] bit NOT NULL);

SELECT * FROM Rents;
