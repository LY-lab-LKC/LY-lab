// Import the filesystem module 
const fs = require("fs"); 

let directory_name = "static/img/gallery/AnatomyChallenge_2024"; 

// Function to get current filenames 
// in directory 
let filenames = fs.readdirSync(directory_name); 

console.log("\nFilenames in directory:"); 
filenames.forEach((file) => { 
	console.log("File:", directory_name + "/" + file); 
}); 
