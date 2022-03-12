import datetime as dt

from textode import Back, Func, Keyboard, Text, TO_MAIN


nested_node = Keyboard(
    "Here you are!",
    buttons={
        "Some": Text("Some"),
        "Useless": Text("Useless"),
        "Buttons": Text("Buttons"),
        "Back to main": Back("Returning to main", level=TO_MAIN),
    },
)

nested_keyboard = Keyboard(
    "Wanna see some nested code?",
    buttons={
        "Yes": nested_node,
        "No": Back("Your choice, not mine", level=TO_MAIN),
    },
)

time_node = Func(lambda: dt.datetime.now().strftime("%H:%M:%S"))

help_node = Text("Some long and boring bot instruction...")

main_node = Keyboard(
    "Your main keyboard!",
    buttons={
        "Something interesting goes here...": nested_keyboard,
        "Current time?": time_node,
        "Help!": help_node,
    },
)
