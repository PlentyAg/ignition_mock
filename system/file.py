def readFileAsString(file_name):
    file = None
    try:
        file = open(file_name)
        content = file.read()
        return content
    except BaseException, e:
        print('Error occurred while opening a file', e)
    finally:
        if file:
            file.close()
