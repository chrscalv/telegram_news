CREATE TABLE platform (
    id bigint PRIMARY KEY
    platform_name VARCHAR (100) UNIQUE NOT NULL
    link VARCHAR (255) NOT NULL
)

CREATE TABLE selectors(
    id bigint PRIMARY KEY
    selectors_name VARCHAR
    platform_id bigint 
    parent_id bigint
)
CREATE TABLE keyword(
    id bigint PRIMARY KEY
    keyword_name: VARCHAR(255) NOT NULL
)