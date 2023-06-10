document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('search-button');
    const tutorialList = document.getElementById('tutorial-list');

    searchButton.addEventListener('click', function() {
      const searchText = document.getElementById('tutorial-search').value.toLowerCase();
      const tutorialItems = tutorialList.getElementsByTagName('li');

      for (let i = 0; i < tutorialItems.length; i += 2) {
        const tutorialTitle = tutorialItems[i].textContent.toLowerCase();
        const videoItem = tutorialItems[i].nextElementSibling;
        if (tutorialTitle.includes(searchText)) {
          tutorialItems[i].style.display = 'block';
          videoItem.style.display = 'block';
        } else {
          tutorialItems[i].style.display = 'none';
          videoItem.style.display = 'none';
        }
      }
    });
  });