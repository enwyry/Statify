import sys
import time
import builtins

#ALL MADE BY CHATGPT i just wanted nice text

# normal / default print
def nprint(*args, **kwargs):
    builtins.print(*args, **kwargs)


# typed print with inward dash animation
def print(*args, sep=" ", end="\n", delay=0.006, dash_delay=0.06):
    text = sep.join(map(str, args))
    rendered = ""
    i = 0

    while i < len(text):
        # normal characters → typed normally
        if text[i] != "-":
            rendered += text[i]
            sys.stdout.write(text[i])
            sys.stdout.flush()
            time.sleep(delay)
            i += 1
            continue

        # detect continuous dash block
        start = i
        while i < len(text) and text[i] == "-":
            i += 1
        count = i - start

        # inward animation buffer
        buffer = [" "] * count
        left = 0
        right = count - 1

        while left <= right:
            buffer[left] = "-"
            buffer[right] = "-"
            frame = rendered + "".join(buffer)

            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(dash_delay)

            left += 1
            right -= 1

        # settle final dash block
        rendered += "-" * count
        sys.stdout.write("\r" + rendered)
        sys.stdout.flush()

    sys.stdout.write(end)
