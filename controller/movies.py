import model.hello as model

def getFunc():
    return model.getFunc()
    pass

def postFunc(data = ''):
    print('poster')
    return f'Post Function with {data}'
    pass