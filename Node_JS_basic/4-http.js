const { createServer } = require('node:http');

// Create the server and assign it to the variable 'app'
const app = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

// Listen on port 1245
app.listen(1245, () => {
  console.log('Server running at http://127.0.0.1:1245/');
});

// Export the server as 'app'
module.exports = app;
