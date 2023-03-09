0x00 AirBnB clone - The console

In this directory you will find a implementation of a AirBnB clone. In this first step is implemented the Console. Commands for create, update, destroy, show and manage diferent classes and attributes for the items that the app will be offer and for the users.

The console

    create your data model
    manage (create, update, destroy, etc) objects via a console / command interpreter
    store and persist objects to a file (JSON file) The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored. This abstraction will also allow you to change the type of storage easily without updating all of your codebase. The console will be a tool to validate this storage engine

Command interpreter

Our command interpreter looks like a mini shell and allow us manage the objects of our project:

    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Update attributes of an object
    Destroy an object
>>>>>>> da56fe813e99123e169bfbd0e88e5cf7d7756373
