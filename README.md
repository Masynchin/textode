# textode

Textode is a simple tool to create text bots with only one handler.
You can use it for Telegram, VK or any other social network.

## What is it for

Textode helps you build **static text bots**.

**Static text bots** are bots that has concrete structure, like instruction
on the pill bottle or a movie script. So, perfect examples of what you can do
with this library is instruction bots, text quests, and so on.

## What is it not for

It is not designed to build bots that use data provided by user
(e.g. store user age).

## What is the idea

In textode the main part of the bot is Node. It used to build bot structure.

For example, this is the basic bot in textode:
~~~python
Keyboard(
    "Hello! Here is your keyboard.",
    buttons={
        "About bot": Text("*about*"),
        "Bot logo": Image("logo.png"),
    },
)
~~~

With this structure bot handles "/start" message, responses with
"Hello! Here is your keyboard." text and keyboard of two buttons -
"About bot" that sends text about bot and "Bot logo" that sends image
of bot logo.

The main advantage of this approach is that your bot is now defined by
concrete schema. Instead of making handlers you are designing Node structure.

Another advantage is that instead of many handlers you now have one.
It works because of Node identity, they all have the same basic fields:

- title (by parent) - message text that triggers node.
- text - text that sends back.

Because of that, you need to make only one handler that picking right node
(depends on user input), handles if there is no node with this text, or
handles node type (sends keyboard for Keyboard, image for ImageNode etc.).

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
