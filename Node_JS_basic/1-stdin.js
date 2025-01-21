console.log("Welcome to Holberton School, what is your name?");

process.stdin.on("data", (data) => {
    const name = data.toString().trim(); // Trim to remove extra whitespace or newline
    console.log(`Your name is: ${name}`);
    console.log("This important software is now closing");
    process.exit(); // Exit the process after the response
});
