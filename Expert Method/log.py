import os


class Log:
    def executionLog(toLog):
        return
        Log.__checkDir("Expert Method\\Logs")
        with open("Expert Method\\Logs\\execution_log.txt", "a", encoding="UTF8") as log:
            log.write(f"{toLog}\n")

    def __checkDir(directory):
        return
        directory = directory.split("\\")
        if directory not in os.listdir():
            os.mkdir(directory)
