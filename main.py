import argparse
import re


CHAR_NEVER_USED = "龘"


def _script2subtitles(args):
    # Read script
    with open(args["script_file"]) as f:
        script = f.read()

    # Insert line breaks after ！, ？, ：, ⋯⋯
    for punctuation in ["！", "？", "：", "⋯⋯"]:
        # Temporary replacement for special handling
        for special_ending in ["）", "」"]:
            script = script.replace(punctuation + special_ending, CHAR_NEVER_USED + special_ending)

        script = script.replace(punctuation, punctuation + "\n")

        # Restore special handling
        script = script.replace(CHAR_NEVER_USED, punctuation)

    # Insert line breaks after 。）, 。」, ！）, ！」, ？）, ？」, ⋯⋯）, ⋯⋯」
    for punctuation in ["。）", "。」", "！）", "！」", "？）", "？」", "⋯⋯）", "⋯⋯」"]:
        script = script.replace(punctuation, punctuation + "\n")

    # Replace 。, ； with line breaks
    for punctuation in ["。", "；"]:
        # Temporary replacement for special handling
        for special_ending in ["）", "」"]:
            script = script.replace(punctuation + special_ending, CHAR_NEVER_USED + special_ending)

        script = script.replace(punctuation, "\n")

        # Restore special handling
        script = script.replace(CHAR_NEVER_USED, punctuation)

    # For long lines, replace some ，, 、 with line breaks
    script = list(script)
    line_start_pos = 0
    potential_break_pos = None

    for cursor in range(len(script)):
        char = script[cursor]

        if char == "\n":
            line_start_pos = cursor + 1
            potential_break_pos = None

        line_length = cursor - line_start_pos + 1

        if line_length > args["max_line_length"] and potential_break_pos != None:
            script[potential_break_pos] = "\n"
            line_start_pos = potential_break_pos + 1
            potential_break_pos = None

        if char in ["，", "、"]:
            potential_break_pos = cursor
    
    script = "".join(script)

    # Combine multiple line breaks into one
    script = re.sub("\n+", "\n", script)

    # Write output
    with open(args["subtitles_file"], "w") as f:
        f.write(script)

    print("Done")


def _get_parser():
    parser = argparse.ArgumentParser(description="Auto insert line breaks to a Chinese script to form lines of subtitles")
    parser.add_argument("script_file", help="script text file path")
    parser.add_argument("subtitles_file", help="output subtitles text file path")
    parser.add_argument("--max_line_length", type=int, default=20, help="maximum numer of characters in a line")
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args = vars(parser.parse_args())
    
    _script2subtitles(args)