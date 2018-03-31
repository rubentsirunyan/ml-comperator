-- ****************** SqlDBM: MySQL ******************;
-- ***************************************************;



-- ************************************** `L4`

CREATE TABLE `L4`
(
 `Id`    INT NOT NULL ,
 `Value` VARCHAR(45) NOT NULL ,

PRIMARY KEY (`Id`)
);





-- ************************************** `L3`

CREATE TABLE `L3`
(
 `Id`    INT NOT NULL ,
 `Value` VARCHAR(45) NOT NULL ,

PRIMARY KEY (`Id`)
);





-- ************************************** `L0`

CREATE TABLE `L0`
(
 `Id`    INT NOT NULL ,
 `Value` VARCHAR(45) NOT NULL ,

PRIMARY KEY (`Id`)
);





-- ************************************** `L1`

CREATE TABLE `L1`
(
 `Id`    INT NOT NULL ,
 `Value` VARCHAR(45) NOT NULL ,

PRIMARY KEY (`Id`)
);





-- ************************************** `data`

CREATE TABLE `data`
(
 `Id`                                                    INT NOT NULL ,
 `M Customer Subtype L0`                                 INT NOT NULL ,
 `M Number of houses`                                    INT NOT NULL ,
 `M Avg size household`                                  INT NOT NULL ,
 `M Avg age L1`                                          INT NOT NULL ,
 `M Customer main type L2`                               INT NOT NULL ,
 `M Roman catholic L3`                                   INT NOT NULL ,
 `M Protestant L3`                                       INT NOT NULL ,
 `M Other religion L3`                                   INT NOT NULL ,
 `M No religion L3`                                      INT NOT NULL ,
 `M Married L3`                                          INT NOT NULL ,
 `M Living together L3`                                  INT NOT NULL ,
 `M Other relation L3`                                   INT NOT NULL ,
 `M Singles L3`                                          INT NOT NULL ,
 `M Household without children L3`                       INT NOT NULL ,
 `M Household with children L3`                          INT NOT NULL ,
 `M High level education L3`                             INT NOT NULL ,
 `M Medium level education L3`                           INT NOT NULL ,
 `M Lower level education L3`                            INT NOT NULL ,
 `M High status L3`                                      INT NOT NULL ,
 `M Entrepreneur L3`                                     INT NOT NULL ,
 `M Farmer L3`                                           INT NOT NULL ,
 `M Middle management L3`                                INT NOT NULL ,
 `M Skilled labourers L3`                                INT NOT NULL ,
 `M Unskilled labourers L3`                              INT NOT NULL ,
 `M Social class A L3`                                   INT NOT NULL ,
 `M Social class B1 L3`                                  INT NOT NULL ,
 `M Social class B2 L3`                                  INT NOT NULL ,
 `M Social class C L3`                                   INT NOT NULL ,
 `M Social class D L3`                                   INT NOT NULL ,
 `M Rented House L3`                                     INT NOT NULL ,
 `M Home owners L3`                                      INT NOT NULL ,
 `M 1 car L3`                                            INT NOT NULL ,
 `M 2 cars L3`                                           INT NOT NULL ,
 `M No car L3`                                           INT NOT NULL ,
 `M National Health Service L3`                          INT NOT NULL ,
 `M Private health insurance L3`                         INT NOT NULL ,
 `M Income < 30.000 L3`                                  INT NOT NULL ,
 `M Income 30-45.000 L3`                                 INT NOT NULL ,
 `M Income 45-75.000 L3`                                 INT NOT NULL ,
 `M Income 75-122.000 L3`                                INT NOT NULL ,
 `M Income > 123.000 L3`                                 INT NOT NULL ,
 `M Average income L3`                                   INT NOT NULL ,
 `M Purchasing power class L3`                           INT NOT NULL ,
 `Contribution third party insurance (firms) L3`         INT NOT NULL ,
 `Contribution private third party insurance L4`         INT NOT NULL ,
 `Contribution third party insurane (agriculture) L4`    INT NOT NULL ,
 `Contribution car policies L4`                          INT NOT NULL ,
 `Contribution delivery van policies L4`                 INT NOT NULL ,
 `Contribution motorcycle/scooter policies L4`           INT NOT NULL ,
 `Contribution lorry policies L4`                        INT NOT NULL ,
 `Contribution trailer policies L4`                      INT NOT NULL ,
 `Contribution tractor policies L4`                      INT NOT NULL ,
 `Contribution agricultural machines policies  L4`       INT NOT NULL ,
 `Contribution moped policies L4`                        INT NOT NULL ,
 `Contribution life insurances L4`                       INT NOT NULL ,
 `Contribution private accident insurance policies L4`   INT NOT NULL ,
 `Contribution family accidents insurance policies L4`   INT NOT NULL ,
 `Contribution disability insurance policies L4`         INT NOT NULL ,
 `Contribution fire policies L4`                         INT NOT NULL ,
 `Contribution surfboard policies L4`                    INT NOT NULL ,
 `Contribution boat policies L4`                         INT NOT NULL ,
 `Contribution bicycle policies L4`                      INT NOT NULL ,
 `Contribution property insurance policies L4`           INT NOT NULL ,
 `Contribution social security insurance policies L4`    INT NOT NULL ,
 `Number of private third party insurance 1 - 12 `       INT NOT NULL ,
 `Number of third party insurance (firms) 1 - 12 `       INT NOT NULL ,
 `Number of third party insurane (agriculture) 1 - 12 `  INT NOT NULL ,
 `Number of car policies 1 - 12 `                        INT NOT NULL ,
 `Number of delivery van policies 1 - 12 `               INT NOT NULL ,
 `Number of motorcycle or scooter policies 1 - 12 `      INT NOT NULL ,
 `Number of lorry policies 1 - 12 `                      INT NOT NULL ,
 `Number of trailer policies 1 - 12 `                    INT NOT NULL ,
 `Number of tractor policies 1 - 12 `                    INT NOT NULL ,
 `Number of agricultural machines policies 1 - 12 `      INT NOT NULL ,
 `Number of moped policies 1 - 12 `                      INT NOT NULL ,
 `Number of life insurances 1 - 12 `                     INT NOT NULL ,
 `Number of private accident insurance policies 1 - 12 ` INT NOT NULL ,
 `Number of family accidents insurance policies 1 - 12 ` INT NOT NULL ,
 `Number of disability insurance policies 1 - 12 `       INT NOT NULL ,
 `Number of fire policies 1 - 12 `                       INT NOT NULL ,
 `Number of surfboard policies 1 - 12 `                  INT NOT NULL ,
 `Number of boat policies 1 - 12 `                       INT NOT NULL ,
 `Number of bicycle policies 1 - 12 `                    INT NOT NULL ,
 `Number of property insurance policies 1 - 12 `         INT NOT NULL ,
 `Number of social security insurance policies 1 - 12 `  INT NOT NULL ,
 `Number of mobile home policies 0 - 1`                  INT NOT NULL ,

PRIMARY KEY (`Id`)
);


