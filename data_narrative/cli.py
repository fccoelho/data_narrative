"""Console script for data_narrative."""

import fire


def help() -> None:
    print("data_narrative")
    print("=" * len("data_narrative"))
    print("Tool to generate natural language narrative for a database table")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
