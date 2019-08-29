CREATE DATABASE cu_data_mining;

USE cu_data_mining;

CREATE TABLE rates (
	id int NOT NULL auto_increment,
  del_cu_rate float NOT NULL,
  eur_to_usd_ex_rate float NOT NULL,
  camden_cu_rate float NOT NULL,
  date_added datetime DEFAULT current_timestamp,
  PRIMARY KEY (id)
);