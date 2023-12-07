## Multilingual Greetings with Decorative Display

This Python script generates multilingual greetings with decorative patterns. Let's dive into the breakdown of its structure and functionalities:

### Initialization

- `decor_symbols`: Contains a set of decorative symbols used to embellish the greetings.
- `languages`: Consists of the names of various languages.
- `greetings`: Stores greeting messages in multiple languages.

### Functions

- `random_number(limit)`: Generates a random number between 0 and `limit-1`.
- `decorate(func, lang, index, index2, spacing)`: A decorator function that decorates greetings with patterns. It uses the `decor_symbols` to create visual patterns around the greetings.
- `display_text(spaces, idx)`: Prints a greeting message from the `greetings` list with a specified number of spaces before it.

### Execution

The script iterates through the `languages` list, applying a randomly selected decorative symbol from `decor_symbols` to each language's greeting using the `decorate` decorator function. The greetings are printed with decorative patterns, creating an aesthetically appealing output.

### Enhancements

Consider adding comments throughout the code to explain individual sections or functions in more detail. This can enhance readability and help others understand the code's functionality more easily. Additionally, providing examples or use cases showcasing the script's output could be beneficial.
