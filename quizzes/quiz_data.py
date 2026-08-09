# Single source of truth for curated, topic-matched quizzes and questions.
# 8 Categories x 5 Topics = 40 Quizzes x 10 Questions = 400 Questions total.

ALL_QUIZZES_DATA = {
    'Programming': {
        'Python Fundamentals': {
            'description': 'Test your core understanding of Python syntax, data types, functions, and control flow.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the output of print(2 ** 3) in Python?", "6", "8", "9", "12", "B", "The ** operator represents exponentiation in Python. 2 raised to the power 3 is 8."),
                ("Which keyword is used to define a function in Python?", "func", "define", "def", "function", "C", "The 'def' keyword is used to define functions in Python."),
                ("Which of the following data types is MUTABLE in Python?", "Tuple", "String", "List", "Integer", "C", "Lists are mutable, meaning their elements can be changed after creation. Tuples, strings, and integers are immutable."),
                ("How do you start a single-line comment in Python?", "//", "/*", "<!--", "#", "D", "In Python, single-line comments start with the hash symbol (#)."),
                ("What is the correct file extension for Python scripts?", ".pt", ".pyt", ".py", ".python", "C", "Standard Python source files use the .py extension."),
                ("Which built-in function returns the number of items in a list?", "length()", "size()", "len()", "count()", "C", "The len() function returns the number of items in an iterable object."),
                ("What does the 'continue' keyword do inside a loop?", "Exits the loop entirely", "Skips the rest of the current iteration", "Restarts the entire script", "Raises an Exception", "B", "The 'continue' statement skips the remaining code inside a loop for the current iteration and moves to the next."),
                ("Which of the following is an invalid variable name in Python?", "my_var", "_myvar", "2nd_var", "var2", "C", "Variable names cannot start with a digit in Python."),
                ("Which method appends a single item to the end of a Python list?", "insert()", "push()", "add()", "append()", "D", "The append() method adds an element to the end of an existing list."),
                ("What is the result of the expression 10 % 3?", "3.33", "1", "3", "0", "B", "The modulo operator (%) returns the remainder of integer division. 10 divided by 3 has a remainder of 1.")
            ]
        },
        'Web Development': {
            'description': 'Master frontend building blocks: HTML5 semantic tags, CSS styling properties, and JavaScript DOM interaction.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What does HTML stand for?", "Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink Text Language", "Home Tool Markup Language", "A", "HTML stands for Hyper Text Markup Language, the standard markup language for documents designed to display in web browsers."),
                ("Which CSS property controls the size of text?", "text-style", "font-style", "text-size", "font-size", "D", "The font-size CSS property sets the size of text content."),
                ("What does CSS stand for?", "Computer Style Sheets", "Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", "B", "CSS stands for Cascading Style Sheets, used to format layout and presentation of web pages."),
                ("Which HTML tag represents the top-level main heading?", "<h6>", "<heading>", "<h1>", "<head>", "C", "The <h1> tag specifies the most important heading on a page."),
                ("In modern JavaScript, which keyword declares a block-scoped variable?", "v", "variable", "let", "var=", "C", "The 'let' (and 'const') keyword declares block-scoped local variables in JavaScript."),
                ("Which HTML tag is used to emphasize text with semantic importance?", "<i>", "<italic>", "<em>", "<strong>", "C", "The <em> tag is used to indicate structural emphasis in HTML."),
                ("Which CSS property sets the background color of an element?", "bgcolor", "color", "background-color", "bg-color", "C", "The background-color property sets the background color of an element."),
                ("How do you trigger a pop-up alert box in JavaScript?", "alertBox('Hello')", "msgBox('Hello')", "msg('Hello')", "alert('Hello')", "D", "The window.alert() method displays an alert dialog with specified content."),
                ("Which HTML attribute provides alternative text for screen readers if an image fails to load?", "title", "alt", "src", "longdesc", "B", "The alt attribute specifies alternative text for an image."),
                ("Which HTML tag is used to create a hyper-link to another webpage?", "<link>", "<a>", "<href>", "<url>", "B", "The <a> (anchor) tag creates hyperlinks in HTML documents.")
            ]
        },
        'Data Structures': {
            'description': 'Evaluate your knowledge on Arrays, Stacks, Queues, Linked Lists, Trees, and Hash Tables.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which data structure follows the Last-In, First-Out (LIFO) principle?", "Queue", "Stack", "Tree", "Graph", "B", "A Stack operates on a LIFO structure where elements pushed last are popped first."),
                ("What is the average time complexity of key lookup in a Hash Table?", "O(1)", "O(log n)", "O(n)", "O(n^2)", "A", "With a good hash function, key lookup in a hash table takes constant time O(1)."),
                ("Which data structure operates on a First-In, First-Out (FIFO) policy?", "Stack", "Queue", "Array", "Binary Tree", "B", "A Queue processes elements in FIFO order, similar to a real-world line of people."),
                ("A tree structure where each node has at most two child nodes is called a:", "Binary Tree", "B-Tree", "Trie", "Graph", "A", "A Binary Tree is a hierarchical structure in which each parent node has maximum 2 children."),
                ("What is the term for inserting an element onto a stack?", "Pop", "Push", "Enqueue", "Append", "B", "Pushing adds an element to the top of the stack; popping removes it."),
                ("Which of the following is considered a linear data structure?", "Tree", "Graph", "Array", "Binary Heap", "C", "An Array is a contiguous linear sequence of memory elements."),
                ("In a singly linked list, what two components form each node?", "Index and Value", "Key and Value", "Data and Pointer to Next Node", "Hash and Data", "C", "Each node in a singly linked list contains stored data and a reference pointer to the next node."),
                ("Which operation removes the front element from a Queue?", "Dequeue", "Enqueue", "Pop", "Shift", "A", "Enqueue adds an item to the rear, while Dequeue removes an item from the front."),
                ("What is the time complexity to access an array element when the index is known?", "O(n)", "O(log n)", "O(1)", "O(n^2)", "C", "Array memory allocation enables instant O(1) direct index accessing."),
                ("Which data structure is primarily utilized in Breadth-First Search (BFS) graph traversal?", "Stack", "Queue", "Priority Queue", "Min-Heap", "B", "BFS visits neighboring vertices level-by-level using a FIFO Queue.")
            ]
        },
        'Database Design': {
            'description': 'Understand relational concepts, Primary/Foreign keys, SQL query syntax, and schema normalization rules.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the primary role of a Primary Key in a database table?", "Encrypt sensitive table data", "Uniquely identify each record in a table", "Store foreign references", "Sort query output automatically", "B", "A Primary Key constraint uniquely identifies each record in a database table without duplicate or NULL values."),
                ("Which SQL clause is used to retrieve data from a database?", "GET", "EXTRACT", "OPEN", "SELECT", "D", "The SELECT statement extracts record fields from one or more tables."),
                ("What does SQL stand for?", "Structured Query Language", "Strong Question Language", "System Query Logic", "Simple Query List", "A", "SQL stands for Structured Query Language."),
                ("Which SQL keyword is used to sort the result set in ascending or descending order?", "SORT BY", "ORDER BY", "ALIGN BY", "GROUP BY", "B", "The ORDER BY keyword sorts query results by one or more columns."),
                ("What is the purpose of a Foreign Key constraint?", "Encrypt table columns", "Enforce unique values in a single table", "Link records between two tables", "Prevent duplicate rows", "C", "A Foreign Key establishes a relational link referencing the primary key of another table."),
                ("Which SQL statement updates existing records in a table?", "MODIFY", "UPDATE", "CHANGE", "ALTER", "B", "The UPDATE statement modifies existing data records within a table."),
                ("In relational database terminology, what is a single horizontal row called?", "Attribute", "Field", "Tuple / Record", "Schema", "C", "A row in a relational database table is formally termed a Tuple or Record."),
                ("Which SQL clause filters records based on specified conditional criteria?", "WHERE", "GROUP BY", "HAVING", "ORDER BY", "A", "The WHERE clause filters records before any grouping occurs."),
                ("Which Normal Form ensures there are no transitive dependencies between non-key attributes?", "1NF", "2NF", "3NF", "BCNF", "C", "Third Normal Form (3NF) requires a table to be in 2NF and have no non-key attribute transitively dependent on the primary key."),
                ("Which SQL clause groups rows that have matching values into summary rows?", "ORDER BY", "GROUP BY", "JOIN", "FILTER BY", "B", "The GROUP BY statement groups rows sharing column values to run aggregate functions (COUNT, SUM, AVG).")
            ]
        },
        'Algorithms': {
            'description': 'Test your grasp of sorting methods, search algorithms, recursion, and Big-O efficiency metrics.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which sorting algorithm has an average time complexity of O(n log n)?", "Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort", "C", "Merge Sort consistently achieves O(n log n) performance using a divide-and-conquer strategy."),
                ("What is the core definition of a recursive function?", "A loop that runs infinitely", "A function that calls itself", "A function with no return value", "A sorting algorithm", "B", "Recursion occurs when a function invokes itself to break down problems into smaller base cases."),
                ("Which algorithm finds the shortest path between nodes in a weighted graph with non-negative edge weights?", "Depth-First Search", "Breadth-First Search", "Dijkstra's Algorithm", "Binary Search", "C", "Dijkstra's algorithm efficiently computes single-source shortest paths in weighted graphs."),
                ("What is the worst-case time complexity of Bubble Sort?", "O(n)", "O(n log n)", "O(n^2)", "O(2^n)", "C", "Bubble Sort requires nested passes over un-ordered elements, resulting in O(n^2) time complexity."),
                ("What prerequisite condition MUST be met before performing a Binary Search?", "The array must be empty", "The array must be sorted", "The array must contain even elements", "The array must be reversed", "B", "Binary search depends on sorted element order to halve search bounds repeatedly."),
                ("Dynamic Programming relies on breaking problems into subproblems possessing which key property?", "Random values", "Greedy steps", "Overlapping subproblems & optimal substructure", "Unsorted keys", "C", "Dynamic Programming stores solved results of overlapping subproblems to avoid redundant calculations."),
                ("Which search algorithm inspects elements sequentially from beginning to end?", "Binary Search", "Linear Search", "Jump Search", "Interpolation Search", "B", "Linear search iterates index-by-index until matching the target element."),
                ("What algorithmic strategy does Merge Sort utilize?", "Greedy strategy", "Backtracking", "Divide and Conquer", "Brute Force", "C", "Merge Sort divides arrays into halves, recursively sorts them, and merges sorted sub-arrays."),
                ("In complexity theory, what set represents problems solvable in polynomial time by a deterministic machine?", "NP", "P", "NP-Complete", "NP-Hard", "B", "Class P consists of decision problems solvable in polynomial time O(n^k)."),
                ("What is the time complexity of searching a sorted array of size n using Binary Search?", "O(1)", "O(n)", "O(log n)", "O(n^2)", "C", "Binary Search eliminates half of remaining elements each step, completing in O(log n) time.")
            ]
        }
    },
    'Science': {
        'Physics & Motion': {
            'description': 'Explore fundamental laws of classical mechanics, energy forms, light velocity, and thermodynamics.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is Isaac Newton's First Law of Motion also known as?", "Law of Universal Gravitation", "Law of Inertia", "Law of Action and Reaction", "Law of Acceleration", "B", "Newton's First Law states an object remains at rest or in uniform motion unless acted on by an external force (Law of Inertia)."),
                ("What is the approximate speed of light in a vacuum?", "300,000 km/s", "150,000 km/s", "1,000,000 km/s", "30,000 km/s", "A", "Light travels in a vacuum at approximately 299,792 kilometers per second (~300,000 km/s)."),
                ("What standard SI unit measures energy or work?", "Watt", "Pascal", "Joule", "Newton", "C", "The Joule (J) is the SI unit of work and energy."),
                ("Which fundamental force keeps planets orbiting around the Sun?", "Electromagnetic Force", "Weak Nuclear Force", "Gravitational Force", "Strong Nuclear Force", "C", "Gravity is the attractive force that keeps celestial bodies in orbital paths."),
                ("What device converts mechanical energy into electrical energy?", "Electric Motor", "Generator", "Transformer", "Capacitor", "B", "Generators use electromagnetic induction to turn mechanical rotation into electrical energy."),
                ("Which state of matter has a definite volume but no fixed shape?", "Solid", "Liquid", "Gas", "Plasma", "B", "Liquids take the shape of their container while maintaining a fixed volume."),
                ("What physical quantity is calculated as Force divided by Area?", "Work", "Power", "Pressure", "Momentum", "C", "Pressure is defined as force applied perpendicular to a surface per unit area (P = F / A)."),
                ("Which scientist formulated the famous mass-energy equivalence equation E = mc²?", "Niels Bohr", "Galileo Galilei", "Albert Einstein", "Isaac Newton", "C", "Albert Einstein published the principle of mass-energy equivalence in 1905."),
                ("What is the acceleration due to gravity near Earth's surface?", "9.8 m/s²", "5.2 m/s²", "12.4 m/s²", "1.6 m/s²", "A", "Standard gravity on Earth is approximately 9.8 meters per second squared (m/s²)."),
                ("Which spectrum wave has the shortest wavelength and highest frequency?", "Radio waves", "Visible light", "Gamma rays", "Microwaves", "C", "Gamma rays have the highest frequency and energy in the electromagnetic spectrum.")
            ]
        },
        'Chemistry & Elements': {
            'description': 'Test your knowledge on periodic elements, chemical reactions, atomic structure, and pH scales.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the chemical symbol for Gold on the periodic table?", "Ag", "Au", "Fe", "Gd", "B", "Au (from Latin 'Aurum') is the chemical symbol for Gold."),
                ("What particle carries a negative electrical charge inside an atom?", "Proton", "Neutron", "Electron", "Positron", "C", "Electrons orbit the atomic nucleus carrying a negative charge."),
                ("What is the pH value of pure, neutral water at 25°C?", "0", "5", "7", "14", "C", "Neutral pure water measures exactly 7 on the 0-14 pH scale."),
                ("Which gas is most abundant in Earth's atmosphere (~78%)?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Argon", "B", "Nitrogen gas makes up roughly 78% of Earth's atmospheric volume."),
                ("What type of bond is formed when electrons are shared between two non-metal atoms?", "Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond", "B", "Covalent bonding involves sharing pairs of electrons between atoms."),
                ("What is the lightest element on the Periodic Table with atomic number 1?", "Helium", "Hydrogen", "Lithium", "Carbon", "B", "Hydrogen is the simplest and lightest element with atomic number 1."),
                ("What common compound has the chemical formula NaCl?", "Baking Soda", "Table Salt", "Sugar", "Bleach", "B", "Sodium Chloride (NaCl) is common table salt."),
                ("Substances with a pH value less than 7 are classified as:", "Bases / Alkaline", "Acids", "Salts", "Oxides", "B", "Solutions with pH below 7 are acidic; pH above 7 is basic."),
                ("Which noble gas is commonly used in illuminated glowing sign tubes?", "Argon", "Neon", "Krypton", "Xenon", "B", "Neon produces a reddish-orange glow when an electric current passes through it."),
                ("What process describes a solid changing directly into a gas without turning liquid?", "Evaporation", "Condensation", "Sublimation", "Deposition", "C", "Sublimation is the transition directly from solid to gas (e.g. dry ice).")
            ]
        },
        'Biology & Human Body': {
            'description': 'Master cellular biology, genetics, human organ systems, and photosynthetic plant processes.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which organelle is widely known as the 'powerhouse of the cell'?", "Nucleus", "Ribosome", "Mitochondria", "Golgi Body", "C", "Mitochondria generate most of the cell's chemical energy stored in ATP."),
                ("What double-helix molecule carries the genetic instructions for living organisms?", "RNA", "DNA", "ATP", "Glucose", "B", "Deoxyribonucleic acid (DNA) stores hereditary genetic instructions."),
                ("What process do green plants use to synthesize food from sunlight and CO2?", "Respiration", "Photosynthesis", "Transpiration", "Fermentation", "B", "Photosynthesis uses solar energy to convert water and carbon dioxide into glucose and oxygen."),
                ("How many chambers are inside a healthy human heart?", "2", "3", "4", "6", "C", "The human heart has 4 chambers: two atria and two ventricles."),
                ("What pigment gives plant leaves their green color?", "Carotene", "Chlorophyll", "Hemoglobin", "Melanin", "B", "Chlorophyll absorbs red and blue light while reflecting green light."),
                ("Which blood cell type is primarily responsible for fighting infections?", "Red Blood Cells", "White Blood Cells", "Platelets", "Plasma", "B", "White blood cells (leukocytes) protect the body against infectious diseases."),
                ("What is the largest organ in the human body?", "Liver", "Brain", "Skin", "Heart", "C", "Skin is the body's largest organ, accounting for ~15% of body weight."),
                ("Human DNA is packaged into how many pairs of chromosomes?", "12 pairs", "23 pairs", "46 pairs", "30 pairs", "B", "Humans have 23 pairs of chromosomes, totaling 46 chromosomes per cell."),
                ("Which organ produces the hormone insulin to regulate blood sugar levels?", "Liver", "Kidney", "Pancreas", "Thyroid", "C", "The Pancreas secretes insulin to control glucose levels in the bloodstream."),
                ("What structural system connects bones to other bones at joints?", "Tendons", "Ligaments", "Muscles", "Cartilage", "B", "Ligaments are tough fibrous bands connecting bone to bone.")
            ]
        },
        'Astronomy & Space': {
            'description': 'Journey through our solar system, stellar lifecycles, neighboring galaxies, and lunar missions.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which planet in our solar system is known as the 'Red Planet'?", "Venus", "Mars", "Jupiter", "Mercury", "B", "Mars appears red due to iron oxide (rust) covering its surface."),
                ("What is the approximate age of the Universe according to cosmological estimates?", "4.5 billion years", "13.8 billion years", "20 billion years", "9.3 billion years", "B", "Cosmic microwave background data estimates the universe age at ~13.8 billion years."),
                ("Which star is closest to our Solar System?", "Sirius", "Alpha Centauri A", "Proxima Centauri", "Betelgeuse", "C", "Proxima Centauri is a red dwarf star located ~4.24 light-years away."),
                ("What is the dominant gas in Venus' atmosphere (~96.5%)?", "Carbon Dioxide", "Nitrogen", "Oxygen", "Methane", "A", "Venus has a thick atmosphere mostly comprised of Carbon Dioxide, creating an intense greenhouse effect."),
                ("Which large spiral galaxy is closest to the Milky Way?", "Triangulum Galaxy", "Andromeda Galaxy", "Whirlpool Galaxy", "Sombrero Galaxy", "B", "The Andromeda Galaxy (M31) is our closest neighboring spiral galaxy ~2.5 million light-years away."),
                ("Which planet holds the record for having the most confirmed moons in our Solar System?", "Jupiter", "Saturn", "Uranus", "Neptune", "B", "Saturn has over 140 confirmed orbiting moons."),
                ("What was the name of the first artificial satellite launched into space in 1957?", "Apollo 11", "Sputnik 1", "Explorer 1", "Voyager 1", "B", "The Soviet Union launched Sputnik 1 on October 4, 1957."),
                ("Who was the first human to walk on the surface of the Moon?", "Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong", "Michael Collins", "C", "Neil Armstrong stepped onto the Moon on July 21, 1969 during Apollo 11."),
                ("What is the name of the galaxy containing our Solar System?", "Andromeda", "Milky Way", "Centaurus", "Orion", "B", "Our solar system resides in the Milky Way barred spiral galaxy."),
                ("What astronomical classification best describes our Sun?", "Yellow Dwarf Star (G2V)", "Red Giant", "White Dwarf", "Blue Supergiant", "A", "The Sun is a G-type main-sequence star, commonly called a yellow dwarf.")
            ]
        },
        'Environmental & Earth Science': {
            'description': 'Understand Earth tectonic layers, atmospheric zones, water cycles, and ecological principles.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which atmospheric layer contains the ozone layer that protects Earth from UV radiation?", "Troposphere", "Stratosphere", "Mesosphere", "Thermosphere", "B", "The Stratosphere contains high concentrations of ozone (O3) absorbing solar UV rays."),
                ("What process causes large tectonic plates to move across the mantle?", "Mantle Convection", "Gravitational Pull", "Solar Tides", "Ocean Currents", "A", "Convection currents in the molten mantle drive tectonic plate movement."),
                ("What instrument measures earthquake intensity and seismic waves?", "Barometer", "Seismograph", "Anemometer", "Hygrometer", "B", "A Seismograph detects and records ground vibrations caused by seismic waves."),
                ("What is the hardest naturally occurring mineral on Mohs hardness scale?", "Quartz", "Corundum", "Diamond", "Topaz", "C", "Diamond scores a maximum 10 on the Mohs mineral hardness scale."),
                ("What percentage of Earth's surface is covered by oceans and water?", "50%", "61%", "71%", "85%", "C", "Oceans and liquid bodies cover roughly 71% of the Earth's surface."),
                ("Which rock type forms from cooled and solidified lava or magma?", "Sedimentary", "Metamorphic", "Igneous", "Fossiliferous", "C", "Igneous rocks (like basalt or granite) crystallize from molten magma/lava."),
                ("What component of the water cycle describes water vapor turning back into liquid drops?", "Evaporation", "Condensation", "Precipitation", "Transpiration", "B", "Condensation cools water vapor into liquid droplets forming clouds."),
                ("What gas released by fossil fuel burning is the primary driver of global greenhouse warming?", "Argon", "Carbon Dioxide", "Helium", "Ozone", "B", "Carbon Dioxide (CO2) traps heat energy in the lower atmosphere."),
                ("What boundary scale rates hurricane wind speeds from Category 1 to 5?", "Richter Scale", "Saffir-Simpson Scale", "Beaufort Scale", "VEI Scale", "B", "The Saffir-Simpson Hurricane Wind Scale categorizes tropical cyclones by sustained wind speed."),
                ("What is Earth's innermost solid metallic layer made primarily of?", "Silicon and Aluminum", "Iron and Nickel", "Copper and Zinc", "Gold and Lead", "B", "Earth's inner core is a solid sphere composed mostly of iron and nickel.")
            ]
        }
    },
    'Mathematics': {
        'Algebra & Equations': {
            'description': 'Solve linear equations, quadratic formulas, polynomial factoring, and exponential expressions.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Solve for x: 3x + 7 = 22", "x = 3", "x = 5", "x = 6", "x = 4", "B", "Subtract 7 from 22 to get 3x = 15. Divide by 3 to find x = 5."),
                ("What is the quadratic formula used to solve ax² + bx + c = 0?", "x = (-b ± √(b² - 4ac)) / (2a)", "x = (b ± √(b² + 4ac)) / a", "x = -b / 2a", "x = √(b² - 4ac)", "A", "The standard quadratic formula is x = (-b ± √(b² - 4ac)) / (2a)."),
                ("What is the value of 5⁰ (five to the power of zero)?", "0", "5", "1", "10", "C", "Any non-zero real number raised to the power of zero equals 1."),
                ("Factor the quadratic expression: x² - 9", "(x - 3)(x - 3)", "(x + 3)(x - 3)", "(x + 9)(x - 1)", "(x + 3)(x + 3)", "B", "x² - 9 is a difference of squares: (x + 3)(x - 3)."),
                ("If f(x) = 2x + 3, what is f(4)?", "7", "9", "11", "14", "C", "Substitute 4 for x: 2(4) + 3 = 8 + 3 = 11."),
                ("Simplify: (x³)²", "x⁵", "x⁶", "x⁹", "x¹", "B", "When raising a power to a power, multiply exponents: 3 * 2 = 6, yielding x⁶."),
                ("If 2^x = 16, what is x?", "2", "3", "4", "5", "C", "2 raised to the power 4 is 16 (2 * 2 * 2 * 2 = 16)."),
                ("What is the slope of the linear line y = 4x - 7?", "4", "-7", "7", "1/4", "A", "In slope-intercept form (y = mx + b), m represents the slope (4)."),
                ("Solve for y: 2y - 4 = 10", "y = 5", "y = 7", "y = 8", "y = 6", "B", "Add 4 to 10 to get 2y = 14. Divide by 2 to get y = 7."),
                ("What is the absolute value |-15|?", "-15", "0", "15", "1/15", "C", "The absolute value of a negative number is its positive magnitude: 15.")
            ]
        },
        'Geometry & Shapes': {
            'description': 'Master geometric theorems, triangle ratios, circle areas, polygon angles, and volume calculations.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("If a right-angled triangle has legs of length 6 and 8, what is the hypotenuse length?", "9", "10", "12", "14", "B", "By Pythagorean theorem a² + b² = c²: 6² + 8² = 36 + 64 = 100. √100 = 10."),
                ("What is the formula for the area of a circle with radius r?", "2πr", "πr²", "πd", "2πr²", "B", "Area of a circle is calculated using A = πr²."),
                ("What is the sum of interior angles of a regular hexagon (6 sides)?", "540°", "720°", "900°", "360°", "B", "Sum of interior angles = (n - 2) * 180°. For n=6: (6-2)*180° = 4*180° = 720°."),
                ("What is the perimeter of a rectangle with length 12 cm and width 5 cm?", "34 cm", "60 cm", "17 cm", "24 cm", "A", "Perimeter P = 2*(length + width) = 2*(12 + 5) = 34 cm."),
                ("How many total degrees are in a full circle revolution?", "180°", "270°", "360°", "540°", "C", "A complete circular rotation comprises 360 degrees."),
                ("What is the area of a triangle with base 10 cm and height 6 cm?", "60 cm²", "30 cm²", "16 cm²", "20 cm²", "B", "Area of a triangle = (1/2) * base * height = 0.5 * 10 * 6 = 30 cm²."),
                ("How many sides does a regular nonagon have?", "7", "8", "9", "10", "C", "A nonagon is a polygon with 9 sides."),
                ("What is the volume of a cube with side length 4 cm?", "16 cm³", "32 cm³", "64 cm³", "128 cm³", "C", "Volume of a cube = side³ = 4 * 4 * 4 = 64 cm³."),
                ("What is the complementary angle to 35 degrees?", "55°", "145°", "65°", "90°", "A", "Complementary angles sum to 90 degrees. 90° - 35° = 55°."),
                ("What trigonometric ratio is defined as Opposite divided by Hypotenuse?", "Cosine", "Sine", "Tangent", "Secant", "B", "Sine (sin) = Opposite / Hypotenuse in a right triangle.")
            ]
        },
        'Arithmetic & Number Theory': {
            'description': 'Test fundamental numeracy: prime numbers, fractions, LCM/GCD, percentages, and proportions.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which of the following numbers is a PRIME number?", "9", "15", "17", "21", "C", "17 has only two factors: 1 and 17, making it prime. 9, 15, and 21 are composite."),
                ("What is the Least Common Multiple (LCM) of 4 and 6?", "12", "24", "10", "8", "A", "Multiples of 4: 4, 8, 12... Multiples of 6: 6, 12... Smallest common multiple is 12."),
                ("What is the Greatest Common Divisor (GCD) of 24 and 36?", "6", "12", "18", "4", "B", "12 is the largest integer dividing both 24 and 36 without a remainder."),
                ("Convert the fraction 3/4 into a percentage:", "60%", "70%", "75%", "80%", "C", "3 divided by 4 equals 0.75, which is 75%."),
                ("What is 15% of 200?", "20", "25", "30", "35", "C", "0.15 * 200 = 30."),
                ("Evaluate: 12 + 8 ÷ 2", "10", "16", "20", "14", "B", "Follow Order of Operations (PEMDAS): Division first (8/2 = 4), then addition (12 + 4 = 16)."),
                ("What is the reciprocal of 2/5?", "5/2", "-2/5", "1/5", "5/4", "A", "Flipping numerator and denominator gives 5/2."),
                ("What is the next prime number after 11?", "13", "14", "15", "17", "A", "13 is the smallest prime number greater than 11."),
                ("Simplify the ratio 15 : 25 into simplest form:", "3 : 4", "3 : 5", "5 : 3", "1 : 2", "B", "Divide both terms by 5: 15/5 = 3 and 25/5 = 5, giving 3:5."),
                ("What is 2 raised to the power of 5 (2⁵)?", "16", "25", "32", "64", "C", "2 * 2 * 2 * 2 * 2 = 32.")
            ]
        },
        'Calculus & Functions': {
            'description': 'Calculate derivatives, antiderivatives, limits, rates of change, and natural logarithms.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the derivative of f(x) = x^2 with respect to x?", "2x", "x", "2", "x^3 / 3", "A", "Using the Power Rule (d/dx [x^n] = n*x^(n-1)), derivative of x^2 is 2x."),
                ("What is the derivative of the natural logarithm function f(x) = ln(x) for x > 0?", "1/x", "e^x", "x", "ln(x)/x", "A", "The derivative of ln(x) is 1/x."),
                ("What is the indefinite integral of 1/x with respect to x?", "ln(|x|) + C", "-1/x^2 + C", "x^2/2 + C", "e^x + C", "A", "The antiderivative of 1/x is ln(|x|) + C."),
                ("What is the derivative of sin(x) with respect to x?", "cos(x)", "-cos(x)", "tan(x)", "-sin(x)", "A", "d/dx [sin(x)] = cos(x)."),
                ("What is the derivative of a constant value c?", "1", "c", "0", "x", "C", "The rate of change of any constant value is 0."),
                ("What is the limit of (1/x) as x approaches infinity?", "0", "1", "Infinity", "Undefined", "A", "As denominator x grows infinitely large, 1/x approaches 0."),
                ("What is the derivative of e^x with respect to x?", "e^x", "x * e^(x-1)", "ln(x)", "1/e^x", "A", "The natural exponential function e^x is its own derivative."),
                ("What is the antiderivative of x with respect to x?", "(x^2)/2 + C", "x^2 + C", "1", "2x + C", "A", "Using reverse power rule: ∫ x dx = (x^(1+1))/(1+1) = (x^2)/2 + C."),
                ("What value is sin(90°) in trigonometry?", "0", "0.5", "1", "-1", "C", "sin(90°) on the unit circle equals 1."),
                ("What is the derivative of cos(x)?", "sin(x)", "-sin(x)", "tan(x)", "-cos(x)", "B", "d/dx [cos(x)] = -sin(x).")
            ]
        },
        'Probability & Statistics': {
            'description': 'Analyze statistical averages, medians, variance, permutations, and probability distributions.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the mean of the dataset [4, 8, 12, 16]?", "8", "10", "12", "14", "B", "Mean = (4 + 8 + 12 + 16) / 4 = 40 / 4 = 10."),
                ("What is the median of the dataset [3, 7, 9, 15, 21]?", "7", "9", "12", "15", "B", "The middle number in the sorted set is 9."),
                ("What is the probability of rolling a 4 on a fair 6-sided die?", "1/2", "1/4", "1/6", "1/3", "C", "There is 1 favorable outcome out of 6 possible sides: 1/6."),
                ("What is the mode in a statistical dataset?", "The average value", "The middle value", "The most frequently occurring value", "The difference between max and min", "C", "The mode is the number that appears most frequently in a dataset."),
                ("What is the probability of flipping two coins and getting heads on both?", "1/2", "1/4", "3/4", "1/8", "B", "P(Head) * P(Head) = (1/2) * (1/2) = 1/4."),
                ("How many unique permutations can be formed from the 3 letters A, B, C?", "3", "6", "9", "12", "B", "3! (3 factorial) = 3 * 2 * 1 = 6."),
                ("What is the range of the dataset [5, 12, 3, 22, 18]?", "17", "19", "22", "15", "B", "Range = Max value - Min value = 22 - 3 = 19."),
                ("If an event is guaranteed to happen, what is its probability value?", "0", "0.5", "1.0", "100", "C", "Certain events have a probability of 1 (or 100%)."),
                ("What does Standard Deviation measure in statistics?", "Central tendency", "Data dispersion / spread", "Total sum", "Median value", "B", "Standard deviation quantifies the amount of variation or dispersion around the mean."),
                ("What is 5! (5 factorial)?", "20", "60", "120", "720", "C", "5! = 5 * 4 * 3 * 2 * 1 = 120.")
            ]
        }
    },
    'General Knowledge': {
        'World Geography & Capitals': {
            'description': 'Identify national capitals, major mountain ranges, global oceans, and river paths.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What is the capital city of Japan?", "Kyoto", "Osaka", "Tokyo", "Hiroshima", "C", "Tokyo is the capital and largest city of Japan."),
                ("Which ocean is the largest on Earth by surface area?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", "C", "The Pacific Ocean covers over 30% of Earth's surface."),
                ("What is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", "B", "The Nile River stretches ~6,650 km in northeastern Africa."),
                ("In which country are the Pyramids of Giza located?", "Greece", "Mexico", "Egypt", "Iraq", "C", "The Giza pyramid complex is located near Cairo, Egypt."),
                ("What is the smallest independent state in the world by land area?", "Monaco", "San Marino", "Vatican City", "Liechtenstein", "C", "Vatican City is the smallest independent state at ~0.49 sq km."),
                ("Which continent contains the Amazon Rainforest?", "Africa", "Asia", "South America", "North America", "C", "The Amazon Rainforest spans 9 South American countries, mostly in Brazil."),
                ("What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "C", "Canberra is the official capital city of Australia."),
                ("Which mountain range features Mount Everest, the world's highest peak?", "Andes", "Alps", "Himalayas", "Rockies", "C", "Mount Everest is in the Himalayas on the Nepal-China border."),
                ("What country has the largest total population in the world?", "India", "China", "United States", "Indonesia", "A", "India is the world's most populous country."),
                ("What sea separates Europe and Africa?", "Red Sea", "Caribbean Sea", "Mediterranean Sea", "Baltic Sea", "C", "The Mediterranean Sea connects Europe, Africa, and Asia.")
            ]
        },
        'Famous Art & Architecture': {
            'description': 'Test your knowledge on iconic paintings, world architecture monuments, and master artists.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who painted the famous Renaissance masterpiece 'Mona Lisa'?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "C", "Leonardo da Vinci painted the Mona Lisa in the early 16th century."),
                ("In which city is the iconic Eiffel Tower located?", "Berlin", "London", "Paris", "Rome", "C", "The Eiffel Tower was constructed in Paris, France for the 1889 World's Fair."),
                ("Who painted the famous Post-Impressionist work 'The Starry Night'?", "Pablo Picasso", "Vincent van Gogh", "Salvador Dali", "Edvard Munch", "B", "Vincent van Gogh painted 'The Starry Night' in June 1889."),
                ("In which Indian city is the ivory-white marble Taj Mahal mausoleum located?", "New Delhi", "Agra", "Jaipur", "Mumbai", "B", "The Taj Mahal was commissioned by Shah Jahan in Agra, India."),
                ("Who painted the ceiling of the Sistine Chapel in the Vatican?", "Leonardo da Vinci", "Raphael", "Michelangelo", "Donatello", "C", "Michelangelo painted the Sistine Chapel ceiling between 1508 and 1512."),
                ("Which ancient amphitheater landmark is located in Rome, Italy?", "Parthenon", "Colosseum", "Petra", "Chichen Itza", "B", "The Colosseum in Rome is the largest ancient amphitheater built."),
                ("Who created the famous surrealist painting featuring melting clocks ('The Persistence of Memory')?", "Salvador Dalí", "René Magritte", "Pablo Picasso", "Frida Kahlo", "A", "Salvador Dalí painted 'The Persistence of Memory' in 1931."),
                ("Which famous modernist artist co-founded the Cubism movement?", "Claude Monet", "Pablo Picasso", "Henri Matisse", "Paul Cézanne", "B", "Pablo Picasso co-founded Cubism in the early 20th century."),
                ("In which country is the ancient stone citadel Machu Picchu located?", "Bolivia", "Colombia", "Peru", "Chile", "C", "Machu Picchu is a 15th-century Inca citadel in southern Peru."),
                ("Who sculpted the famous Renaissance marble statue of 'David'?", "Michelangelo", "Donatello", "Bernini", "Rodin", "A", "Michelangelo sculpted 'David' between 1501 and 1504 in Florence.")
            ]
        },
        'Inventions & Discoveries': {
            'description': 'Learn about groundbreaking technological breakthroughs, inventors, and scientific milestones.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who is widely credited with inventing the practical incandescent light bulb?", "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", "Benjamin Franklin", "B", "Thomas Edison developed a commercially viable incandescent light bulb in 1879."),
                ("Who discovered the antibiotic Penicillin in 1928?", "Louis Pasteur", "Alexander Fleming", "Robert Koch", "Edward Jenner", "B", "Alexander Fleming discovered penicillin produced by Penicillium mold."),
                ("Who is credited with inventing the telephone in 1876?", "Guglielmo Marconi", "Alexander Graham Bell", "Thomas Edison", "Samuel Morse", "B", "Alexander Graham Bell was awarded the first US patent for the telephone."),
                ("Which brothers built and flew the first successful motor-operated airplane in 1903?", "Wright Brothers", "Montgolfier Brothers", "Packard Brothers", "Warner Brothers", "A", "Orville and Wilbur Wright achieved the first controlled powered flight at Kitty Hawk."),
                ("Who invented the movable-type printing press around 1440?", "Johannes Gutenberg", "Galileo Galilei", "Isaac Newton", "Leonardo da Vinci", "A", "Gutenberg's printing press revolutionized book production across Europe."),
                ("Who formulated the Theory of General Relativity?", "Isaac Newton", "Niels Bohr", "Albert Einstein", "Stephen Hawking", "C", "Albert Einstein published General Relativity in 1915."),
                ("Who developed the first safe smallpox vaccine in 1796?", "Louis Pasteur", "Edward Jenner", "Jonas Salk", "Alexander Fleming", "B", "Edward Jenner developed the smallpox vaccine using cowpox virus."),
                ("What electronic networking protocol breakthrough in the late 1960s formed ARPANET / early Internet?", "TCP/IP", "Ethernet", "ARPANET Packet Switching", "HTTP", "C", "ARPANET used packet switching to pioneer modern digital computer networks."),
                ("Who invented the World Wide Web (WWW) in 1989 at CERN?", "Steve Jobs", "Bill Gates", "Tim Berners-Lee", "Alan Turing", "C", "Tim Berners-Lee invented HTML, HTTP, and the World Wide Web."),
                ("Who discovered radium and polonium and won two Nobel Prizes in Physics and Chemistry?", "Lise Meitner", "Rosalind Franklin", "Marie Curie", "Ada Lovelace", "C", "Marie Curie was the first person to win two Nobel Prizes in different scientific fields.")
            ]
        },
        'World Organizations & Global Affairs': {
            'description': 'Understand global bodies: United Nations, Olympics, Nobel prizes, and international treaties.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In which city is the main headquarters of the United Nations (UN) located?", "Geneva", "London", "New York City", "Paris", "C", "The UN official headquarters has been in New York City since 1952."),
                ("How many interlocking rings appear on the official Olympic flag?", "4", "5", "6", "7", "B", "5 interlocking rings represent the five inhabited continents."),
                ("In which country are the prestigious Nobel Prizes awarded annually (except Peace)?", "Switzerland", "Sweden", "Norway", "Denmark", "B", "Nobel Prizes in Physics, Chemistry, Medicine, and Literature are awarded in Stockholm, Sweden."),
                ("Where is the Nobel Peace Prize awarded annually?", "Geneva, Switzerland", "Oslo, Norway", "Stockholm, Sweden", "The Hague, Netherlands", "B", "The Nobel Peace Prize is presented annually in Oslo, Norway."),
                ("What global financial institution has the acronym IMF?", "International Monetary Fund", "International Mercantile Foundation", "Imperial Money Forum", "Intercontinental Monetary Fund", "A", "IMF stands for International Monetary Fund."),
                ("Where is the International Court of Justice (ICJ) located?", "Geneva", "Brussels", "The Hague", "Vienna", "C", "The ICJ is seated at the Peace Palace in The Hague, Netherlands."),
                ("What agency of the United Nations is responsible for international public health?", "UNICEF", "UNESCO", "WHO", "UNHCR", "C", "WHO stands for World Health Organization."),
                ("Which international humanitarian organization uses a Red Cross or Red Crescent symbol?", "Amnesty International", "Red Cross Movement", "Greenpeace", "Doctors Without Borders", "B", "The International Red Cross and Red Crescent Movement provides humanitarian aid."),
                ("What currency is used by 20 member states of the European Union?", "Pound Sterling", "Swiss Franc", "Euro", "Krona", "C", "The Euro (€) is the official currency of the Eurozone."),
                ("What defense alliance is known by the acronym NATO?", "North Atlantic Treaty Organization", "North American Trade Organization", "National Association of Trade Officers", "New Atlantic Tactical Order", "A", "NATO stands for North Atlantic Treaty Organization.")
            ]
        },
        'Pop Culture & General Trivia': {
            'description': 'Fun trivia spanning world record breakers, cinema, global traditions, and pop culture.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("What animal is endemic to Australia and feeds almost exclusively on eucalyptus leaves?", "Kangaroo", "Koala", "Wombat", "Platypus", "B", "Koalas live in eastern Australia and eat eucalyptus leaves."),
                ("How many chemical elements are officially recognized on the standard periodic table?", "108", "112", "118", "120", "C", "The periodic table contains 118 confirmed chemical elements."),
                ("What is the largest hot desert in the world?", "Gobi Desert", "Kalahari Desert", "Sahara Desert", "Arabian Desert", "C", "The Sahara is the world's largest hot desert, covering North Africa."),
                ("What hard substance makes up human teeth and is the hardest substance in the body?", "Bone", "Enamel", "Dentin", "Keratin", "B", "Tooth enamel is the hardest tissue in the human body."),
                ("Which country is famous for inventing the martial art Karate?", "China", "Korea", "Japan", "Thailand", "C", "Karate developed on the Okinawa island of Japan."),
                ("What instrument has 88 black and white keys?", "Accordion", "Harpsichord", "Piano", "Organ", "C", "A standard modern acoustic piano has 88 keys (52 white, 36 black)."),
                ("What natural phenomenon causes the Northern Lights?", "Solar wind interacting with Earth's magnetic field", "Moon reflection on ice", "Volcanic ash", "Lightning in clouds", "A", "Aurora Borealis occurs when charged solar particles collisionally excite atmospheric gases."),
                ("How many colors make up a standard rainbow spectrum?", "5", "6", "7", "8", "C", "7 colors: Red, Orange, Yellow, Green, Blue, Indigo, Violet (ROYGBIV)."),
                ("What metal element is liquid at standard room temperature?", "Lead", "Mercury", "Copper", "Tin", "B", "Mercury (Hg) is a liquid metal at standard room temperature."),
                ("Which bird species is famous for being incapable of flight and native to Antarctica?", "Puffin", "Penguin", "Albatross", "Ostrich", "B", "Emperor penguins are flightless birds adapted to Antarctic icy waters.")
            ]
        }
    },
    'Aptitude': {
        'Logical Reasoning': {
            'description': 'Sharpen deductive logic: letter/number patterns, analogies, coding deciphering, and odd-one-out.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Identify the next number in the series: 2, 4, 8, 16, ...", "20", "24", "32", "64", "C", "Each number is multiplied by 2. 16 * 2 = 32."),
                ("If all A are B, and all B are C, which statement MUST be true?", "All C are A", "All A are C", "Some B are not C", "No A is C", "B", "By transitive logical deduction, if A ⊆ B and B ⊆ C, then A ⊆ C."),
                ("Look at this series: SCD, TEF, UGH, ___, WKL. What fills the blank?", "CMN", "UJI", "VIJ", "IJT", "C", "First letters: S, T, U, V, W. Second & third: CD, EF, GH, IJ, KL. Result: VIJ."),
                ("Which word does NOT belong with the others?", "Apple", "Banana", "Carrot", "Mango", "C", "Carrot is a root vegetable; Apple, Banana, and Mango are fruits."),
                ("Odometer is to mileage as Compass is to:", "Speed", "Hiking", "Needle", "Direction", "D", "An odometer measures mileage; a compass indicates direction."),
                ("Look at the series: 36, 34, 30, 28, 24... What number comes next?", "20", "22", "23", "26", "B", "Alternating subtract 2 then subtract 4. 24 - 2 = 22."),
                ("Melt is to Liquid as Freeze is to:", "Ice", "Solid", "Condense", "Crystal", "B", "Melting creates liquid; freezing creates solid."),
                ("Find the odd one out among these geometric figures:", "Triangle", "Square", "Circle", "Rectangle", "C", "Triangle, Square, and Rectangle have straight straight-edge polygon sides; Circle is curved."),
                ("If RED is coded numerically as 27, how is BLUE coded?", "40", "42", "45", "50", "A", "Sum of letter positions: B(2)+L(12)+U(21)+E(5) = 40."),
                ("Day is to Night as White is to:", "Black", "Color", "Dark", "Sun", "A", "Day and Night are direct antonyms; White and Black are antonyms.")
            ]
        },
        'Quantitative Aptitude': {
            'description': 'Practice distance/speed calculations, age equations, work efficiency, and interest formulas.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("A shirt costs $20 after a 20% discount. What was its original price?", "$24", "$25", "$30", "$22", "B", "Let original price be P. 0.80 * P = $20 => P = 20 / 0.8 = $25."),
                ("If a train travels at a speed of 60 mph, how far will it travel in 3.5 hours?", "180 miles", "190 miles", "210 miles", "240 miles", "C", "Distance = Speed * Time = 60 * 3.5 = 210 miles."),
                ("What is the average of numbers 10, 20, 30, 40, and 50?", "25", "30", "35", "40", "B", "Sum = 150. Count = 5. Average = 150 / 5 = 30."),
                ("If x + 7 = 15, what is the value of 2x?", "16", "14", "18", "12", "A", "x = 15 - 7 = 8. Therefore 2x = 2 * 8 = 16."),
                ("If 5 workers take 10 days to build a wall, how many days will 10 workers take at the same rate?", "5 days", "10 days", "15 days", "20 days", "A", "Worker-days required = 5 * 10 = 50. 50 / 10 workers = 5 days."),
                ("What is 20% of what number equals 10?", "40", "50", "60", "100", "B", "0.20 * N = 10 => N = 10 / 0.20 = 50."),
                ("A father is twice as old as his son. 10 years ago, he was three times as old. How old is the son now?", "15", "20", "25", "30", "B", "Son = s, Father = 2s. 10 yrs ago: 2s - 10 = 3(s - 10) => 2s - 10 = 3s - 30 => s = 20."),
                ("Calculate simple interest on $1000 at 5% annual rate for 2 years:", "$50", "$100", "$150", "$200", "B", "Interest = (P * R * T) / 100 = (1000 * 5 * 2) / 100 = $100."),
                ("A train 120m long passes a post in 6 seconds. What is its speed in km/h?", "60 km/h", "72 km/h", "80 km/h", "90 km/h", "B", "Speed = 120m / 6s = 20 m/s. Convert to km/h: 20 * 3.6 = 72 km/h."),
                ("What is the square root of 144?", "10", "11", "12", "14", "C", "12 * 12 = 144.")
            ]
        },
        'Verbal Ability': {
            'description': 'Enhance English proficiency: synonyms, antonyms, idiom definitions, and correct grammar usage.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Choose the word that is a SYNONYM for 'abundant':", "Scarce", "Plentiful", "Empty", "Rare", "B", "'Abundant' means present in great quantities (Plentiful)."),
                ("Choose the correctly spelled English word:", "Accomodate", "Acommodate", "Accommodate", "Acomodate", "C", "'Accommodate' has double 'c' and double 'm'."),
                ("Choose the word that is an ANTONYM for 'expand':", "Grow", "Shrink", "Inflate", "Extend", "B", "'Shrink' is the opposite of 'expand'."),
                ("What is the meaning of the popular idiom 'Bite the bullet'?", "Eat quickly", "Endure a painful situation bravely", "Get angry", "Start a conflict", "B", "'Bite the bullet' means facing a difficult situation with courage."),
                ("Which word in this sentence is a Noun: 'The happy child ran fast'?", "happy", "child", "ran", "fast", "B", "'Child' is a person/noun."),
                ("Choose the word that is a SYNONYM for 'benevolent':", "Cruel", "Kind", "Hostile", "Selfish", "B", "'Benevolent' means well-meaning and kind."),
                ("Complete the sentence correctly: 'She is very proficient ___ mathematics.'", "in", "on", "at", "with", "C", "The standard preposition phrase is 'proficient at' (or 'in'). 'at' is correct here."),
                ("Choose the word that is an ANTONYM for 'obscure':", "Hidden", "Clear", "Vague", "Secret", "B", "'Clear' is the opposite of 'obscure'."),
                ("What is the correct plural form of 'mouse' (animal)?", "Mouses", "Mice", "Meese", "Mices", "B", "The plural of mouse is mice."),
                ("What does the idiom 'A piece of cake' mean?", "A sweet dessert", "Something very easy to do", "A small fraction", "A difficult choice", "B", "'A piece of cake' refers to a task that is effortless.")
            ]
        },
        'Data Interpretation': {
            'description': 'Interpret pie charts, percentage changes, margin gains, and chart data tables.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("If a circular pie chart is divided into 4 equal slices, what angle does each slice represent?", "45°", "90°", "180°", "120°", "B", "360° / 4 = 90°."),
                ("If company sales decrease from 100 units to 50 units, what is the percentage decrease?", "25%", "50%", "75%", "100%", "B", "((100 - 50) / 100) * 100 = 50%."),
                ("If company profits double every year starting at $1000 in Year 1, what is profit in Year 3?", "$2000", "$3000", "$4000", "$8000", "C", "Year 1 = $1000, Year 2 = $2000, Year 3 = $4000."),
                ("What is the arithmetic average of numbers [2, 4, 6, 8]?", "4", "5", "6", "8", "B", "Sum = 20. Count = 4. Average = 20 / 4 = 5."),
                ("If a bar chart displays three columns of heights 10, 20, and 30, what is their combined total?", "40", "50", "60", "70", "C", "10 + 20 + 30 = 60."),
                ("A product sells for $100 with a 20% profit margin on revenue. What was the cost to make it?", "$20", "$80", "$100", "$120", "B", "Profit = $20. Cost = Revenue - Profit = $100 - $20 = $80."),
                ("If a stock index drops by 10% on Monday and rises by 10% on Tuesday, its final value is:", "Higher than initial", "Lower than initial", "Identical to initial", "Cannot be determined", "B", "100 -> drops 10% to 90 -> rises 10% of 90 (9) to 99 (1% lower than 100)."),
                ("In a school class of 50 students, 60% are boys. How many girls are in the class?", "20", "30", "40", "10", "A", "Girls percentage = 40%. 40% of 50 = 20 girls."),
                ("A pie chart slice represents 25% of budget for Rent. What fraction is this?", "1/2", "1/3", "1/4", "1/5", "C", "25 / 100 = 1/4."),
                ("If revenue grows linearly from $100 to $200 over 5 years, what is the annual growth amount?", "$10", "$20", "$25", "$50", "B", "Total growth = $100. Over 5 years = $100 / 5 = $20 per year.")
            ]
        },
        'Puzzles & Brain Teasers': {
            'description': 'Solve classic logical riddles, time/clock angle puzzles, and lateral thinking teasers.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("At exactly 3:00, what is the angle between the hour hand and the minute hand of a clock?", "45°", "60°", "90°", "120°", "C", "Clock face is 360°. 12 hours = 30° per hour. At 3:00, 3 * 30° = 90°."),
                ("I speak without a mouth and hear without ears. I have no body, but come alive with wind. What am I?", "A ghost", "An echo", "A shadow", "A cloud", "B", "An echo relies on sound waves reflecting."),
                ("What item has keys but cannot open any door locks?", "A piano", "A map", "A treasure chest", "A clock", "A", "A piano has musical keys."),
                ("What gets wetter and wetter the more it dries?", "A sponge", "A cloud", "A towel", "Water", "C", "A towel absorbs moisture as it dries your body."),
                ("What must be broken before you can cook or use it?", "A glass", "A promise", "An egg", "A lock", "C", "An eggshell must be cracked/broken to consume."),
                ("If a doctor gives you 3 pills and tells you to take one every 30 minutes, how long do they last?", "1.5 hours", "1 hour", "2 hours", "30 minutes", "B", "Take Pill 1 at 0 min, Pill 2 at 30 min, Pill 3 at 60 min (total 1 hour)."),
                ("What has a head and a tail, but no body?", "A snake", "A coin", "A comet", "A rope", "B", "A standard coin has heads and tails sides."),
                ("A clock strikes once at 1 o'clock, twice at 2 o'clock, and so on. How many total strikes in 12 hours?", "12", "72", "78", "144", "C", "Sum 1 to 12 = (12 * 13) / 2 = 78 total strikes."),
                ("If 5 machines take 5 minutes to make 5 widgets, how long for 100 machines to make 100 widgets?", "100 minutes", "5 minutes", "20 minutes", "1 minute", "B", "1 machine takes 5 minutes to make 1 widget. 100 machines working simultaneously take 5 minutes."),
                ("What building has the most stories?", "A skyscraper", "A library", "A hospital", "A museum", "B", "A library contains thousands of written stories (books).")
            ]
        }
    },
    'History': {
        'Ancient Civilizations': {
            'description': 'Journey through ancient Egypt, Mesopotamia, Indus Valley, Roman Republic, and Classical Greece.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who was the first official Emperor of the Roman Empire?", "Julius Caesar", "Augustus", "Nero", "Marcus Aurelius", "B", "Augustus (Octavian) became the first Emperor of Rome in 27 BC."),
                ("Which ancient civilization constructed the Pyramids and Sphinx of Giza?", "Mesopotamia", "Ancient Egypt", "Indus Valley", "Persia", "B", "Ancient Egyptians constructed Giza monuments during the Old Kingdom."),
                ("Between which two rivers did ancient Mesopotamia flourish ('land between rivers')?", "Nile and Amazon", "Tigris and Euphrates", "Indus and Ganges", "Yellow and Yangtze", "B", "Mesopotamia lay between the Tigris and Euphrates rivers."),
                ("Which famous ancient Greek philosopher was the teacher of Alexander the Great?", "Socrates", "Plato", "Aristotle", "Pythagoras", "C", "Aristotle tutored young Alexander the Great in Macedonia."),
                ("What ancient legal code from Babylon is famous for 'an eye for an eye'?", "Justinian Code", "Magna Carta", "Code of Hammurabi", "Twelve Tables", "C", "King Hammurabi of Babylon enacted the Code of Hammurabi c. 1750 BC."),
                ("Who was the famous Queen of Egypt who formed alliances with Julius Caesar and Mark Antony?", "Nefertiti", "Cleopatra", "Hatshepsut", "Sobekneferu", "B", "Cleopatra VII Philopator was the last active ruler of Ptolemaic Egypt."),
                ("Which city-state was the principal rival of Athens during the Peloponnesian War?", "Sparta", "Corinth", "Thebes", "Troy", "A", "Sparta led the Peloponnesian League against the Delian League led by Athens."),
                ("What ancient overland trade network connected Han Dynasty China with Europe?", "Amber Road", "Spice Route", "Silk Road", "Incense Route", "C", "The Silk Road facilitated trade and cultural exchange across Eurasia."),
                ("Which Roman general crossed the Rubicon river in 49 BC and became dictator of Rome?", "Mark Antony", "Julius Caesar", "Scipio Africanus", "Pompey", "B", "Julius Caesar crossed the Rubicon initiating civil war."),
                ("The ancient Olympic Games originated in which country?", "Italy", "Egypt", "Greece", "Persia", "C", "The ancient Olympic Games were held at Olympia in Greece starting in 776 BC.")
            ]
        },
        'World War I & II': {
            'description': 'Examine global conflicts of the 20th century: causes, major battles, dates, and peace treaties.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In which year did World War II officially end?", "1918", "1945", "1939", "1950", "B", "WWII ended in 1945 following the surrender of Axis forces."),
                ("The assassination of Archduke Franz Ferdinand in 1914 triggered which conflict?", "Crimean War", "World War I", "Franco-Prussian War", "World War II", "B", "Archduke Franz Ferdinand's assassination in Sarajevo ignited World War I."),
                ("What treaty formally concluded World War I in 1919?", "Treaty of Paris", "Treaty of Versailles", "Treaty of Ghent", "Treaty of Utrecht", "B", "The Treaty of Versailles was signed on June 28, 1919."),
                ("Which surprise military strike prompted the United States to enter World War II in 1941?", "Battle of Midway", "Pearl Harbor Attack", "D-Day Invasion", "Battle of the Bulge", "B", "Japan's attack on Pearl Harbor on Dec 7, 1941 brought the US into WWII."),
                ("What military code name was given to the Allied Normandy landings on June 6, 1944?", "Operation Barbarossa", "Operation Market Garden", "Operation Overlord (D-Day)", "Operation Torch", "C", "Operation Overlord was the Allied invasion of Normandy (D-Day)."),
                ("Who was the Prime Minister of Great Britain during most of World War II?", "Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Woodrow Wilson", "B", "Winston Churchill led Britain as Prime Minister from 1940 to 1945."),
                ("Which three major powers formed the principal Axis Powers in World War II?", "US, UK, USSR", "Germany, Italy, Japan", "France, Britain, Russia", "Germany, Austria, Turkey", "B", "Germany, Italy, and Japan signed the Tripartite Pact forming the Axis."),
                ("In which country did the brutal 1942-1943 Battle of Stalingrad take place?", "Germany", "Poland", "Soviet Union (USSR)", "France", "C", "Stalingrad (now Volgograd) was a decisive battle in the Soviet Union."),
                ("What international body was established immediately following World War II to maintain peace?", "League of Nations", "United Nations", "NATO", "European Union", "B", "The United Nations was chartered in October 1945."),
                ("In what year did World War I start?", "1914", "1917", "1939", "1912", "A", "World War I broke out in July 1914.")
            ]
        },
        'Medieval & Renaissance Era': {
            'description': 'Explore feudal Europe, Magna Carta, Renaissance rebirth of art, Crusades, and Silk Road trade.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In which century was the Magna Carta signed in England (1215)?", "11th Century", "13th Century", "15th Century", "17th Century", "B", "King John signed Magna Carta at Runnymede in 1215 (13th century)."),
                ("What devasting pandemic killed an estimated 30-60% of Europe's population in the 14th century?", "Spanish Flu", "Black Death (Plague)", "Cholera", "Smallpox", "B", "The Black Death bubonic plague swept Europe from 1346 to 1353."),
                ("Which Italian city is widely regarded as the birthplace of the Renaissance movement?", "Rome", "Venice", "Florence", "Milan", "C", "Florence was the epicenter of early Renaissance art and humanism."),
                ("Who was the Joan of Arc, the famed heroine of France during the Hundred Years' War?", "A French Queen", "A peasant girl who led French troops", "A naval admiral", "An Italian painter", "B", "Joan of Arc rallied French forces against English troops before being martyred."),
                ("What military campaigns were waged by Western European Christians to reclaim the Holy Land?", "The Crusades", "The Punic Wars", "The Napoleonic Wars", "The Thirty Years' War", "A", "The Crusades were religious wars sanctioned by the Latin Church."),
                ("Who painted the famous School of Athens fresco in the Vatican?", "Leonardo da Vinci", "Raphael", "Donatello", "Titian", "B", "Raphael painted The School of Athens between 1509 and 1511."),
                ("Which Venetian merchant traveler wrote a famous book chronicling his travels across Asia and China?", "Christopher Columbus", "Marco Polo", "Vasco da Gama", "Ferdinand Magellan", "B", "Marco Polo documented Asian trade routes and Kublai Khan's court."),
                ("What empire fell when Constantinople was captured by Sultan Mehmed II in 1453?", "Roman Empire", "Byzantine Empire", "Holy Roman Empire", "Ottoman Empire", "B", "The fall of Constantinople marked the end of the Byzantine Empire."),
                ("Who started the Protestant Reformation in 1517 by posting his Ninety-five Theses?", "John Calvin", "Martin Luther", "Henry VIII", "Erasmus", "B", "Martin Luther nailed his 95 Theses to the Wittenberg church door."),
                ("What European era translates literally to 'Rebirth' in French?", "Enlightenment", "Renaissance", "Baroque", "Middle Ages", "B", "Renaissance means 'Rebirth' of classical learning and culture.")
            ]
        },
        'American & European History': {
            'description': 'Cover the French Revolution, American Independence, Industrial Revolution, and Cold War era.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In which year did the French Revolution begin with the storming of the Bastille?", "1776", "1789", "1812", "1848", "B", "The French Revolution began in 1789."),
                ("Who served as the first President of the United States from 1789 to 1797?", "Thomas Jefferson", "George Washington", "John Adams", "Benjamin Franklin", "B", "George Washington was the first US President."),
                ("Which French military leader crowned himself Emperor of the French in 1804?", "Louis XIV", "Napoleon Bonaparte", "Charles de Gaulle", "Louis XVI", "B", "Napoleon Bonaparte ruled as Emperor until 1815."),
                ("In what year was the United States Declaration of Independence adopted?", "1776", "1789", "1792", "1801", "A", "The Continental Congress adopted the Declaration of Independence on July 4, 1776."),
                ("What major historical transformation began in Britain during the 18th century involving steam power and factories?", "Digital Revolution", "Industrial Revolution", "Agricultural Revolution", "Scientific Revolution", "B", "The Industrial Revolution mechanized manufacturing and transport."),
                ("Which US President issued the Emancipation Proclamation in 1863 during the Civil War?", "George Washington", "Abraham Lincoln", "Ulysses S. Grant", "Andrew Jackson", "B", "Abraham Lincoln declared freedom for enslaved people in Confederate states."),
                ("What concrete barrier divided Berlin from 1961 until its fall in 1989?", "Iron Curtain", "Berlin Wall", "Maginot Line", "Siegfried Line", "B", "The Berlin Wall symbolized the Cold War division of Europe."),
                ("Who was the British monarch who reigned during the height of the British Empire for 63 years (1837-1901)?", "Queen Elizabeth I", "Queen Victoria", "Queen Mary", "Queen Anne", "B", "Queen Victoria ruled during the Victorian Era."),
                ("Which conflict pitted North and South Korea against each other from 1950 to 1953?", "Vietnam War", "Korean War", "Pacific War", "Cold War", "B", "The Korean War ended in an armistice establishing the DMZ in 1953."),
                ("What 1962 confrontation brought the US and USSR to the brink of nuclear war?", "Suez Crisis", "Cuban Missile Crisis", "Berlin Blockade", "Prague Spring", "B", "The Cuban Missile Crisis resolved after intense 13-day nuclear standoff.")
            ]
        },
        'Famous Historical Figures': {
            'description': 'Test your knowledge on influential historical leaders, conquerors, and peace advocates.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which Macedonian ruler created one of the largest empires in ancient history by age 30?", "Julius Caesar", "Alexander the Great", "Xerxes", "Charlemagne", "B", "Alexander the Great conquered the Persian Empire and expanded to India."),
                ("Who led India's non-violent independence movement against British rule?", "Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "B.R. Ambedkar", "B", "Mahatma Gandhi championed non-violent civil disobedience (Satyagraha)."),
                ("Which Mongol leader founded the Mongol Empire in 1206?", "Kublai Khan", "Genghis Khan", "Tamerlane", "Attila the Hun", "B", "Genghis Khan unified Mongol tribes to build a massive Eurasian empire."),
                ("Who was the leader of the Civil Rights Movement in the US famous for his 'I Have a Dream' speech?", "Malcolm X", "Martin Luther King Jr.", "Frederick Douglass", "Rosa Parks", "B", "Martin Luther King Jr. delivered his speech in Washington in 1963."),
                ("Which South African anti-apartheid leader served as President of South Africa from 1994 to 1999?", "Desmond Tutu", "Nelson Mandela", "Thabo Mbeki", "Steve Biko", "B", "Nelson Mandela spent 27 years imprisoned before becoming President."),
                ("Who was the Ottoman Sultan known as 'the Magnificent' during the empire's golden age?", "Mehmed II", "Suleiman I", "Selim I", "Osman I", "B", "Suleiman the Magnificent ruled the Ottoman Empire from 1520 to 1566."),
                ("Which French heroine rallied troops at the Siege of Orléans during the Hundred Years' War?", "Marie Antoinette", "Joan of Arc", "Catherine de' Medici", "Charlotte Corday", "B", "Joan of Arc lifted the Siege of Orléans in 1429."),
                ("Who was the Carthaginian general famous for leading war elephants across the Alps against Rome?", "Hamilcar Barca", "Hannibal Barca", "Hasdrubal", "Scipio", "B", "Hannibal Barca invaded Italy during the Second Punic War."),
                ("Which British leader won the Battle of Trafalgar against Franco-Spanish fleets in 1805?", "Duke of Wellington", "Admiral Horatio Nelson", "Winston Churchill", "Oliver Cromwell", "B", "Admiral Lord Nelson led the Royal Navy to victory at Trafalgar."),
                ("Who was the founder and first Emperor of the Qin Dynasty who unified China in 221 BC?", "Qin Shi Huang", "Han Wudi", "Tang Taizong", "Sun Tzu", "A", "Qin Shi Huang unified China and initiated construction of the Great Wall.")
            ]
        }
    },
    'Literature': {
        'Shakespeare & Classic Drama': {
            'description': 'Master William Shakespeare plays: Hamlet, Romeo and Juliet, Macbeth, Othello, and sonnets.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who wrote the classic tragedy play 'Romeo and Juliet'?", "William Shakespeare", "Christopher Marlowe", "John Milton", "Geoffrey Chaucer", "A", "William Shakespeare wrote Romeo and Juliet early in his career."),
                ("Which Shakespeare play features the famous soliloquy line: 'To be, or not to be: that is the question'?", "Macbeth", "Hamlet", "Othello", "King Lear", "B", "Hamlet delivers this philosophical soliloquy in Act III, Scene 1."),
                ("Which Shakespearean play is known colloquially as 'The Scottish Play' by theater actors?", "Julius Caesar", "Macbeth", "The Tempest", "Coriolanus", "B", "Superstition leads actors to call Macbeth 'The Scottish Play'."),
                ("What was the name of the famous London playhouse associated with William Shakespeare?", "The Rose", "The Globe Theatre", "The Swan", "The Curtain", "B", "The Globe Theatre was built in 1599 by Shakespeare's playing company."),
                ("In 'Romeo and Juliet', what are the family names of the two feuding households?", "Montague and Capulet", "Bennet and Darcy", "Lannister and Stark", "Morel and Sinico", "A", "Romeo Montague and Juliet Capulet belong to the feuding families."),
                ("Which character is the villainous, manipulative antagonist in Shakespeare's 'Othello'?", "Cassio", "Iago", "Roderigo", "Brutus", "B", "Iago deceitfully plots against Othello throughout the play."),
                ("In which play does the character Puck (Robin Goodfellow) cause magical romantic mischief?", "Twelfth Night", "A Midsummer Night's Dream", "As You Like It", "Much Ado About Nothing", "B", "Puck applies a love potion in A Midsummer Night's Dream."),
                ("How many lines are in a traditional Shakespearean sonnet?", "12", "14", "16", "10", "B", "A Shakespearean sonnet consists of 14 lines in iambic pentameter."),
                ("Which Shakespearean tragedy centers on a king who divides his kingdom among his three daughters?", "King Lear", "Julius Caesar", "Richard III", "Antony and Cleopatra", "A", "King Lear tests the devotion of Goneril, Regan, and Cordelia."),
                ("What is the setting for Shakespeare's comedy 'Twelfth Night'?", "Venice", "Illyria", "Verona", "Athens", "B", "Twelfth Night is set in the kingdom of Illyria.")
            ]
        },
        'Famous Novels & Fiction': {
            'description': 'Test your memory of famous novels: To Kill a Mockingbird, 1984, Pride and Prejudice, Great Gatsby.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who wrote the dystopian novel '1984' published in 1949?", "Aldous Huxley", "George Orwell", "Ray Bradbury", "H.G. Wells", "B", "George Orwell wrote 1984 as a warning against totalitarianism."),
                ("Who is the author of the Pulitzer Prize-winning novel 'To Kill a Mockingbird'?", "F. Scott Fitzgerald", "Harper Lee", "Ernest Hemingway", "John Steinbeck", "B", "Harper Lee published To Kill a Mockingbird in 1960."),
                ("Who wrote the 1813 romantic novel of manners 'Pride and Prejudice'?", "Charlotte Brontë", "Emily Brontë", "Jane Austen", "George Eliot", "C", "Jane Austen authored Pride and Prejudice following Elizabeth Bennet's story."),
                ("Who wrote the 1925 novel 'The Great Gatsby' set in the Roaring Twenties?", "F. Scott Fitzgerald", "Ernest Hemingway", "William Faulkner", "John Dos Passos", "A", "F. Scott Fitzgerald depicted Jay Gatsby and the American Dream."),
                ("In Herman Melville's novel 'Moby-Dick', what kind of creature is Moby Dick?", "Giant Squid", "White Sperm Whale", "Great White Shark", "Kraken", "B", "Moby Dick is an elusive white sperm whale pursued by Captain Ahab."),
                ("Who is the author of 'The Catcher in the Rye' featuring narrator Holden Caulfield?", "J.D. Salinger", "Jack Kerouac", "Truman Capote", "John Updike", "A", "J.D. Salinger published The Catcher in the Rye in 1951."),
                ("Which novel begins with the iconic line: 'Call me Ishmael'?", "Treasure Island", "Moby-Dick", "The Old Man and the Sea", "Robinson Crusoe", "B", "Ishmael opens Herman Melville's Moby-Dick."),
                ("Who authored the epic fantasy series 'The Lord of the Rings'?", "C.S. Lewis", "J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "B", "J.R.R. Tolkien wrote The Hobbit and The Lord of the Rings."),
                ("Which Charles Dickens novel features the miserly character Ebenezer Scrooge?", "Oliver Twist", "A Christmas Carol", "Great Expectations", "David Copperfield", "B", "Ebenezer Scrooge is visited by ghosts in A Christmas Carol (1843)."),
                ("Who wrote 'The Grapes of Wrath' about Dust Bowl migrant workers?", "Ernest Hemingway", "John Steinbeck", "William Faulkner", "Sinclair Lewis", "B", "John Steinbeck won the Pulitzer Prize for The Grapes of Wrath.")
            ]
        },
        'Poetry & Famous Poets': {
            'description': 'Explore timeless poetry: Robert Frost, Emily Dickinson, Edgar Allan Poe, Wordsworth, and poetic meters.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who wrote the famous poem 'The Road Not Taken' ('Two roads diverged in a yellow wood')?", "Walt Whitman", "Robert Frost", "Langston Hughes", "Ezra Pound", "B", "Robert Frost published 'The Road Not Taken' in 1916."),
                ("Which macabre poem features a haunting bird repeating the single word 'Nevermore'?", "The Raven", "Annabel Lee", "Ode to a Nightingale", "The Tyger", "A", "Edgar Allan Poe published 'The Raven' in 1845."),
                ("Which American poet is famous for writing un-conventional punctuation and capitalization ('Hope is the thing with feathers')?", "Sylvia Plath", "Emily Dickinson", "Maya Angelou", "Christina Rossetti", "B", "Emily Dickinson wrote hundreds of distinctive, dash-punctuated poems."),
                ("Who wrote the Romantic poem 'I Wandered Lonely as a Cloud' (Daffodils)?", "Lord Byron", "John Keats", "William Wordsworth", "Percy Bysshe Shelley", "C", "William Wordsworth authored 'I Wandered Lonely as a Cloud'."),
                ("What Japanese traditional poetic form consists of 3 lines with a 5-7-5 syllable structure?", "Sonnet", "Limerick", "Haiku", "Tanka", "C", "A Haiku consists of 17 total syllables across three lines (5, 7, 5)."),
                ("Who wrote the epic 17th-century blank verse poem 'Paradise Lost'?", "John Milton", "Geoffrey Chaucer", "John Donne", "Alexander Pope", "A", "John Milton published 'Paradise Lost' in 1667 depicting the Fall of Man."),
                ("Which famous English poet wrote 'Ode to a Nightingale' and 'Ode on a Grecian Urn'?", "John Keats", "William Blake", "Samuel Taylor Coleridge", "Lord Byron", "A", "John Keats composed his famous Odes in 1819."),
                ("Who wrote the celebrated American poetry collection 'Leaves of Grass'?", "Walt Whitman", "Ralph Waldo Emerson", "Henry Wadsworth Longfellow", "T.S. Eliot", "A", "Walt Whitman self-published 'Leaves of Grass' in 1855."),
                ("What metrical pattern consists of 5 feet of unstressed followed by stressed syllables (da-DUM da-DUM)?", "Trochaic Tetrameter", "Iambic Pentameter", "Anapestic Trimeter", "Dactylic Hexameter", "B", "Iambic pentameter features 10 syllables per line with alternating stress."),
                ("Who wrote 'The Rime of the Ancient Mariner' featuring an albatross?", "Samuel Taylor Coleridge", "William Wordsworth", "Percy Shelley", "John Keats", "A", "Samuel Taylor Coleridge published this ballad in 1798.")
            ]
        },
        'World Authors & Masterpieces': {
            'description': 'Survey world literary giants: Leo Tolstoy, Dostoevsky, Victor Hugo, Homer, and Gabriel García Márquez.',
            'difficulty': 'Hard',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who wrote the epic Russian masterpiece novel 'War and Peace'?", "Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Vladimir Nabokov", "B", "Leo Tolstoy published War and Peace in 1869."),
                ("Which ancient Greek poet is traditionally attributed as the author of 'The Iliad' and 'The Odyssey'?", "Hesiod", "Homer", "Sophocles", "Euripides", "B", "Homer is credited with composing the epic Trojan War poems."),
                ("Who authored the Russian novel 'Crime and Punishment' featuring Raskolnikov?", "Leo Tolstoy", "Fyodor Dostoevsky", "Ivan Turgenev", "Nikolai Gogol", "B", "Fyodor Dostoevsky published Crime and Punishment in 1866."),
                ("Who wrote the French masterpiece 'Les Misérables' and 'The Hunchback of Notre-Dame'?", "Gustave Flaubert", "Victor Hugo", "Émile Zola", "Alexandre Dumas", "B", "Victor Hugo authored both Les Misérables and Notre-Dame de Paris."),
                ("Which Colombian author won the Nobel Prize for his magical realism novel 'One Hundred Years of Solitude'?", "Mario Vargas Llosa", "Gabriel García Márquez", "Jorge Luis Borges", "Pablo Neruda", "B", "Gabriel García Márquez published Cien años de soledad in 1967."),
                ("Who wrote the 14th-century Italian epic poem 'The Divine Comedy' (Inferno, Purgatorio, Paradiso)?", "Petrarch", "Boccaccio", "Dante Alighieri", "Machiavelli", "C", "Dante Alighieri composed The Divine Comedy."),
                ("Who wrote the early 17th-century Spanish masterpiece 'Don Quixote'?", "Miguel de Cervantes", "Lope de Vega", "Federico García Lorca", "Calderón", "A", "Miguel de Cervantes published Don Quixote in two parts (1605/1615)."),
                ("Who wrote the French adventure novels 'The Count of Monte Cristo' and 'The Three Musketeers'?", "Victor Hugo", "Alexandre Dumas", "Honoré de Balzac", "Jules Verne", "B", "Alexandre Dumas authored these popular swashbuckling adventures."),
                ("Which French philosopher wrote the satirical novella 'Candide' in 1759?", "Jean-Jacques Rousseau", "Voltaire", "Montesquieu", "René Descartes", "B", "Voltaire wrote Candide to lampoon Leibnizian optimism."),
                ("Who authored the ancient Indian Sanskrit epic 'Mahabharata'?", "Kalidasa", "Vyasa", "Valmiki", "Chanakya", "B", "Sage Vyasa is traditionally credited as author of the Mahabharata.")
            ]
        },
        'Dystopian & Sci-Fi Literature': {
            'description': 'Explore speculative classics: Frankenstein, Brave New World, Fahrenheit 451, HG Wells, and Jules Verne.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Who wrote the gothic science-fiction novel 'Frankenstein; or, The Modern Prometheus'?", "Mary Shelley", "Bram Stoker", "Edgar Allan Poe", "Jane Austen", "A", "Mary Shelley published Frankenstein in 1818 at age 20."),
                ("Who wrote the 1932 dystopian novel 'Brave New World'?", "George Orwell", "Aldous Huxley", "Ray Bradbury", "Philip K. Dick", "B", "Aldous Huxley authored Brave New World depicting World State conditioning."),
                ("Who wrote 'Fahrenheit 451', a dystopian novel about a future where books are burned?", "Ray Bradbury", "Isaac Asimov", "Arthur C. Clarke", "Robert Heinlein", "A", "Ray Bradbury published Fahrenheit 451 in 1953."),
                ("Who wrote the Victorian sci-fi classics 'The Time Machine' and 'The War of the Worlds'?", "H.G. Wells", "Jules Verne", "Mary Shelley", "Sir Arthur Conan Doyle", "A", "H.G. Wells pioneered science fiction themes of time travel and alien invasion."),
                ("Which French pioneer wrote 'Twenty Thousand Leagues Under the Sea' and 'Journey to the Center of the Earth'?", "H.G. Wells", "Jules Verne", "Victor Hugo", "Alexandre Dumas", "B", "Jules Verne authored Extraordinary Voyages adventure novels."),
                ("Which Isaac Asimov series features the mathematical concept of 'Psychohistory' to predict empire collapse?", "Dune", "Foundation", "Ender's Game", "Hyperion", "B", "Isaac Asimov wrote the Foundation Series centered on Hari Seldon."),
                ("Who wrote the 1965 epic science fiction novel 'Dune' set on desert planet Arrakis?", "Frank Herbert", "Philip K. Dick", "Arthur C. Clarke", "Ursula K. Le Guin", "A", "Frank Herbert authored Dune, one of the best-selling sci-fi novels ever."),
                ("Who wrote 'Do Androids Dream of Electric Sheep?', which inspired the film Blade Runner?", "Philip K. Dick", "William Gibson", "Isaac Asimov", "Ray Bradbury", "A", "Philip K. Dick published the dystopian novel in 1968."),
                ("Who authored the cyber-punk classic 1984 novel 'Neuromancer' that coined the term 'Cyberspace'?", "William Gibson", "Neal Stephenson", "Bruce Sterling", "Philip K. Dick", "A", "William Gibson published Neuromancer in 1984."),
                ("In George Orwell's '1984', what is the name of the omnipresent political leader figurehead?", "The Controller", "Big Brother", "The Commander", "The Archon", "B", "Big Brother symbolizes total surveillance and party power.")
            ]
        }
    },
    'Sports': {
        'Soccer & FIFA World Cup': {
            'description': 'Test your knowledge on FIFA World Cup history, tournament rules, legendary players, and clubs.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which country hosted and won the first-ever FIFA World Cup in 1930?", "Brazil", "Argentina", "Uruguay", "Italy", "C", "Uruguay won the inaugural 1930 FIFA World Cup defeating Argentina 4-2."),
                ("Which country has won the most FIFA Men's World Cup titles in history (5 titles)?", "Germany", "Italy", "Brazil", "Argentina", "C", "Brazil has won 5 FIFA World Cup titles (1958, 1962, 1970, 1994, 2002)."),
                ("How many outfield players plus goalkeeper make up one team on a standard soccer pitch?", "9 players", "10 players", "11 players", "12 players", "C", "A soccer match is played between two teams of 11 players each."),
                ("How long is a standard professional soccer match excluding extra time?", "80 minutes", "90 minutes", "100 minutes", "60 minutes", "B", "A standard match consists of two 45-minute halves (90 minutes total)."),
                ("Which card color is shown by the referee to instantly expel a player from a match?", "Yellow Card", "Red Card", "Green Card", "Blue Card", "B", "A Red Card results in immediate ejection from the match."),
                ("Which legendary Brazilian player won 3 FIFA World Cup tournaments (1958, 1962, 1970)?", "Diego Maradona", "Pelé", "Ronaldo Nazário", "Zico", "B", "Pelé is the only player to win 3 FIFA World Cups."),
                ("Which country won the 2022 FIFA Men's World Cup in Qatar?", "France", "Croatia", "Argentina", "Morocco", "C", "Argentina won the 2022 World Cup led by Lionel Messi."),
                ("What term describes a single player scoring 3 goals in a single match?", "Brace", "Hat-trick", "Grand Slam", "Triple Play", "B", "Scoring 3 goals in one game is called a Hat-trick."),
                ("What major club competition features the top European football clubs annually?", "Copa Libertadores", "UEFA Champions League", "MLS Cup", "AFC Champions League", "B", "The UEFA Champions League is Europe's premier club tournament."),
                ("What rule prevents attacking players from hovering behind the last defender before receiving a pass?", "Handball rule", "Offside rule", "Substitutions rule", "Corner rule", "B", "The offside rule penalizes attackers nearer to the opponent goal line than the ball and second-last opponent.")
            ]
        },
        'Basketball & NBA History': {
            'description': 'Cover NBA records, legendary players (Jordan, LeBron), rules, dunks, and court dimensions.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In basketball, how many points is a shot made from beyond the designated arc worth?", "1 point", "2 points", "3 points", "4 points", "C", "Field goals made beyond the 3-point arc earn 3 points."),
                ("Which NBA player scored an astonishing 100 points in a single game in 1962?", "Kareem Abdul-Jabbar", "Wilt Chamberlain", "Michael Jordan", "Kobe Bryant", "B", "Wilt Chamberlain scored 100 points for Philadelphia against NY Knicks."),
                ("Which team won 6 NBA Championships in the 1990s led by Michael Jordan?", "LA Lakers", "Boston Celtics", "Chicago Bulls", "Detroit Pistons", "C", "Chicago Bulls won two 3-peats (1991-93, 1996-98)."),
                ("Who is the NBA's all-time leading career scorer (surpassing Kareem Abdul-Jabbar)?", "Kobe Bryant", "LeBron James", "Karl Malone", "Michael Jordan", "B", "LeBron James broke the all-time scoring record in February 2023."),
                ("How high off the floor is a standard regulation NBA basketball rim mounted?", "9 feet", "10 feet", "11 feet", "12 feet", "B", "Regulation basketball hoops are mounted 10 feet (3.05 m) high."),
                ("How many total players from both teams combined are on the court during play?", "8", "10", "12", "14", "B", "5 players per team = 10 active players on court."),
                ("What type of explosive shot occurs when a player jumps and slams the ball directly down through the hoop?", "Layup", "Hook Shot", "Slam Dunk", "Float Shot", "C", "A Slam Dunk involves forcefully thrusting the ball through the basket."),
                ("How many seconds does an NBA team have to attempt a shot that hits the rim?", "14 seconds", "24 seconds", "30 seconds", "35 seconds", "B", "The NBA shot clock limit is 24 seconds."),
                ("Which franchise shares the record for the most total NBA Championships (17 titles) alongside Boston Celtics?", "Chicago Bulls", "Golden State Warriors", "Los Angeles Lakers", "San Antonio Spurs", "C", "Both the Lakers and Celtics have won 17 NBA Championships."),
                ("What penalty is awarded when a player is fouled in the act of shooting?", "Corner throw", "Free Throws", "Penalty kick", "Turnover", "B", "Fouled shooters are awarded 2 or 3 un-contested Free Throws worth 1 point each.")
            ]
        },
        'Tennis & Grand Slams': {
            'description': 'Master Grand Slam tournaments: Wimbledon, US Open, French Open, Australian Open, and tennis scoring.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("Which male tennis player holds the record for the most Grand Slam singles titles (24 titles)?", "Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras", "C", "Novak Djokovic has won 24 Men's Grand Slam singles titles."),
                ("Which famous Grand Slam tournament is played exclusively on traditional grass courts?", "Australian Open", "French Open (Roland Garros)", "Wimbledon", "US Open", "C", "Wimbledon is played on grass courts in London."),
                ("On what surface court is the French Open (Roland-Garros) played?", "Hard court", "Clay court", "Grass court", "Carpet court", "B", "Roland Garros is played on red clay courts."),
                ("In standard tennis scoring, what score value follows '30' within a game?", "35", "40", "45", "Game", "B", "Points progress: 15, 30, 40, Game."),
                ("What tennis term describes a score tie at 40-40 within a game?", "Love", "Deuce", "Fault", "Break", "B", "A 40-40 score is called Deuce, requiring 2 consecutive points to win."),
                ("What word represents a zero score in tennis terminology?", "Zero", "Nil", "Love", "Blank", "C", "Zero points in tennis is called 'Love' (e.g. 15-Love)."),
                ("Which female player won 23 Grand Slam singles titles in the Open Era?", "Steffi Graf", "Serena Williams", "Martina Navratilova", "Chris Evert", "B", "Serena Williams won 23 Open Era singles titles."),
                ("What is the term for a serve that lands legally in the service box without being touched by the opponent?", "Ace", "Smash", "Volley", "Let", "A", "An Ace is a winning serve untouched by the receiver."),
                ("Which surface is used for the US Open and Australian Open tournaments?", "Grass", "Clay", "Hard Court (Acrylic)", "Wood", "C", "Both Australian Open and US Open are played on hard courts."),
                ("How many games must a player win to claim a standard tennis set (with a 2-game margin)?", "4 games", "6 games", "8 games", "10 games", "B", "A player must win at least 6 games to win a standard set.")
            ]
        },
        'Olympic Games & Athletics': {
            'description': 'Explore ancient & modern Olympic history, track and field world records, and marathon distances.',
            'difficulty': 'Easy',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("How long is an official athletic marathon race in miles?", "24.5 miles", "26.2 miles (42.195 km)", "28.0 miles", "30.0 miles", "B", "Official marathon distance is 26 miles 385 yards (~26.2 miles)."),
                ("Who holds the men's 100m world sprint record of 9.58 seconds set in 2009?", "Carl Lewis", "Usain Bolt", "Tyson Gay", "Yohan Blake", "B", "Usain Bolt of Jamaica set the 100m world record in Berlin."),
                ("Which country has won the most total Olympic medals in the history of the modern Olympic Games?", "Russia", "China", "United States", "Germany", "C", "The United States leads all nations in total summer & winter Olympic medals."),
                ("Which city hosted the 2012 Summer Olympic Games?", "Beijing", "London", "Rio de Janeiro", "Tokyo", "B", "London hosted the 2012 Summer Olympics."),
                ("How often are the Summer Olympic Games held?", "Every 2 years", "Every 3 years", "Every 4 years", "Every 5 years", "C", "The Summer Olympics occur quadrennially (every 4 years)."),
                ("What color is NOT one of the 5 rings on the official Olympic flag?", "Blue", "Yellow", "Purple", "Green", "C", "The 5 ring colors are Blue, Yellow, Black, Green, and Red (no Purple)."),
                ("What symbolic flame is lit at Olympia, Greece, and carried to the host city before each Games?", "Torch Relay Flame", "Eternal Flame", "Beacon of Peace", "Solstice Flame", "A", "The Olympic Torch Relay carries the flame lit in Ancient Olympia."),
                ("Which athletic field event involves throwing a heavy spherical metal ball as far as possible?", "Discus", "Javelin", "Shot Put", "Hammer Throw", "C", "Shot Put involves pushing ('putting') a heavy metal ball."),
                ("Which track event features runners leaping over 10 fixed barriers during a race?", "Decathlon", "Hurdles", "Steeplechase", "Relay", "B", "Hurdle races require clearing ten barriers along the track."),
                ("How many events comprise a men's Decathlon track and field competition?", "5 events", "7 events", "10 events", "12 events", "C", "A Decathlon consists of 10 combined track and field events.")
            ]
        },
        'Cricket & Global Sports': {
            'description': 'Test your knowledge on Cricket rules, Golf terminology, Formula 1, and global athletic sports.',
            'difficulty': 'Medium',
            'time_limit': 10,
            'pass_mark': 60,
            'questions': [
                ("In Cricket, how many legal deliveries / balls make up one complete 'Over'?", "4 balls", "6 balls", "8 balls", "10 balls", "B", "An Over in cricket consists of 6 legal deliveries bowled from one end."),
                ("In Golf, what term describes scoring two strokes UNDER par on a single hole?", "Birdie", "Eagle", "Albatross", "Bogey", "B", "An Eagle is 2 strokes under par; Birdie is 1 stroke under par."),
                ("In Formula 1 motor racing, what flag is waved to signal the end of the race and victory?", "Yellow Flag", "Red Flag", "Chequered Flag (Black & White)", "Green Flag", "C", "The Chequered Flag signals the winner and end of an F1 race."),
                ("In Cricket, what three wooden posts stuck in the ground with bails on top are defended by batters?", "Stumps / Wickets", "Bases", "Poles", "Gates", "A", "Wickets consist of 3 wooden stumps and 2 bails."),
                ("Which nation won the 2019 ICC Men's Cricket World Cup in a dramatic Super Over finish?", "Australia", "India", "England", "New Zealand", "C", "England won the 2019 ICC World Cup at Lord's against New Zealand."),
                ("In Golf, what term describes completing a hole in one stroke ONE under par?", "Eagle", "Birdie", "Par", "Bogey", "B", "A Birdie is 1 stroke under par for a hole."),
                ("In Rugby Union, how many players are on the field per team?", "11", "13", "15", "18", "C", "Rugby Union matches feature 15 players per side."),
                ("In Badminton, what feather-lined object is hit back and forth across the net instead of a ball?", "Shuttlecock (Birdie)", "Puck", "Squash Ball", "Pelota", "A", "Badminton uses a lightweight Shuttlecock."),
                ("In Swimming, which stroke is performed facing downward with simultaneous arm sweeping and dolphin kick?", "Freestyle", "Backstroke", "Butterfly", "Breaststroke", "C", "The Butterfly stroke uses simultaneous arm recovery and dolphin kicking."),
                ("What major international multi-sport event features athletes with physical disabilities?", "Special Olympics", "Paralympic Games", "World Games", "Commonwealth Games", "B", "The Paralympic Games are held immediately following the Olympic Games.")
            ]
        }
    }
}
