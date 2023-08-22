class App:
  __conf = {
    "API_KEY": "3a80dca2bb1308f8f6d224e6cadd8499c31110109b2341a56925829196f0fe2f",
    "API_SECRET": "a83970bd48beae08aec9754baba497ebb902084aa4cd693038d7e1c576509695",
  }
#  __conf = {
#    "API_KEY": "89d10fd21d36daf2c00038768be515bfbedd18b4386cf3c0dabefc62ff1b4fce",
#    "API_SECRET": "0fb7bbcddb33d0db17cb067bc3ab3c0c8066bab4c8defd8c76c0c1d52600890e",
#  }

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
    