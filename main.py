import logging
from pathlib import Path

from managers.phone_book_manager import PhoneBookManager


def main():
    logging.basicConfig(level=logging.INFO)

    data_dir = Path(__file__).parent / "data"
    manager = PhoneBookManager(
        data_dir=data_dir,
    )
    manager.run()

if __name__ == '__main__':
    main()
