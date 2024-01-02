/*Arduino buttons*/ 
function buttonClicked(action) {
    fetch(`/run_python_code/${action}`)
      .then((response) => response.json())
      .catch((error) => {
        console.error("Error:", error);
      });
}

document.getElementById('signInLink').addEventListener('click', function() {
  window.location.href = 'your_destination_page.html';
});
