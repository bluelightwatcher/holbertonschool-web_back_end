const { createServer } = require('node:http');
const fs = require('fs');
const path = require('path');

// Function to count students in a database
const countStudents = (database) => new Promise((resolve, reject) => {
  const results = {
    CS: [],
    SWE: [],
  };

  fs.readFile(database, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim().length > 0);
    const header = lines.shift(); // Remove the header line

    if (!header || header.split(',').length !== 4) {
      reject(new Error('Invalid CSV format'));
      return;
    }

    lines.forEach((line) => {
      const [firstName, lastName, age, field] = line.split(',');
      if (field === 'CS') results.CS.push(firstName);
      if (field === 'SWE') results.SWE.push(firstName);
    });

    const output = [
      `Number of students: ${lines.length}`,
      `Number of students in CS: ${results.CS.length}. List: ${results.CS.join(', ')}`,
      `Number of students in SWE: ${results.SWE.length}. List: ${results.SWE.join(', ')}`,
    ];

    resolve(output.join('\n'));
  });
});

// Create the HTTP server
const app = createServer((req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    // Get the database file from command-line arguments
    const database = process.argv[2];

    if (!database) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    countStudents(database)
      .then((data) => {
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('Server running at http://127.0.0.1:1245/');
});

// Export the server
module.exports = app;
