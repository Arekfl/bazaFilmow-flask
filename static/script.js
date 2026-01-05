function deleteSelected() {
    var checkboxes = document.querySelectorAll('#movieList input[type="checkbox"]:checked');
    var deletePromises = [];
    
    checkboxes.forEach(function(checkbox) {
        var listItem = checkbox.parentNode;
        var movieId = listItem.getAttribute('data-movie-id');
        
        if (movieId) {
            // Send DELETE request to backend
            deletePromises.push(
                fetch('/deleteMovie/' + movieId, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
            );
        }
    });
    
    // Wait for all deletions and reload page
    Promise.all(deletePromises).then(function() {
        window.location.reload();
    }).catch(function(error) {
        console.error('Error deleting movies:', error);
        alert('Error deleting movies. Please try again.');
    });
}