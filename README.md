# recipebox_redux

This is an edit of a project created by my classmate, Cedric, with two new additions: the ability to edit recipes, and a feature allowing users to mark recipes as "favorites."

Editing of recipes is limited to only admins and the author of the recipe being edited. Any other users trying to access the page will receive an error message, while non-logged-in users will be redirected to sign in.

Logged in users now have an option to "favorite" each recipe by clicking a button. A list of an author's favorite recipes appears on their profile page, with links to each recipe.

The purpose of this branch is to make these updates without changing the original code or functionality unnecessarily. I tried very hard to leave the original code intact and work with what was already there. The only changes I made were related to those new features -- either implementing them or making tweaks to avoid errors associated with those changes.

There were a couple of minor exceptions:

1. A .gitignore file was created to speed up the process of pushing updates to GitHub.

2. The link to individual recipes on the homepage was corrected to allow for easier testing of the new features. I added a line showing who was logged in, because things were getting confusing!

3. I added text to this README.

This was a fun exercise, and I look forward to more such assignments!
