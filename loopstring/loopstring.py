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

    # 🚀 NEW SHORTCUTS FOR VERSION 0.0.5 🚀
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
