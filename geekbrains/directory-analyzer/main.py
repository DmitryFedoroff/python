from controller.directory_controller import DirectoryController


def main() -> None:
    target_directory = './'
    output_directory = './output'
    controller = DirectoryController(target_directory)
    controller.analyze_and_save(output_directory)


if __name__ == '__main__':
    main()
