# project1_2020
 CS50 Project 1 (2020)

The folder structure of this project is the same as the initial wiki.zip file in the project's description.

For the Markdown to HTML conversion I used the python library "markdown2" as suggested, therefore I include a requirements.txt file to install it.

The templates of the encyclopedia app are the following:

- `layout.html`: Base template provided at starting project files. Added missing URL linking for the website to work.
- `index.html`: Added missing URL linking for the website to work.
- `entry.html`: Displays title and content of an entry, as well as an edit link.
- `edit.html`: Displays title and allows edition of the content of an entry.
- `create.html`: Allows the creation of a new entry.
- `search.html`: Displays search's results as a list, or a message if there are no results.

The possible URL routes of the website are the following:

- `"/"`: redirects to `"/wiki/"` route.
- `"/wiki/"`: Index page listing all existing entries.
- `"/wiki/<str:title>"`: Shows the entry if exists, or an error message if not.
- `"/wiki/<str:title>/edit"`: Allows edition of the entry if exists, or an error message if not.
- `"/wiki/create"`: Allows creation of a new entry. Unique title required.
- `"/wiki/search"`: Allows search using query from GET request parameter (ex, `"/wiki/search?q=python"`)-
- `"/wiki/random"`: Redirects to a random entry page.

