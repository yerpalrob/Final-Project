### BooksLib

- My project is meant to be the front end for a library's database, which they could have open on their computers. The librarian would be the only one with access to log in and create new books, and visitors would be able to find a book and see where that book is located.
- In the folder /src/src/books you will find the files which I created
- In views.py the two views are created (the view of all of the books, and the view of a single book in detail).
- In urls.py the two url paths are defined. They are the list view of all books, and the detail view of an individual book.
- In models.py the models are created. First, each location is put into a static list as that is something which won't change. The model for the books is then created to include the name of the book, the description of the book, the author, the published year, the image, and the location in the library. 
- In admin.py the admin site is created, so that new books could be added to the site.
- In the folder ../books/templates/books the html templates for my site can be found
- base.html contains the basic elements of my site. Each page needs the option to go home to the main directory, or to go to the admin login site.
- book_detail.html contains the detail view of chosen book. 
- Index.html contains the directory view of the books in the library. For each book in the group list, a card div is created which cleanly places the books on the page.

### Other Infomation for the Staff to know

- I hope you enjoy the look of this project. I know that this project is not as ambitious as it could be. I started working on it later than I should have and with everything happening, my work (which is online content creation for various clients) has increased as two of my clients have taken to hosting multiple weekly webinars, and with my school work all coming to a head, I did what I could complete in the time I had left. I should have definitely taken advantage of the time given.