def hello(name = ''):
  if name == '':
    name = 'World'

  print("Hello, {}".format(name))
  return

hello()
hello('Jade')

