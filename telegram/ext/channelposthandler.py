from telegram import Update
from telegram.utils.deprecate import deprecate
from .handler import Handler


class ChannelPostHandler(Handler):
    def check_update(self, update):
        return isinstance(update, Update) and update.channel_post

    def handle_update(self, update, dispatcher):
        return self.callback(dispatcher.bot, update)

    m = "telegram.ChannelPostHandler."
    checkUpdate = deprecate(check_update, m + "checkUpdate", m + "check_update")
    handleUpdate = deprecate(handle_update, m + "handleUpdate", m + "handle_update")
