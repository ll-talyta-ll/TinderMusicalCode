const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'mysqlserver.cjysrlze2w3y.us-east-1.rds.amazonaws.com',
  user: 'admin',
  password: 'Brasilhexa2022',
});

connection.connect((error) => {
  if(error){
    console.log('Error connecting to the MySQL Database');
    return;
  }
  console.log('Connection established sucessfully');
});
connection.end((error) => {
});





