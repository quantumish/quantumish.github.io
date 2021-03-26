// Get the hour
const today = new Date();
const hour = today.getHours();

// Here you can change your greetings
const gree1 = 'Go to sleep already!';
const gree2 = 'Good morning!';
const gree3 = 'Good afternoon!';
const gree4 = 'Good evening!';

// Define the hours of the greetings
if (hour >= 23 || hour < 5) {
	document.getElementById('greetings').innerText = gree1;
} else if (hour >= 6 && hour < 12) {
	document.getElementById('greetings').innerText = gree2;
} else if (hour >= 12 && hour < 17) {
	document.getElementById('greetings').innerText = gree3;
} else {
	document.getElementById('greetings').innerText = gree4;
}
