"""
general > __fl_state

Functions to do with the state of FL Studio
"""
from fl_model import getState
from fl_model.decorators import since


def getRecPPB() -> int:
    """Returns the current timebase (PPQN) multiplied by the number of beats in
    a bar.

    ## NOTE:
    * This DOES NOT respect time signature markers

    ## Returns:
     * `int`: timebase * numerator

    Included since API version 1
    """
    return 0


@since(8)
def getRecPPQ() -> int:
    """Returns the current timebase (PPQN)

    ## Returns:
     * `int`: timebase

    Included since API version 8
    """
    return 0


def getUseMetronome() -> bool:
    """Returns whether the metronome is active

    ## Returns:
     * `bool`: metronome enabled

    Included since API version 1
    """
    return False


def getPrecount() -> bool:
    """Returns whether precount before recording is enabled

    ## Returns:
     * `bool`: precount before recording

    Included since API version 1
    """
    return False


def getChangedFlag() -> int:
    """Returns whether a project has been changed since the last save

    ## Returns:
     * `int`: changed flag:
          * `0`: Unchanged since last save

          * `1`: Changed since last save

          * `2`: Changed since last save, but unchanged since last auto-save

    Included since API version 1
    """
    return 0


def getVersion() -> int:
    """Returns MIDI Scripting API version number. Note that this is the API
    version, rather than the FL Studio version.

    To get the version of FL Studio, use [`ui.getVersion()`][ui.getVersion]
    instead.

    ## Returns:
     * `int`: version number

    Included since API version 1
    """
    return getState().general.api_version


@since(7)
def processRECEvent(eventId: int, value: int, flags: int) -> int:
    """Processes a REC event, usually changing an automatable value.

    ## Try to achieve your task with other API functions first!

    This part of FL's scripting API is incomplete, poorly documented, and
    filled with hidden bugs. REC events expose more controls inside FL Studio,
    while being *much* more confusing than other parts of the API.

    "REC events" represent every automatable control in FL studio.
    Each "REC" is identified with a unique integer, "event ID".
    FL Studio reserves a range of event IDs for each channel, mixer track, plugin,
    and so on.

    REC events have some other properties available:

    * Descriptive name: [`device.getLinkedParamName()`][device.getLinkedParamName]

    * Current value: [`device.getLinkedValue()`][device.getLinkedValue]

    * Current value as an appropriately formatted string:
      [`device.getLinkedValueString()`][device.getLinkedValueString]

    ## HELP WANTED:
    * More information from Image-Line? More details on what `flags` can do?

    ## Args:
     * `eventId` (`int`): Refer to the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventParams)

     * `value` (`int`): value of even within a range. This range depends on the
       plugin, but you can specify for it to be between `0 - 2^30` by using the
       `midi.REC_MIDIController` flag. Note that providing an invalid value can
       lead to very strange behavior and sometimes crashes.

     * `flags` (`int`): Refer to the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#RecEventFlags)

    ## Returns:
     * `int`: Unknown

    Included since API version 7
    """
    return 0


@since(15)
def dumpScoreLog(time: int, silent: bool = False) -> None:
    """
    Write recently played MIDI to the selected pattern.

    ## Args:
     * `time` (`int`): The duration of time to write, from `time` seconds
       before the last note played, to the last note.

     * `silent` (`int`): Whether the empty score message is suppressed (`True`)
       or not (`False`)

    Included since API version 15
    """


@since(15)
def clearLog() -> None:
    """Clear the score log

    Included since API version 15
    """
