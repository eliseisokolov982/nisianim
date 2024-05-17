def intToDecimal(amount, decimals):
  """Converts an integer amount to a decimal string with the specified number of decimals.

  Args:
    amount: The integer amount to convert.
    decimals: The number of decimal places to include in the result.

  Returns:
    A decimal string with the specified number of decimals.
  """

  if decimals <= 0:
    return str(amount)

  factor = 10 ** decimals
  amount_str = str(amount * factor)
  return amount_str[:-decimals] + '.' + amount_str[-decimals:]


amount = intToDecimal(0.00001, 18)
