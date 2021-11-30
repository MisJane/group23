-- SQL_DDL_Joins

-- 1. Создать таблицу employees
--- id. serial,  primary key,
--- employee_name. Varchar(50), not null

create table employees
(
    id            serial
        constraint employees_pkey
            primary key,
    employee_name varchar(50) not null
);

-- 2. Наполнить таблицу employee 70 строками
INSERT INTO public.employees (id, employee_name) VALUES (DEFAULT, 'George Washington')

-- 3. Создать таблицу salary
-- - id. Serial  primary key,
-- - monthly_salary. Int, not null

create table employee_salary
(
    id             serial
        constraint employee_salary_pkey
            primary key,
        employee_id    integer not null
        constraint employee_salary_employee_id_key
            unique
			salary_id integer not null
        constraint employee_salary_salary_id_key
);

-- 4. Наполнить таблицу salary 15 строками:

INSERT INTO public.salary (id, monthly_salary) VALUES (DEFAULT, '1000')

-- 5. Создать таблицу employee_salary
-- - id. Serial  primary key,
-- - employee_id. Int, not null, unique
-- - salary_id. Int, not null

create table employee_salary
(
    id             serial
        constraint employee_salary_pkey
             primary key,
        employee_id    integer not null
        constraint employee_salary_employee_id_key
            unique,
            salary_id integer not null
        constraint employee_salary_salary_id_key
)

-- 6. Наполнить таблицу employee_salary 40 строками:
-- - в 10 строк из 40 вставить несуществующие employee_id

INSERT INTO public.employees (id, employee_name) VALUES (DEFAULT, 'William Henry Harrison')

-- 7. Создать таблицу roles
-- - id. Serial  primary key,
-- - role_name. int, not null, unique

create table roles (
id serial primary key,
role_name integer not null unique
)
-- 8. Поменять тип столба role_name с int на varchar(30)
alter table role
alter column role_name type varchar(30)
using role_name::integer;

-- 9. Наполнить таблицу roles 20 строками:
INSERT INTO public.role (id, role_name) VALUES (DEFAULT, 'Junior Python developer')

-- 10. Создать таблицу roles_employee
-- id. Serial  primary key,
 -- employee_id. Int, not null, unique (внешний ключ для таблицы employees, поле id)
 -- role_id. Int, not null (внешний ключ для таблицы roles, поле id)

create table roles_employee (
id serial primary key,
employee_id int not null unique,
role_id int not null,
foreign key (employee_id)
	references employees (id),
foreign key (role_id)
	references roles (id)
);

-- 11. Наполнить таблицу roles_employee 40 строками:
insert into roles_employee (id, employee_id, role_id)
values (default, 7, 2);
