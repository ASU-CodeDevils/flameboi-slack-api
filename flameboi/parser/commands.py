"""
TODO: Implement and interface/lib that will load/run the different functionality moduels
"""


def send_chat(chan: str, txt: str, bot):
    response = bot.chat_postMessage(
        channel=chan,
        text=txt,
    )
    assert response["ok"]


def send_thread(chan, txt, ts, bot):
    response = bot.chat_postMessage(
        channel=chan,
        text=txt,
        thread_ts=ts,
    )
    assert response["ok"]


def send_react(chan, ts, emote, bot):
    response = bot.reactions_add(
        channel=chan,
        timestamp=ts,
        name=emote,
        )
    assert response["ok"]


commands = {
    "send_chat": send_chat,
    "send_thread": send_thread,
    "send_react": send_react,
}
