#!/usr/bin/env python
import twee_utils

def main():
    passage_header = twee_utils.twee_header_template("Alpha", ["opening", "introduction"], {"author":"Marco Lustri", "date":"6-6-22"})
    twee_utils.render_twee_header("practice.tw", passage_header)
    print(twee_utils.get_UUID())

if __name__ == "__main__":
    main()