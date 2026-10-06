from datetime import datetime
import math


def get_current_date() -> str:
    """
    Get the current date.
    Use when the user asks about today's date.
    """

    print("TOOL CALLED: get_current_date")

    return datetime.now().strftime("%Y-%m-%d")


def get_current_time() -> str:
    """
    Get the current local server time.
    Use when the user asks for the current time.
    """

    print("TOOL CALLED: get_current_time")

    return datetime.now().strftime("%H:%M:%S")


def calculate(expression: str) -> str:
    """
    Evaluate a basic mathematical expression.
    Example: 25 * 4 + 10
    """

    print(f"TOOL CALLED: calculate({expression})")

    allowed_names = {
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round,
    }

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            allowed_names,
        )

        return str(result)

    except Exception as exc:
        return f"Calculation failed: {exc}"