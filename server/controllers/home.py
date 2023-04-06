def home(appRoute):
    return appRoute.send_static_file('index.html')