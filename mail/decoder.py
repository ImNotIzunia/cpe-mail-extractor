from email.header import decode_header

def decode(value: str | None) -> str:
    if not value:
        return ""
    
    parts = decode_header(value)

    result = ""

    for text, encoding in parts:
        if isinstance(text, bytes):
            result += text.decode(
                encoding or "utf-8",
                errors="replace"
            )
        else:
            result += text

    return result

