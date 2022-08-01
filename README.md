# textode

[![Latest PyPI package version](https://badge.fury.io/py/textode.svg)](https://badge.fury.io/py/textode)

Textode is a simple tool to create stateless dialogs.
You can use it for bulding bots, text quests, instructions and so on.

## What is it for

Textode helps you build **stateless dialogs**.

**Stateless dialogs** are dialogs that has no state.
Thus, it will help you build some dialog-based system
where all possible questions and answers are known before system run.

Even through it has some features to bring interractive elements
(such as `Func` node), it doesn't designed to have any state.

## What is it not for

It is not designed to build dialogs that has state.
It means that it can't operate with runtime-provided data
(e.g. store user credentials).

## What is the idea

The main idea is of textode is about creating dialog scheme.
In textode dialog is tree of questions and answers.
Here is the basic example:

~~~mermaid
flowchart TD;
    Main["*dialog start*"];
    About["Text description of what this bot can do"];
    Logo["Image of bot logo"];

    Main -->|"About bot"| About;
    Main -->|"Bot logo"| Logo;
~~~

This dialog includes this states:

- Start - in response dialog shows possible options to go through.

- About bot - in response dialog shows description of bot.
  User stays in start state since there are no other possible
  states after this state.

- Bot logo - in response dialog shows picture with bot logo.
  User also stays in start state same as with "About bot".

Here is how it can be represented with textode:

~~~python
Keyboard(
    "Hello! Starts the dialog. Choose what you want to know about:",
    buttons={
        "About bot": Text("*about*"),
        "Bot logo": Image("logo.png"),
    },
)
~~~

Here `Keyboard` is node with some children.
It is named like that because in many bots it
can be represented with keyboard.

The main advantage of this approach is that your dialog
is now defined by concrete schema. There is no need to write
any extra functions to handle transitions between states.

You need only one handler which connects user with this dialog.
This handler check if there is node with matching text or not.
Then you can send response. That is how handler runs dialog.

## Installation

via pip:

`pip install textode`

or poetry:

`poetry add textode`

## Examples

Look [here](examples) for usage examples
([aiogram](https://github.com/aiogram/aiogram) and
[vkbottle](https://github.com/vkbottle/vkbottle) are presented)
with schemas (built by [Graphviz](https://graphviz.org/)
with [JetBrains Mono](https://www.jetbrains.com/lp/mono/) font).

## Projects that use Textode

Are you using Textode? Please consider opening a pull request to list your project here:

- [PFR Instruction](https://github.com/bullbesh/pfr_instruction)
