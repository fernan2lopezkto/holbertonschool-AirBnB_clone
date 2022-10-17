<co>
<br>
<h1> HBNB </h1>
<br>
<br>
<h3>Juan Rey</h3>
<h3>Mauro Trenche</h3>
<h4>Holberton School<br>
ZONAMERICA<br>
Montevideo, Uruguay<br>
</h4>
<br>
<h2>AirBnB clone, general description</h2>
<p>The goal of the project is to deploy on our server a simple copy of the AirBnB website.</p><br>
<h3>About Airbnb</h3>
<p>Airbnb was born in 2007, when two of its founders welcomed three guests to their San Francisco apartment. It has grown a lot since then and currently has 4 million hosts who have shared their accommodations with more than 1 billion travelers in almost every country in the world. Every day, hosts offer exceptional stays and unique experiences that allow travelers to discover the world in a more authentic and intimate way.</p>
<br>
<h3>-Learning Objectives</h3>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>
<p>
    -How to create a Python package<br>
    -How to create a command interpreter in Python using the cmd module<br>
    -What is Unit testing and how to implement it in a large project<br>
    -How to serialize and deserialize a Class<br>
    -How to write and read a JSON file<br>
    -How to manage datetime<br>
    -What is an UUID<br>
    -What is *args and how to use it<br>
    -What is **kwargs and how to use it<br>
    -How to handle named arguments in a function<br>
</p>
<h3>The console</h3>
<p>
-create your data model<br>
-manage (create, update, destroy, etc) objects via a console / command interpreter<br>
-store and persist objects to a file (JSON file)<br>
</p>
<br>
<p>
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
<br><br>
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
<br><br>
The console will be a tool to validate this storage engine
</p>

</co>


<h1>Project general description</h1>

### Contents
- `console.py`: the core of the `cmd` line interpreter
- ***models***
  - `base_model.py`: Defines all common attributes/methods for other classes. It is initialized with ***kwargs* and sets the attributes *id*, *created_at* and *updated_at* with `datetime` and converted in ISO format.\
    *save()*: saves changes and updates the updated time.\
    *to_dict()*: returns a key/value dictionary of __dict__.
  - `Other classes`: (User, State, City, Amenity, Place, Review).
  - ***engine***
    - `file_storage.py`: Serializes instances to a JSON file and deserializes JSON file to instances.\
		*all()*: returns the dictionary `__objects`.\
    *new()*: sets in `__objects` the obj with key "<obj class name>.id".\
		*save()*: serializes `__objects` to the JSON file.\
		*reload()*: deserializes the JSON file to `__objects`.\
        

## Command Interpreter
prompt($): (hbnb)

### How to use it
- Type `./console.py` to launch the command interpreter.
- **create** - Creates a new instance of the class.\
	Usage: `create class_name`

		(hbnb) create BaseModel
			
- **show** - Prints an instance based on the class name and id.\
	Usage: `show class_name id`

		(hbnb) show BaseModel 1234

- **destroy** - Deletes an instance based on the class name and id.\
	Usage: `destroy class_name id`
		
		(hbnb) destroy BaseModel 1234

- **all** - Prints all instances based or not on the class name.\
	Usage: `all class_name` | `all`
	
		(hbnb) all BaseModel
		(hbnb) all

- **update** - Updates an instance based on the class name and id by adding or updating attribute.\
	Usage: `update class_name id attribute_name "attribute_value"`
	
		(hbnb) update BaseModel 1234 email "aibnb@mail.com"


