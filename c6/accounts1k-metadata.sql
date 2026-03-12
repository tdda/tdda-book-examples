select table_name, column_name, data_type, udt_name
from INFORMATION_SCHEMA.COLUMNS
where table_name ='accounts1k';
