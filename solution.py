def fizz_buzz(value):

  mod = lambda value, number: value % number == 0

  three, five = mod(value, 3), mod(value, 5)

  options = {three: 'fizz', five: 'buzz', three and five: 'fizz_buzz'}

  return(options[True])
