create sequence gov_id start with 1000 increment by 3;

create table gov_employee (
  id integer GENERATED ALWAYS as IDENTITY,
  gov_id integer default nextval('gov_id'),
  name TEXT
);


-- Do not modify below this line --
INSERT INTO gov_employee (name) 
  VALUES
      ('John Doe'),
      ('Jane Doe'),
      ('Jim Beam');

SELECT * FROM gov_employee;
