from textwrap import dedent

INDENTS = 4

def print_hanging_indents(poem: str):
    shouldIndent = False
    lines: list = dedent(poem).splitlines()
    poem = ''
    for line in lines:
        if line == '':
            shouldIndent = False
            continue
        if shouldIndent:
            poem += ' ' * INDENTS
        else:
            shouldIndent = True
        poem += line + '\n'
    print(poem)
    
if __name__ == '__main__':
    rosetti_unformatted = """
                        Remember me when I am gone away,
                        Gone far away into the silent land;
                        When you can no more hold me by the hand,

                        Nor I half turn to go yet turning stay.

                        Remember me when no more day by day
                        You tell me of our future that you planned:
                        Only remember me; you understand
                        """
    rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""
    print_hanging_indents(rosetti_unformatted)
    print(rosetti_formatted)