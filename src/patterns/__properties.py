"""
patterns > properties

Managing properties of patterns
"""

from fl_model import getState
from fl_model.patterns import getPatternReference


def patternNumber() -> int:
    """Returns the index for the currently active pattern.

    This is the pattern where notes and step sequencing will be modified. It is
    usually equal to the most recently selected pattern. If that pattern is
    deselected, it the pattern number will return to the first selected
    pattern, or if there are no selections, it will remain the same.

    ## Returns:
     * `int`: index of the currently active pattern

    Included since API version 1
    """
    return getState().patterns.active_pattern


def patternCount() -> int:
    """Returns the number of patterns in the project which have been modified
    from their default state.

    ### WARNING:
    There is no guarantee that these patterns are all adjacent, as the API
    allows for the modification of patterns at any index at any time. You
    should only rely on this pattern for indexes if your script manages
    patterns in a responsible manner.

    ## Returns:
    * `int`: the number of patterns

    Included since API version 1
    """
    return len(getState().patterns.p)


def patternMax() -> int:
    """Returns the maximum number of patterns that can be created. In FL Studio
    20, this is 999

    ## Returns:
     * `int`: max number of patterns

    Included since API version 1
    """
    return 999


def getPatternName(index: int) -> str:
    """Returns the name of the pattern at `index`.

    ## Args:
     * `index` (`int`): pattern index

    ## Returns:
     * `str`: name of pattern.

    Included since API version 1
    """
    return ""


def setPatternName(index: int, name: str) -> None:
    """Sets the name of pattern at `index`

    Setting the name to an empty string will reset the name of the pattern to
    its default.

    ## Args:
     * index (`int`): index of pattern

     * name (`str`): new name

    Included since API version 1
    """


def getPatternColor(index: int) -> int:
    """Returns the color of the pattern at `index`.

    ## Args:
     * `index` (`int`): pattern index

    ## Returns:
     * `int`: color of pattern (0x--BBGGRR)

    Included since API version 1
    """
    return 0


def setPatternColor(index: int, color: int) -> None:
    """Sets the color of the pattern at `index`.

    ## Args:
     * `index` (`int`): pattern index

     * `color` (`int`): color of pattern (0x--BBGGRR)

    Included since API version 1
    """


def getPatternLength(index: int) -> int:
    """Returns the length of the pattern at `index` in beats.

    ## Args:
     * `index` (`int`): pattern index

    ## Returns:
     * `int`: length of pattern in beats

    Included since API version 1
    """
    return 0


def jumpToPattern(index: int) -> None:
    """Scroll the patterns list to the pattern at `index`, and select it.

    ## NOTE:
    * It is possible to jump to non-existent patterns. They will be created at
      the requested index. Script writers should be careful not to create
      patterns at unusual indexes. For example, creating a "Pattern 999" as the
      second pattern in a project would be somewhat confusing for user.

    ## Args:
     * index (`int`): pattern index

    Included since API version 1
    """


def findFirstNextEmptyPat(flags: int, x: int = -1, y: int = -1) -> None:
    """Selects the first or next empty pattern.

    ## Args:
     * `flags` (`int`):
          * `FFNEP_FindFirst` (`0`): Find first pattern

          * `FFNEP_DontPromptName` (`1`): Don't prompt pattern name (this
            doesn't seem to work)

     * `x` (`int`, optional): ???. Defaults to -1.

     * `y` (`int`, optional): ???. Defaults to -1.

    Included since API version 1
    """


def isPatternSelected(index: int) -> bool:
    """Returns whether the pattern at `index` is selected.

    ## Args:
     * `index` (`int`): pattern index

    ## Returns:
     * `bool`: whether pattern is selected

    Included since API version 2
    """
    return getState().patterns.p[index].selected


def selectPattern(index: int, value: int = -1, preview: bool = False) -> None:
    """Selects the pattern at `index`.

    ## Args:
     * `index` (`int`): pattern index

     * `value` (`int`, optional): selection mode:
          * `-1`: Toggle (default)

          * `0`: Deselect

          * `1`: Select

     * `preview` (`bool`, optional): whether set FL Studio to pattern mode and
       start playback if the pattern gets selected. Defaults to `False`.

    Included since API version 2
    """
    if value == -1:
        select = not getState().patterns.p[index].selected
    elif value == 0:
        select = False
    elif value == 1:
        select = True
    else:
        raise ValueError(f"Invalid 'value' parameter: {value}")
    getState().patterns.p[index - 1].selected = select
    if select:
        # Set active pattern to this one
        getState().patterns.active_pattern = index
    else:
        # Set active pattern to first active pattern
        for i, p in enumerate(getState().patterns.p):
            i += 1
            if p.selected:
                getState().patterns.active_pattern = i
                break


def selectAll() -> None:
    """Selects all patterns

    Included since API version 2
    """


def deselectAll() -> None:
    """Deselects all patterns

    Included since API version 2
    """


def burnLoop(index: int, storeUndo: int = 1, updateUi: int = 1) -> None:
    """???

    ## HELP WANTED:
    * The documentation for this doesn't make sense.

    ## Args:
     * `index` (`int`): ???

     * `storeUndo` (`int`, optional): ???. Defaults to 1.

     * `updateUi` (`int`, optional): ???. Defaults to 1.

    Included since API version 9
    """
