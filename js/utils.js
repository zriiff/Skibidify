export function callAPI() {
  fetch('http://127.0.0.1:5000/api/skibidify?name=Zach') // Ensure the port and URL are correct
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
      console.log(data.message);  // Print the message from the API
    })
    .catch(error => {
      console.error('Error:', error);
    });
}