const fs = require('fs').promises;

async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8'); // Read the file asynchronously
        const lines = data.split('\n').filter((line) => line.trim() !== ''); // Remove empty lines

        if (lines.length <= 1) {
            throw new Error('Cannot load the database');
        }

        const headers = lines.shift(); // Remove the header row
        const students = lines.map((line) => line.split(','));

        const totalStudents = students.length;
        console.log(`Number of students: ${totalStudents}`);

        const fields = {};
        students.forEach((student) => {
            const field = student[3]; // Assume the field of study is the 4th column
            const firstName = student[0]; // Assume the first name is the 1st column
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        });

        for (const [field, names] of Object.entries(fields)) {
            console.log(
                `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
            );
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
