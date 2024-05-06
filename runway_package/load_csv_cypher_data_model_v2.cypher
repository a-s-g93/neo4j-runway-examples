CREATE CONSTRAINT country_name IF NOT EXISTS FOR (n:Country) REQUIRE n.name IS UNIQUE;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Country {name: row.name})
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Capital {})
    SET n.capital = row.capital
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Region {})
    SET n.region = row.region
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Subregion {})
    SET n.subregion = row.subregion
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Currency {})
    SET n.currencyName = row.currency_name
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:Timezone {})
    SET n.timezones = row.timezones
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MERGE (n:GeographicalCoordinates {})
    SET n.latitude = row.latitude, n.longitude = row.longitude
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:Capital {})
    MERGE (source)-[n:HAS_CAPITAL]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:Region {})
    MERGE (source)-[n:BELONGS_TO_REGION]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:Subregion {})
    MERGE (source)-[n:BELONGS_TO_SUBREGION]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:Currency {})
    MERGE (source)-[n:USES_CURRENCY]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:Timezone {})
    MERGE (source)-[n:HAS_TIMEZONE]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
LOAD CSV WITH HEADERS FROM 'file:///countries.csv' as row
CALL {
    WITH row
    MATCH (source:Country {name: row.name})
    MATCH (target:GeographicalCoordinates {})
    MERGE (source)-[n:LOCATED_IN]->(target)
    
} IN TRANSACTIONS OF 10000 ROWS;
