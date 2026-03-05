The project follows a structured testing approach to ensure reliability and maintainability. This adherees to the standard of Software Testing Levels.

1. Unit Testing
Unit tests isolate the calculation logic from the user interface to ensure each operation functions correctly when in isolation
Tool: Python unittest
Coverage: 8 unit tests that cover all four operations (add, subtract, multiply, divide), and four edge cases (division by zero, negative numbers as inputs, decimals, large numbers)
Execution command: pytest

2. Integration Testing
Integration testing ensurest that the communication between the UI layer and the Logic Layer (main.py and calculator_logic.py) is as expected. The objective of the integration tests was to see if the data flows correctly from user input to the logic module, and that return values are properly handled.

In summary, all the application runs as intended, all functions operate within their scope and the user experience is not unintentionally limited.
