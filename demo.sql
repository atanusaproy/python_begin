# PGSQL database

CREATE table tbl_users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

insert into tbl_users (name) values ('Atanu'), ('Sahinoor'), ('Arnab');

create table tbl_user_details (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tbl_users(id),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

insert into tbl_user_details (user_id, email, phone_number) values (1, 'atanu@gmail.com', '1234567890'),
(2, 'sahinoor@gmail.com', '1234567891');

create table tbl_user_addresses (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tbl_users(id),
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

insert into tbl_user_addresses (user_id, address_line1, address_line2) values (1, 'Kolkata City', 'West Bengal'),
(1, 'Mumbai', 'Maharashtra'),
(2, 'Delhi', 'New Delhi');


select 
tua.user_id as app_user_id,
tu."name" as user_name
ARRAY_AGG(
    json_build_object(
        'address_line1', tua.address_line1,
        'address_line2', tua.address_line2
    )
) as address_list
from 
 tbl_users tu 
RIGHT join tbl_user_addresses tua 
 on tua.user_id = tu.id
group by tu.id, tua.user_id;7