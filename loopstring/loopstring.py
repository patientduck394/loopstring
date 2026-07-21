class FG:
    """Foreground text colors"""
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

class BG:
    """Background colors"""
    BLACK   = "\033[40m"
    RED     = "\033[41m"
    GREEN   = "\033[42m"
    YELLOW  = "\033[43m"
    BLUE    = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN    = "\033[46m"
    WHITE   = "\033[47m"
    RESET   = "\033[49m"

class FORMAT:
    """Formatting tags"""
    BOLD = '\033[1m' # Bold
    DIM = '\033[2m' # Dim
    ITALIC = '\033[3m' # Italic
    UNDERLINE = '\033[4m' # Underline
    REVERSE = '\033[7m' # Reverse video
    STRIKETHROUGH = '\033[9m' # Strikethrough
    RESET   = "\033[39m"

class BOXES:
    @staticmethod
    def draw_box(text: str, style: str = 'light') -> str:
        """Wraps text inside a customizable Unicode box.
    
        Supported styles: 'light', 'heavy', 'double', 'rounded', 'dashed'
        """
        # ... keep all your existing draw_box code exactly the same ...
        glyphs = {
            'light':   {'h': '─', 'v': '│', 'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘'},
            'heavy':   {'h': '━', 'v': '┃', 'tl': '┏', 'tr': '┓', 'bl': '┗', 'br': '┛'},
            'double':  {'h': '═', 'v': '║', 'tl': '╔', 'tr': '╗', 'bl': '╚', 'br': '╝'},
            'rounded': {'h': '─', 'v': '│', 'tl': '╭', 'tr': '╮', 'bl': '╰', 'br': '╯'},
            'dashed':  {'h': '┄', 'v': '┆', 'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘'}
        }
        g = glyphs.get(style.lower(), glyphs['light'])
        lines = text.split('\n')
        max_width = max(len(line) for line in lines) if lines else 0
        box = []
        box.append(f"{g['tl']}{g['h'] * (max_width + 2)}{g['tr']}")
        for line in lines:
            box.append(f"{g['v']} {line.ljust(max_width)} {g['v']}")
        box.append(f"{g['bl']}{g['h'] * (max_width + 2)}{g['br']}")
        return '\n'.join(box)

    @staticmethod
    def rounded(text: str) -> str:
        """Shortcut to draw a rounded box."""
        return BOXES.draw_box(text, style='rounded')

    @staticmethod
    def heavy(text: str) -> str:
        """Shortcut to draw a heavy box."""
        return BOXES.draw_box(text, style='heavy')

    @staticmethod
    def double(text: str) -> str:
        """Shortcut to draw a double box."""
        return BOXES.draw_box(text, style='double')

    @staticmethod
    def dashed(text: str) -> str:
        """Shortcut to draw a dashed box."""
        return BOXES.draw_box(text, style='dashed')

    
class SYMBOLS:
    """Cool symbols for layouts, dashboards, and loading bars!"""
    # Original Symbols
    HEXAGON = '⬢' 
    PENTAGON = '⬟' 
    STAR = '⭑' 
    DOWNLOAD = '⤓' 
    LIGHTSHADE = '░'
    MEDIUMSHADE = '▒'
    DARKSHADE = '▓'
    FULLSHADE = '█'
    PHONE = '☎'
    PENTAGONARROW = '⭔'
    ENTERKEY = '⏎'
    CHECKMARK = '✓'
    SPACEBAR = '␣'
    THINSQUARE = '⌷'
    SLOPE = '⌳'
    FILLEDRIGHTTRIANGLE = '▶'
    RIGHTTRIANGLE = '▷'
    ASTROIDSTAR = '✦'

    MONITOR = '🖵'          # U+1F5B5 - Physical monitor screen layout
    CLEAR_SCREEN = '⎚'     # U+239A - Classic wipe/clear screen icon
    PROMPT = '❯'           # U+276F - Modern CLI input hook
    NETWORK = '🛜︎'          # U+1F6DC - Wi-Fi/Network status indicator

    FILL_1_8 = '▏'         # U+258F - Left 1/8 block fill
    FILL_1_4 = '▎'         # U+258E - Left 1/4 block fill
    FILL_HALF = '▌'        # U+258C - Left half block fill
    FILL_3_4 = '▊'         # U+258A - Left 3/4 block fill

    FOLDER_CLOSED = '🗀'   # U+1F5C0 - Closed directory item
    FOLDER_OPEN = '🗁'     # U+1F5C1 - Expanded directory folder
    DOCUMENT = '🖹'        # U+1F5B9 - Log/Text file symbol
    TRASH = '🗑︎'           # U+1F5D1 - Delete/Erase storage indicator

    LOOP_INFINITY = '∞'    # U+221E - Infinity track loop
    LOOP_SINGLE = '➰︎'      # U+27B0 - Light curly loop curl
    LOOP_DOUBLE = '➿︎'      # U+27BF - Double curly loop hook
    LOOP_REFRESH = '⥁'     # U+2941 - Circular reload sequence

    SCALES = '⚖'

class TITLES:
    @staticmethod
    def draw_divider(text, style="box"):
        if style == "box":
            return(f"▌[{text}]▐")
        elif style == "server":
            return(f"╽ {text} ╿")
        elif style == "pixel":
            return(f"▀▄ {text} ▄▀")
        elif style == "shade":
            return(f"░▒▓█ {text} █▓▒░")
        elif style == "angle_bracket":
            return(f"❬ {text} ❭")
        elif style == "boxed":
            return(f"┍[ {text} ]┑")
        elif style == "bullet":
            return(f"⁌ {text} ⁍")
        elif style == "dotted_line":
            return(f"⁞ {text} ⁞")
        elif style == "mini_triangle":
            return(f"◂ {text} ▸")
        elif style == "science":
            return(f"⚗⚛ {text} ⚛⚗")
        elif style == "line":
            return(f"── {text} ──")
        
class DIVIDERS:
    @staticmethod
    def draw_divider(length, style="box"):
        if style == "stripes":
            return("▌" * length)
        elif style == "server":
            return("╽╿" * length)
        elif style == "pixel":
            return("▀▄" * length)
        elif style == "shade":
            return(("░▒▓█") + ("█" * length) + ("█▓▒░"))
        elif style == "angle_bracket":
            return("❭" * length)
        elif style == "grass":
            return("v" * length)
        elif style == "full_block":
            return("█" * length)
        elif style == "dotted_line":
            return("⁞" * length)
        elif style == "square_wave":
            return("⎍" * length)
        elif style == "light_shade":
            return("░" * length)
        elif style == "medium_shade":
            return("▒" * length)
        elif style == "dark_shade":
            return("▓" * length)
        elif style == "line":
            return("─" * length)
        elif style == "cloud":
            return("C" + ("⁐" * length) + "Ↄ")

class MULTI_INPUT_MATRICES:
    @staticmethod
    def draw_matrix(text1, text2, text3, matrixType="square"):
        """
        Draws matrices with three text parameters.
        Available in 3 styles:
        - Square
        - Rounded
        - Curly
        """
        # Combine inputs to find the maximum string length efficiently
        texts = [text1, text2, text3]
        biggestLength = max(len(t) for t in texts)
        
        # Dynamically pad each text string to match the longest one
        padded_texts = [t.ljust(biggestLength) for t in texts]
        
        if matrixType == "square":
            # Brackets now dynamically scale based on the largest input width
            topBracket    = "⎡ " + padded_texts[0] + " ⎤"
            middleBracket = "⎢ " + padded_texts[1] + " ⎥"
            bottomBracket = "⎣ " + padded_texts[2] + " ⎦"
        elif matrixType == "rounded":
            topBracket    = "⎧ " + padded_texts[0] + " ⎫"
            middleBracket = "⎪ " + padded_texts[1] + " ⎪"
            bottomBracket = "⎩ " + padded_texts[2] + " ⎭"
        elif matrixType == "curly":
            topBracket    = "⎧ " + padded_texts[0] + " ⎫"
            middleBracket = "⎨ " + padded_texts[1] + " ⎬"
            bottomBracket = "⎩ " + padded_texts[2] + " ⎭"
            
        return topBracket + "\n" + middleBracket + "\n" + bottomBracket + "\n"

class MATRICES:
    @staticmethod
    def draw_matrix(text, matrixType="square"):
        """
        Draws matrices with one text parameter.
        Available in 3 styles:
        - Square
        - Rounded
        - Curly
        """
        textLength = 0
        textLength = len(text)
        if matrixType == "square":
            topBracket = "⎡" + ((" " * textLength) + "  ") + "⎤"
            middleBracket = "⎢" + (" " + text + " ") + "⎥"
            bottomBracket = "⎣" + ((" " * textLength) + "  ") + "⎦"
        elif matrixType == "rounded":
            topBracket = "⎧" + ((" " * textLength) + "  ") + "⎫"
            middleBracket = "⎪" + (" " + text + " ") + "⎪"
            bottomBracket = "⎩" + ((" " * textLength) + "  ") + "⎭"
        elif matrixType == "curly":
            topBracket = "⎧" + ((" " * textLength) + "  ") + "⎫"
            middleBracket = "⎨" + (" " + text + " ") + "⎬"
            bottomBracket = "⎩" + ((" " * textLength) + "  ") + "⎭"
        
        return((topBracket + "\n") + (middleBracket + "\n") + (bottomBracket + "\n"))
    

class WRITEDOWN:
    def format_writedown(writedown_text):
        """
        Parses standard Writedown (a Markdown modification) syntax string formatting loops and translates
        them directly into terminal screen Colorama escape styles.
        """
        lines = writedown_text.split(r"\n") # Splits text lines accurately
        
        
        
        for line in lines:
            processed_line = line.strip()
            
            # 1. Parse # Headers -> Bright Cyan Bold
            if processed_line.startswith("# "):
                processed_line = "\033[36m" + "\033[1m" + "▶ " + processed_line[2:].upper()
            # 2. Parse ##  and ### Headers -> Bright White Bold
            elif processed_line.startswith("## "):
                processed_line = "\033[36m" + "\033[1m" + "▷ " + processed_line[3:]
            elif processed_line.startswith("### "):
                processed_line = "\033[36m" + "‣ " + processed_line[4:]
            # 3. Parse * Bullet points -> Green Bullet Indent
            elif processed_line.startswith("* "):
                processed_line = "  " + "\033[32m" + "• " + "\033[37m" + processed_line[2:]
            elif processed_line.startswith("- "):
                processed_line = "  " + "\033[32m" + "- " + "\033[37m" + processed_line[2:]
            elif processed_line.startswith("> "):
                processed_line = "  " + "\033[33m" + "‣ " + "\033[37m" + processed_line[2:]
            elif processed_line.startswith("1. "):
                processed_line = "  " + "\033[31m" + "1. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("2. "):
                processed_line = "  " + "\033[31m" + "2. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("3. "):
                processed_line = "  " + "\033[31m" + "3. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("4. "):
                processed_line = "  " + "\033[31m" + "4. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("5. "):
                processed_line = "  " + "\033[31m" + "5. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("6. "):
                processed_line = "  " + "\033[31m" + "6. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("7. "):
                processed_line = "  " + "\033[31m" + "7. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("8. "):
                processed_line = "  " + "\033[31m" + "8. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("9. "):
                processed_line = "  " + "\033[31m" + "9. " + "\033[37m" + processed_line[3:]
            elif processed_line.startswith("10. "):
                processed_line = "  " + "\033[31m" + "10. " + "\033[37m" + processed_line[4:]
                
            # 4. Parse Inline **Bold** markers using colorama replacements
            while "**" in processed_line:
                processed_line = processed_line.replace("**", "\033[33m" + "\033[1m", 1).replace("**", "\033[0m" + "\033[37m", 1)
                
            # 5. Parse Inline *Italic* markers (we can use Underline style for italics in terminal layouts)
            while "*" in processed_line:
                processed_line = processed_line.replace("*", "\033[4m", 1).replace("*", "\033[24m", 1)
                
            # 6. Parse Inline `Code` markers -> Magenta text style
            while "`" in processed_line:
                processed_line = processed_line.replace("`", "\033[35m", 1).replace("`", "\033[37m", 1)
            
            while "=Y=" in processed_line:
                processed_line = processed_line.replace("=Y=", "\033[43m", 1).replace("=Y=", "\033[0m", 1)

            while "=R=" in processed_line:
                processed_line = processed_line.replace("=R=", "\033[41m", 1).replace("=R=", "\033[0m", 1)
            
            while "=G=" in processed_line:
                processed_line = processed_line.replace("=G=", "\033[42m", 1).replace("=G=", "\033[0m", 1)
            
            while "=C=" in processed_line:
                processed_line = processed_line.replace("=C=", "\033[46m", 1).replace("=C=", "\033[0m", 1)
            
            while "=B=" in processed_line:
                processed_line = processed_line.replace("=B=", "\033[44m", 1).replace("=B=", "\033[0m", 1)

            return("\033[0m" + processed_line + "\033[0m")
