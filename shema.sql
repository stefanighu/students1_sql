drop table if exists students;
drop table if exists courses;
drop table if exists student_courses;

pragma foreign_keys=on;

create table students(
    id integer primary key autoincrement ,
    name text not null,
    age int,
    major text
);

create table courses(
    id integer primary key autoincrement ,
    name text not null,
    instructor text
);

create table student_courses(
    id integer primary key autoincrement ,
    student_id int,
    course_id int,
    foreign key (student_id) references students(id),
    foreign key (course_id) references courses(id)
);


insert into students (name) values ("Степан");
insert into students (name, age) values ("Анна", 20);
insert into students (name, age, major) values ("Віктор", 21, "інженер");

insert into courses (name, instructor) values ("математика", "Олександр Маслов");
insert into courses (name) values ("хімія");

insert into student_courses (student_id, course_id) values (1, 1);
insert into student_courses (student_id, course_id) values (1, 2);
insert into student_courses (student_id, course_id) values (2, 1);
insert into student_courses (student_id, course_id) values (2, 2);
insert into student_courses (student_id, course_id) values (3, 1);