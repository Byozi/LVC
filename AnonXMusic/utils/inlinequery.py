from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"Mevcut müziği veya video yayınını durdurur.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"Mevcut müziği veya video yayınını devam ettirir.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"Mevcut müziği veya video yayınını atlar ve bir sonraki parçaya başlar.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="Mevcut müziği veya video yayınını komple kapatır.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="Mevcut müziği veya video yayınını random olarak çalar.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="Mevcut müziği veya video yayınını dönügye alır ve aynı şarkı sürekli oynatılır.",
            thumb_url="https://telegra.ph/file/9796d04afa1dcd73d16da.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
