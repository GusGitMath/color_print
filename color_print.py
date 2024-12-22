class ColorPrint:
    """
    Utility class for printing colored and styled text in the terminal using ANSI escape codes.
    
    Attributes:
        COLORS (dict): Maps color names to their corresponding ANSI escape codes for text colors.
        STYLES (dict): Maps style names to their corresponding ANSI escape codes for text styles.
        HIGHLIGHTS (dict): Maps highlight (background) color names to their corresponding ANSI escape codes.
    """

    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    STYLES = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "reset": "\033[0m"
    }

    HIGHLIGHTS = {
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "reset": "\033[0m"
    }

    @classmethod
    def colorize(cls, text, color=None, style=None, highlight=None):
        """
        Returns the given text wrapped in ANSI codes for color, style, and highlight.

        Args:
            text (str): The text to be colorized.
            color (str, optional): The text color. Should be a key from the COLORS dictionary.
            style (str, optional): The text style. Should be a key from the STYLES dictionary.
            highlight (str, optional): The background color. Should be a key from the HIGHLIGHTS dictionary.

        Returns:
            str: The colorized text with ANSI escape codes.

        Raises:
            ValueError: If invalid color, style, or highlight is provided.
        """
        if color and color not in cls.COLORS:
            raise ValueError(f"Invalid color '{color}'. Valid options are: {list(cls.COLORS.keys())}")
        if style and style not in cls.STYLES:
            raise ValueError(f"Invalid style '{style}'. Valid options are: {list(cls.STYLES.keys())}")
        if highlight and highlight not in cls.HIGHLIGHTS:
            raise ValueError(f"Invalid highlight '{highlight}'. Valid options are: {list(cls.HIGHLIGHTS.keys())}")

        color_code = cls.COLORS.get(color, "")
        style_code = cls.STYLES.get(style, "")
        highlight_code = cls.HIGHLIGHTS.get(highlight, "")
        reset_code = cls.COLORS["reset"]

        return f"{style_code}{color_code}{highlight_code}{text}{reset_code}"

    @classmethod
    def print(cls, text, color=None, style=None, highlight=None, end="\n"):
        """
        Prints the given text with the specified color, style, and highlight.

        Args:
            text (str): The text to print.
            color (str, optional): The text color. Should be a key from the COLORS dictionary.
            style (str, optional): The text style. Should be a key from the STYLES dictionary.
            highlight (str, optional): The background color. Should be a key from the HIGHLIGHTS dictionary.
            end (str, optional): The string appended after the last value, default is a newline ('\n').
        """
        formatted_text = cls.colorize(text, color=color, style=style, highlight=highlight)
        print(formatted_text, end=end)

    @classmethod
    def color_bar(cls, width=60, char="–", color=None, style=None, highlight=None):
        """
        Prints a solid color bar of the specified width using the specified character.

        Args:
            width (int): The width of the color bar in characters.
            color (str, optional): The text color. Should be a key from the COLORS dictionary.
            highlight (str, optional): The background color. Should be a key from the HIGHLIGHTS dictionary.
            char (str, optional): The character to use for the bar. Default is a space (' ').
        
        Raises:
            ValueError: If invalid color, highlight, or char is provided.
        """
        if color and color not in cls.COLORS:
            raise ValueError(f"Invalid color '{color}'. Valid options are: {list(cls.COLORS.keys())}")
        if highlight and highlight not in cls.HIGHLIGHTS:
            raise ValueError(f"Invalid highlight '{highlight}'. Valid options are: {list(cls.HIGHLIGHTS.keys())}")
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError("Character for the bar must be a single character string.")

        bar_text = char * width
        print(cls.colorize(bar_text, color=color, style=style, highlight=highlight))

# # Usage Examples
# if __name__ == "__main__":
#     ColorPrint.print("Hello, World!")
#     ColorPrint.print("Bold Blue Text", color="blue", style="bold")
#     ColorPrint.print("Underlined Green Text", color="green", style="underline")
#     ColorPrint.print("Highlighted Yellow with Bold", color="white", style="bold", highlight="yellow")
#     ColorPrint.print("Background", highlight="red")
#     ColorPrint.color_bar()
#     ColorPrint.color_bar(30, highlight="green", char="-")