"""Plugins Module (FL Studio built-in)

Handles the way that scripts communicate with and control FL Studio plugins,
including 3rd-party VST/AU plugins. The module allows scripts to get and set
parameter values for plugins on the mixer and the channel rack.

## Working with indexes

Almost all of the functions in this module accept an `index` and a `slotIndex`
parameter, which are used to determine which plugin to interact with.

* `index` either refers to the index of the plugin on the channel rack, or the
  index of the mixer track containing the plugin on the mixer. Note that the
  grouped index is used, rather than a global index on the channel rack.

* `slotIndex` refers the the mixer slot of the plugin if it is on the mixer.
  Leave this parameter unset, or set it to `-1` if the plugin is on the channel
  rack.

Tuple packing and unpacking can be used to simplify this process if your
script uses these variables a lot.

```py
# A plugin on channel 42
index1 = (42,)
# A plugin on mixer track 12, in slot 5
index2 = (12, 5)

# If you use the unary `*` operator, the tuple is unpacked to take up multiple
# arguments. Both of these function calls work correctly.
plugins.isValid(*index1)
plugins.isValid(*index2)
```

Note that this may be unreliable if you are also specifying `useGlobalIndex`

## Interacting with VST plugins

VST plugins can behave somewhat unintuitively as a result of the system that FL
Studio uses for parameter mapping. In the VST specification, all VSTs have 4096
parameters available to use, but aren't required to use all of them. Unused
parameters are hidden in FL Studio's UI, but they are accessible through the
API - their returned names will be an empty string. However, there are actually
144 more parameters available. These are the 128 CC parameters from indexes
4096-4223 and the 16 channel after-touch parameters from indexes 4224-4239.

Module added in API version 8.
"""
from fl_model.decorators import since
import midi


@since(8)
def isValid(
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> bool:
    """Returns whether there is a valid plugin at `index`/`slotIndex`.

    ## Notes
    * Audio samples are not considered to be plugins in FL Studio.

    ## Args:
    * `index` (`int`): index on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
     * `bool`: whether there is a valid plugin at `index`.

    Included since API version 8
    """
    return False


@since(12)
def getPluginName(
    index: int,
    slotIndex: int = -1,
    userName: bool = False,
    useGlobalIndex: bool = False,
) -> str:
    """Returns the name of the plugin at `index`/slotIndex`. This returns the
    original plugin name if `userName` is `False`, otherwise the name of the
    plugin as set by the user.

    ## Args:
    * `index` (`int`): index on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `userName` (`bool`, optional): whether to return the user's name for the
      plugin (`True`), or the default name for the plugin (`False`). Defaults
      to `False`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
     * `str`: plugin name

    Included since API version 8, with `userName` parameter added in API version
    12
    """
    return ""


@since(8)
def getParamCount(
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> int:
    """Returns the number of parameters that the plugin at `index`/`slotIndex`
    has.

    ## NOTE:
    * VST plugins are listed as having `4240` parameters, but not all of
      these are necessarily used by the plugin. The first `4096` are for
      parameters, then the next `128` are used for MIDI CC sends `0` to `127`.
      The final `16` are used for after-touch on each MIDI channel.

    ## Args:
    * `index` (`int`): index on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
    * `int`: number of parameters

    Included since API version 8
    """
    return 0


@since(8)
def getParamName(
    paramIndex: int,
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> str:
    """Returns the name of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## WARNING:
    * In API versions < v20, FL Studio's Python environment will crash if an
      invalid paramIndex is provided to this function.

    ## Args:
    * `paramIndex` (`int`): index of parameter

    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
    * `str`: name of parameter

    Included since API version 8
    """
    return ""


@since(8)
def getParamValue(
    paramIndex: int,
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> float:
    """Returns the value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## Warnings:
    * In API versions < v20, the return values of this function for VST plugins
      seem to be very broken, often being incorrect by orders of magnitude.

    * This appears to have poor performance, being 40x slower than many other
      functions that interact with plugins.

    ## Args:
    * `paramIndex` (`int`): index of parameter

    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
    * `float`: parameter value, between `0.0` and `1.0`

    Included since API version 8
    """
    return 0.0


@since(8)
def setParamValue(
    value: float,
    paramIndex: int,
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """Sets the value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## Warnings:
    * This appears to have poor performance before FL Studio 21, being 40x
      slower than many other functions that interact with plugins.

    ## Args:
    * `value` (`float`): new value of parameter (between `0.0` and `1.0`)

    * `paramIndex` (`int`): index of parameter

    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    Included since API version 8
    """


@since(8)
def getParamValueString(
    paramIndex: int,
    index: int,
    slotIndex: int = -1,
    pickupMode: int = midi.PIM_None,
    useGlobalIndex: bool = False,
) -> str:
    """
    Returns a string value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`. This function is only supported by some FL Studio
    plugins.

    TODO: Find plugins

    ## WARNING:
    * In API versions < v20, FL Studio's Python environment will crash if an
      invalid paramIndex is provided to this function.

    ## Args:
    * `paramIndex` (`int`): index of parameter

    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
     * `str`: string parameter value

    Included since API version 8
    """
    return ""


@since(12)
def getColor(
    index: int,
    slotIndex: int = -1,
    flag: int = midi.GC_BackgroundColor,
    useGlobalIndex: bool = False,
) -> int:
    """Returns various plugin color parameter values for the plugin at
    `index`/`slotIndex`.

    ## Args:
    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `flag` (`int`, optional): color type to return:
          * `GC_BackgroundColor` (`0`, default): The darkest background color
          of the plugin.

          * `GC_Semitone` (`1`): Retrieves semitone color (in FPC, returns
            color of drum pads).

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
    * `int`: color (`0x--BBGGRR`)

    Included since API version 12
    """
    return 0


@since(13)
def getName(
    index: int,
    slotIndex: int = -1,
    flag: int = midi.FPN_Param,
    paramIndex: int = 0,
    useGlobalIndex: bool = False,
) -> str:
    """Returns various names for parts of plugins for the plugin at
    `index`/`slotIndex`.

    ## HELP WANTED:
    * Explanation of `flag` values from `3` onwards, excluding `6`.
    * Fixing the markdown formatting here: I can't get it to behave in VS Code.

    ## Args:
    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `flag` (`int`, optional): name type to return. Names marked with a `!`
      require the `paramIndex` parameter in order to work correctly.
          * `FPN_Param` (`0`, default) `*` : Name of plugin parameter.
              * Eg: `"Expression"`

          * `FPN_ParamValue` (`1`) `*` : Text value of plugin parameter.
              * Eg: `"62%"`

          * `FPN_Semitone` (`2`) `*` : Name of note as defined by plugin.
              * `paramIndex` should be the note number (eg `60` for middle C)

              * If note names aren't defined by the plugin, an empty string is given.

              * Eg: `"Kick"`

          * `FPN_Patch` (`3`): Name of the patch defined by plugin?

          * `FPN_VoiceLevel` (`4`) `*` : Name of per-voice parameter defined by plugin

          * `FPN_VoiceLevelHint` (`5`) `*` : Hint for per-voice parameter defined by plugin

          * `FPN_Preset` (`6`) `*` : For plugins that support internal presets, the name of the preset at `paramIndex`.
              * Eg: `"Dystopian lead"`

          * `FPN_OutCtrl` (`7`): For plugins that output controllers, the name of the output controller?

          * `FPN_VoiceColor` (`8`): Name of per-voice color
              * `paramIndex` as MIDI channel?

          * `FPN_VoiceColor` (`9`): For plugins that output voices, the name of output voice
              * `paramIndex` as voice number?

    * `paramIndex` (`int`, optional): index required by requested flag (if
      necessary)

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
     * `str`: name of requested parameter

    Included since API version 13
    """
    return ""


@since(19)
def getPadInfo(
    chanIndex: int,
    slotIndex: int = -1,
    paramOption: int = 0,
    paramIndex: int = -1,
    useGlobalIndex: bool = False,
) -> int:
    """
    Returns info about drum pads

    Currently only supported by FPC

    ## Note:
    * The official documentation lists this as returning a string, but it
      actually returns an int.

    ## Args:
    * `chanIndex` (`int`): channel of plugin to check

    * `slotIndex` (`int`, optional): slot of mixer track plugin. Defaults to `-1`.

    * `paramOption` (`int`, optional): type of query:
          * `0`: number of pads (note: given number is one greater than there
            actually are, ie. FPC has 32 pads but 33 is returned)

          * `1`: semitone number of pad (use `paramIndex`)

          * `2`: color of pad as 0xBBGGRR (use `paramIndex`)

    * `paramIndex` (`int`, optional): drum pad number (0-indexed)

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    ## Returns:
    * `int`: number of parameters, or

    * `int`: note number of pad, or

    * `int`: color of pad

    Included since API Version 19
    """
    return 0


@since(15)
def getPresetCount(
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> int:
    """Returns the number of presets available for the selected plugin.

    ## Args:
    * `index` (`int`): index of plugin on channel rack or mixer.

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    Included since API version 15
    """
    return 0


@since(10)
def nextPreset(
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """Navigate to the next preset for plugin at `index`/`slotIndex`.

    ## Args:
    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    Included since API version 10
    """


@since(10)
def prevPreset(
    index: int,
    slotIndex: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """Navigate to the previous preset for plugin at `index`/`slotIndex`.

    ## Args:
    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to `-1`.

    * `useGlobalIndex` (`bool`, optional): whether to use global channel
      indexes when modifying plugins on the channel rack. Defaults to `False`.

    Included since API version 10
    """
