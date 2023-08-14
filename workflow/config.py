class App:
  __conf = {
    "API_KEY": "",
    "API_SECRET": "",
  }
  __setters = ["API_KEY", "API_SECRET"]

  @staticmethod
  def config(name):
    return App.__conf[name]

  @staticmethod
  def set(name, value):
    if name in App.__setters:
      App.__conf[name] = value
    else:
      raise NameError("Name not accepted in set() method")