/**Create modularized routing

/**Create server.js file

/**Create index.html file with js routing

Create 2 partial pages:
  /* _customizeUsers.html - create, delete
  /*_userList.html - show all users

Create Controllers for each partial page:
  /**CustomizeUsersController
  /**UserListsController

Both Controllers will inject a user Factory:
  /*userFactory

Factory will hold the following methods:
  /*index: retrieve all users
  /*create: add new users
  *delete: destroy one user
  /*And an array of user objects

Functionality:
1. At root ('/') show two paths to partial pages
2. When CustomizeUsers is select show partial page for Customize users
  - This is where you can create/delete users within the page
  - Continue to show different path directories
3. When UserLists is select show partial page for User list
  - This is where you can see all the users within the Factory
  - Continue to show different path directories
