
CREATE TABLE "star_schema"."Customer_dim"
(
 customer_key varchar(50) NOT NULL,
 name         varchar(100) NOT NULL,
 contact_no   varchar(50) NOT NULL,
 nid          varchar(50) NOT NULL,
 CONSTRAINT PK_1 PRIMARY KEY ( customer_key )
);



CREATE TABLE "star_schema"."Item_dim"
(
 item_key    varchar(50) NOT NULL,
 item_name   varchar(100) NOT NULL,
 "desc"        varchar(300) NOT NULL,
 unit_price  numeric NOT NULL,
 man_country varchar(50) NOT NULL,
 supplier    varchar(100) NOT NULL,
 unit        varchar(50) NOT NULL,
 CONSTRAINT PK_2 PRIMARY KEY ( item_key )
);


CREATE TABLE "star_schema"."Store_dim"
(
 store_key varchar(50) NOT NULL,
 division  varchar(50) NOT NULL,
 district  varchar(100) NOT NULL,
 upazila   varchar(50) NOT NULL,
 CONSTRAINT PK_3 PRIMARY KEY ( store_key )
);


CREATE TABLE "star_schema"."Time_dim"
(
 time_key varchar(50) NOT NULL,
 "date"     date NOT NULL,
 hour     int NOT NULL,
 day      int NOT NULL,
 week     varchar(50) NOT NULL,
 month    int NOT NULL,
 quarter  varchar(2) NOT NULL,
 year     int NOT NULL,
 CONSTRAINT PK_4 PRIMARY KEY ( time_key )
);



CREATE TABLE "star_schema"."Trans_dim"
(
 payment_key varchar(50) NOT NULL,
 trans_type  varchar(50) NOT NULL,
 bank_name   varchar(100) NOT NULL,
 CONSTRAINT PK_5 PRIMARY KEY ( payment_key )
);


-- ************************************** Fact_table

CREATE TABLE "star_schema"."Fact_table"
(
 quantity     int NOT NULL,
 unit         varchar(50) NOT NULL,
 unit_price   numeric NOT NULL,
 total_price  numeric NOT NULL,
 item_key     varchar(50) NOT NULL,
 payment_key  varchar(50) NOT NULL,
 time_key     varchar(50) NOT NULL,
 store_key    varchar(50) NOT NULL,
 customer_key varchar(50) NOT NULL,
 CONSTRAINT FK_1 FOREIGN KEY ( item_key ) REFERENCES "star_schema"."Item_dim" ( item_key ),
 CONSTRAINT FK_2 FOREIGN KEY ( payment_key ) REFERENCES "star_schema"."Trans_dim" ( payment_key ),
 CONSTRAINT FK_3 FOREIGN KEY ( time_key ) REFERENCES "star_schema"."Time_dim" ( time_key ),
 CONSTRAINT FK_4 FOREIGN KEY ( store_key ) REFERENCES "star_schema"."Store_dim" ( store_key ),
 CONSTRAINT FK_5 FOREIGN KEY ( customer_key ) REFERENCES "star_schema"."Customer_dim" ( customer_key )
);

CREATE INDEX FK_1 ON "star_schema"."Fact_table"
(
 item_key
);

CREATE INDEX FK_2 ON "star_schema"."Fact_table"
(
 payment_key
);

CREATE INDEX FK_3 ON "star_schema"."Fact_table"
(
 time_key
);

CREATE INDEX FK_4 ON "star_schema"."Fact_table"
(
 store_key
);

CREATE INDEX FK_5 ON "star_schema"."Fact_table"
(
 customer_key
);


